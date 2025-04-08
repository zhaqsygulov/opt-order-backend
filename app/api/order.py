from fastapi import APIRouter, HTTPException
from app.services.order_service import OrderService
from app.models.order import OrderRequest

router = APIRouter(prefix="/order", tags=["order"])
orders_store = {}

@router.post("")
async def create_order(request: OrderRequest):
    order_id, order_data = await OrderService().generate_order(request)
    orders_store[order_id] = order_data
    return {"order_id": order_id, "link": f"https://yourapp.kz/invoice/{order_id}"}

@router.get("/invoice/{order_id}")
async def get_invoice(order_id: str):
    order = orders_store.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
