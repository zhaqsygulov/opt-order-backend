
from fastapi import APIRouter, Header, HTTPException
from app.services.vendor_client import get_employee_context

router = APIRouter()

@router.get("/vendor/context/{context_id}")
async def get_context(
    context_id: str,
    authorization: str = Header(...),
):
    try:
        return await get_employee_context(authorization, context_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
