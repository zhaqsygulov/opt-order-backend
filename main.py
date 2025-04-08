from fastapi import FastAPI
from app.api import vendor, context, products, order

app = FastAPI(
    title="Opt Order Backend",
    version="0.5.0"
)

app.include_router(vendor.router)
app.include_router(context.router)
app.include_router(products.router)
app.include_router(order.router)
