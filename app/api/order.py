from fastapi import APIRouter

router = APIRouter(prefix="/order", tags=["order"])

@router.get("/status")
async def order_status():
    return {"status": "Order API is alive"}
