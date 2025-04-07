from sqlalchemy import Column, String
from app.services.database import Base

class VendorContext(Base):
    __tablename__ = "vendor_context"

    context_id = Column(String, primary_key=True, index=True)
    employee_id = Column(String)
    organization_id = Column(String)
    account_id = Column(String)
