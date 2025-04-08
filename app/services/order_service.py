import uuid
from app.models.order import OrderRequest

class OrderService:
    async def generate_order(self, request: OrderRequest):
        order_id = str(uuid.uuid4())[:8]
        total = sum(item.quantity * item.price for item in request.items)
        discount_amount = total * (request.discount or 0) / 100
        commission_amount = total * (request.commission or 0) / 100
        total_with_all = total - discount_amount + commission_amount + (request.additional_costs or 0)
        return order_id, {
            "client": request.client,
            "items": request.items,
            "discount": request.discount,
            "commission": request.commission,
            "additional_costs": request.additional_costs,
            "payment_method": request.payment_method,
            "total": total,
            "total_final": total_with_all
        }
