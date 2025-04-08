from fastapi import FastAPI
from app.api import vendor
from app.db.models import Base
from app.db.session import engine

app = FastAPI(
    title="Opt Order Backend",
    version="0.7.0"
)

app.include_router(vendor.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
