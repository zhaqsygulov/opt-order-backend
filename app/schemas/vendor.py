from typing import List, Optional
from pydantic import BaseModel, UUID4

class AccessItem(BaseModel):
    resource: str
    scope: List[str]
    access_token: str

class Subscription(BaseModel):
    type: str
    tariffId: str
    tariffName: str
    expiryMoment: str
    trial: bool
    notForResale: bool
    partner: bool

class VendorActivationRequest(BaseModel):
    appUid: str
    accountId: UUID4
    accountName: str
    subscription: Subscription
    cause: str
    access: List[AccessItem]
    contextId: str
    employeeId: str
    orgId: str
