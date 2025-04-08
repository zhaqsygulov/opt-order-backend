
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update
from app.database import get_session
from app.models import VendorContext, VendorLog
from app.schemas import VendorRequest
import httpx
import uuid
import datetime

router = APIRouter()

@router.put("/vendor/apps/{app_id}/{account_id}")
async def activate_app(app_id: str, account_id: str, body: VendorRequest, session: AsyncSession = Depends(get_session)):
    token = body.access[0].access_token
    context = {
        "account_id": body.accountId,
        "access_token": token,
        "context_id": body.contextId,
        "employee_id": body.employeeId,
        "org_id": body.orgId
    }

    stmt = select(VendorContext).where(VendorContext.account_id == body.accountId)
    result = await session.execute(stmt)
    existing = result.scalar_one_or_none()

    if existing:
        await session.execute(
            update(VendorContext)
            .where(VendorContext.account_id == body.accountId)
            .values(**context)
        )
        action = "updated"
    else:
        new = VendorContext(id=str(uuid.uuid4()), **context)
        session.add(new)
        action = "created"

    log = VendorLog(
        id=str(uuid.uuid4()),
        account_id=body.accountId,
        action=action,
        created_at=datetime.datetime.utcnow()
    )
    session.add(log)

    # Token check
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(
                "https://api.moysklad.ru/api/remap/1.2/entity/product",
                headers={"Authorization": f"Bearer {token}"}
            )
        r.raise_for_status()
    except Exception:
        error_log = VendorLog(
            id=str(uuid.uuid4()),
            account_id=body.accountId,
            action="token_check_failed",
            created_at=datetime.datetime.utcnow()
        )
        session.add(error_log)

    await session.commit()
    return {"status": "ok", "action": action}

@router.get("/vendor/{account_id}")
async def get_vendor_context(account_id: str, session: AsyncSession = Depends(get_session)):
    stmt = select(VendorContext).where(VendorContext.account_id == account_id)
    result = await session.execute(stmt)
    data = result.scalar_one_or_none()
    if not data:
        raise HTTPException(status_code=404, detail="Account not found")
    return data
