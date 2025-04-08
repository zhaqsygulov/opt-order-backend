from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
<<<<<<< HEAD
from app.schemas.vendor import VendorActivationRequest
from app.models.vendor import VendorContext
from app.database import get_session
=======
from sqlalchemy.future import select

from app.database import get_session
from app.models import VendorContext
from app.schemas.vendor import VendorActivationRequest
import uuid

router = APIRouter()

@router.put("/vendor/apps/{app_id}/{account_id}")
<<<<<<< HEAD
async def activate_vendor_app(app_id: str, account_id: str, payload: VendorActivationRequest, session: AsyncSession = Depends(get_session)):
    # Dummy implementation
    return {"message": "App activated", "app_id": app_id, "account_id": account_id}
=======
async def activate_app(
    app_id: str,
    account_id: str,
    data: VendorActivationRequest,
    session: AsyncSession = Depends(get_session)
):
    # Валидация UUID
    try:
        uuid.UUID(account_id)
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid account ID format. Must be UUID.")

    # Получение access_token
    access_token = None
    for item in data.access:
        if item.resource.startswith("https://api.moysklad.ru"):
            access_token = item.access_token
            break

    if access_token is None:
        raise HTTPException(status_code=400, detail="Access token not found for MoySklad API")

    # Проверяем, существует ли уже запись
    result = await session.execute(
        select(VendorContext).where(VendorContext.account_id == account_id)
    )
    existing_context = result.scalar_one_or_none()

    if existing_context:
        # Обновляем
        existing_context.access_token = access_token
        existing_context.context_id = data.contextId
        existing_context.employee_id = data.employeeId
        existing_context.org_id = data.orgId
    else:
        # Создаем новую
        new_context = VendorContext(
            account_id=account_id,
            access_token=access_token,
            context_id=data.contextId,
            employee_id=data.employeeId,
            org_id=data.orgId
        )
        session.add(new_context)

    await session.commit()
    return {"status": "ok"}
