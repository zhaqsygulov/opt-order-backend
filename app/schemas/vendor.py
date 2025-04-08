from pydantic import BaseModel, UUID4
from typing import List, Optional
from datetime import datetime

class AccessData(BaseModel):
    resource: str
    scope: List[str]
    access_token: str

class SubscriptionData(BaseModel):
    type: str
    tariffId: str
    tariffName: str
    expiryMoment: datetime
    trial: bool
    notForResale: bool
    partner: bool

class VendorActivationRequest(BaseModel):
    appUid: str
    accountId: UUID4
    accountName: str
    cause: str
    access: List[AccessData]
    subscription: SubscriptionData
    contextId: Optional[str]
    employeeId: Optional[str]
    orgId: Optional[str]
