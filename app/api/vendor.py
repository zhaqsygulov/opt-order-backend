from fastapi import APIRouter, Header
from app.services.vendor_client import get_employee_context

router = APIRouter()

@router.post("/vendor/context/{context_id}")
async def get_context(context_id: str, authorization: str = Header(...)):
    return await get_employee_context(authorization, context_id)
