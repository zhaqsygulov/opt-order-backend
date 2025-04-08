from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base

class VendorContext(Base):
    __tablename__ = "vendor_context"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    account_id = Column(String, nullable=False)
    access_token = Column(String, nullable=False)
    context_id = Column(String, nullable=True)
    employee_id = Column(String, nullable=True)
    org_id = Column(String, nullable=True)
