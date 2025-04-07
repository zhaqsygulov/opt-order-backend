
from fastapi import FastAPI
from app.api import vendor
from app.api import context
from app.database import Base, engine

app = FastAPI()

app.include_router(vendor.router)
app.include_router(context.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
