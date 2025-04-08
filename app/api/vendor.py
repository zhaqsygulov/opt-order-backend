from fastapi import APIRouter, Header, HTTPException, Depends
from app.services.vendor_service import VendorService
from app.utils.jwt_handler import verify_jwt
from app.models.activation import ActivationRequest, ActivationResponse

router = APIRouter(prefix="/apps", tags=["vendor"])

@router.put("/{app_id}/{account_id}")
async def activate_app(
    app_id: str,
    account_id: str,
    request: ActivationRequest,
    authorization: str = Header(...),
    service: VendorService = Depends()
):
    token = authorization.split(" ")[1]
    if not verify_jwt(token):
        raise HTTPException(status_code=401, detail="Invalid JWT token")
    return await service.activate(app_id, account_id, request)

@router.delete("/{app_id}/{account_id}")
async def deactivate_app(
    app_id: str,
    account_id: str,
    authorization: str = Header(...),
    service: VendorService = Depends()
):
    token = authorization.split(" ")[1]
    if not verify_jwt(token):
        raise HTTPException(status_code=401, detail="Invalid JWT token")
    await service.deactivate(app_id, account_id)
    return {"detail": "Deactivated successfully"}
