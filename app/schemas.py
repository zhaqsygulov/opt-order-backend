
from pydantic import BaseModel, Field
from typing import List

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

class VendorRequest(BaseModel):
    appUid: str
    accountId: str
    accountName: str
    subscription: Subscription
    cause: str
    access: List[AccessItem]
    contextId: str
    employeeId: str
    orgId: str
