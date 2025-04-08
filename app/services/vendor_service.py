from app.models.activation import ActivationRequest
from app.db.models import VendorContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import uuid4
from datetime import datetime

class VendorService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def activate(self, app_id: str, account_id: str, request: ActivationRequest):
        token = request.access[0].access_token

        result = await self.session.execute(
            select(VendorContext).where(VendorContext.account_id == str(account_id))
        )
        existing = result.scalars().first()

        if existing:
            existing.access_token = token
            existing.updated_at = datetime.utcnow()
            existing.context_id = request.contextId
            existing.employee_id = request.employeeId
            existing.org_id = request.orgId
        else:
            context = VendorContext(
                id=str(uuid4()),
                account_id=str(account_id),
                access_token=token,
                context_id=request.contextId,
                employee_id=request.employeeId,
                org_id=request.orgId,
                created_at=datetime.utcnow()
            )
            self.session.add(context)

        await self.session.commit()
        return {"status": "saved", "account_id": str(account_id)}
