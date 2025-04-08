
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VendorContext(Base):
    __tablename__ = "vendor_context"
    id = Column(String, primary_key=True)
    account_id = Column(String)
    access_token = Column(String)
    context_id = Column(String)
    employee_id = Column(String)
    org_id = Column(String)

class VendorLog(Base):
    __tablename__ = "vendor_log"
    id = Column(String, primary_key=True)
    account_id = Column(String)
    action = Column(String)
    created_at = Column(DateTime)
