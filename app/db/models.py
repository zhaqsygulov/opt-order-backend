from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class VendorContext(Base):
    __tablename__ = "vendor_context"

    id = Column(String, primary_key=True, index=True)
    account_id = Column(String, index=True)
    access_token = Column(String)
    context_id = Column(String, nullable=True)
    employee_id = Column(String, nullable=True)
    org_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
