from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.schemas.vendor import VendorActivationRequest
from app.models.vendor import VendorContext
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
