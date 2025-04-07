from pydantic import BaseModel
from app.models.vendor_context import VendorContext 

class GetEmployeeContextResponse(BaseModel):
    employeeId: str
    employeeName: str
    employeeEmail: str | None = None
