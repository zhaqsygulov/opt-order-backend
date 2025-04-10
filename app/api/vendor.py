from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.schemas.vendor import VendorActivationRequest
from app.models.vendor import VendorContext
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from sqlalchemy.future import select

import uuid

router = APIRouter()

@router.put("/vendor/apps/{app_id}/{account_id}")
async def activate_vendor_app(app_id: str, account_id: str, payload: VendorActivationRequest, session: AsyncSession = Depends(get_session)):
    context = VendorContext(
        id=str(uuid.uuid4()),
        account_id=str(payload.accountId),
        access_token=payload.access[0].access_token,
        context_id=payload.contextId,
        employee_id=payload.employeeId,
        org_id=payload.orgId
    )
    session.add(context)
    await session.commit()
    return {"status": "ok", "id": context.id}

# Альтернативный путь, для совместимости с МоемСкладом
@router.put("/api/moysklad/vendor/1.0/apps/{app_id}/{account_id}")
async def activate_from_moysklad(
    app_id: str,
    account_id: str,
    payload: VendorActivationRequest,
    session: AsyncSession = Depends(get_session),
):
    # Используем ту же логику
    context = VendorContext(
        id=str(uuid.uuid4()),
        account_id=str(payload.accountId),
        access_token=payload.access[0].access_token,
        context_id=payload.contextId,
        employee_id=payload.employeeId,
        org_id=payload.orgId
    )
    session.add(context)
    await session.commit()
    return {"status": "ok", "id": context.id}

@router.get("/api/moysklad/vendor/1.0/apps/{app_id}/{account_id}")
async def get_vendor_context(app_id: str, account_id: str, session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(VendorContext).where(VendorContext.account_id == account_id)
    )
    context = result.scalar_one_or_none()

    if not context:
        raise HTTPException(status_code=404, detail="Not Found")

    return {
        "status": "ok",
        "accountId": context.account_id,
        "contextId": context.context_id,
        "employeeId": context.employee_id,
        "orgId": context.org_id,
    }
