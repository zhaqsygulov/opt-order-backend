from pydantic import BaseModel

class GetEmployeeContextResponse(BaseModel):
    employeeId: str
    employeeName: str
    employeeEmail: str | None = None
