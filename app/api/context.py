from fastapi import APIRouter

router = APIRouter(prefix="/context", tags=["context"])

@router.get("/status")
async def context_status():
    return {"status": "Context API is alive"}
