from fastapi import APIRouter, Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import SessionLocal
from app.models.context import VendorContext
from app.services.vendor_client import get_employee_context

router = APIRouter(prefix="/vendor", tags=["Vendor"])

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/context/{context_id}")
async def get_and_store_context(
    context_id: str,
    authorization: str = Header(...),
    db: AsyncSession = Depends(get_db)
):
    # Получаем контекст из МоегоСклада
    context_data = await get_employee_context(context_id, authorization)

    # Запись в базу
    context = VendorContext(
        context_id=context_id,
        employee_id=context_data["employee"]["meta"]["href"],
        organization_id=context_data["organization"]["meta"]["href"],
        account_id=context_data["accountId"]
    )
    db.add(context)
    await db.commit()

    return {"message": "Контекст сохранен", "context": context_data}
