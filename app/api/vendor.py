from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.vendor import VendorActivationRequest
from app.models.vendor import VendorContext
from app.database import get_session

router = APIRouter()

@router.put("/vendor/apps/{app_id}/{account_id}")
async def activate_vendor_app(app_id: str, account_id: str, payload: VendorActivationRequest, session: AsyncSession = Depends(get_session)):
    # Dummy implementation
    return {"message": "App activated", "app_id": app_id, "account_id": account_id}
