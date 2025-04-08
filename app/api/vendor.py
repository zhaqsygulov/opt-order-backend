from fastapi import APIRouter, Header, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.models.activation import ActivationRequest
from app.services.vendor_service import VendorService

router = APIRouter(prefix="/vendor", tags=["vendor"])

@router.put("/apps/{app_id}/{account_id}")
async def activate_vendor_app(
    app_id: str,
    account_id: str,
    request: ActivationRequest,
    session: AsyncSession = Depends(get_session)
):
    return await VendorService(session).activate(app_id, account_id, request)
