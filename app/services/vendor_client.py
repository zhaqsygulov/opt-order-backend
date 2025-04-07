
import httpx
from app.models.context import GetEmployeeContextResponse

BASE_URL = "https://apps-api.moysklad.ru/api/vendor/1.0"

async def get_employee_context(auth: str, context_id: str) -> GetEmployeeContextResponse:
    headers = {
        "Authorization": auth
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/context/{context_id}", headers=headers)
        response.raise_for_status()
        return GetEmployeeContextResponse(**response.json())
