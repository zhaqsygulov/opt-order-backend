
from fastapi import FastAPI
from app.api import vendor

app = FastAPI()
app.include_router(vendor.router)
