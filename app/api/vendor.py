from fastapi import APIRouter

router = APIRouter(prefix="/vendor", tags=["vendor"])

@router.get("/status")
async def vendor_status():
    return {"status": "Vendor API is alive"}
