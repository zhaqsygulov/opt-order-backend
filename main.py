from fastapi import FastAPI
from app.api import vendor

app = FastAPI(
    title="Opt Order Backend",
    version="0.1.0"
)

app.include_router(vendor.router)
