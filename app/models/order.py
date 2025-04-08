from pydantic import BaseModel
from typing import List, Optional

class OrderItem(BaseModel):
    id: str
    name: str
    quantity: int
    price: float

class OrderClient(BaseModel):
    name: str
    phone: str
    city: str

class OrderRequest(BaseModel):
    client: OrderClient
    items: List[OrderItem]
    discount: Optional[float] = 0
    commission: Optional[float] = 0
    additional_costs: Optional[float] = 0
    payment_method: str
