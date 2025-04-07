
from app.models.context import VendorContext

async def get_employee_context(context_id: str, token: str):
    # Здесь будет обращение к VendorAPI
    return {
        "employee": {"meta": {"href": "employee_href"}},
        "organization": {"meta": {"href": "organization_href"}},
        "accountId": "account_id"
    }
