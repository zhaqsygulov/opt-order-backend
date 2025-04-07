from fastapi import FastAPI
from app.api import vendor
from app.database import Base, engine
from app.models.vendor_context import VendorContext
import app.api.context as context

app = FastAPI()

app.include_router(vendor.router)
app.include_router(context.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
