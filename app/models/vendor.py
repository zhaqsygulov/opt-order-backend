from sqlalchemy import Column, String
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
