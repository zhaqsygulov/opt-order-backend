from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID

class ActivationAccess(BaseModel):
    resource: str
    scope: List[str]
    access_token: str

class Subscription(BaseModel):
    tariffId: Optional[str]
    trial: Optional[bool]
    tariffName: Optional[str]
    expiryMoment: Optional[datetime]
    notForResale: Optional[bool]
    partner: Optional[bool]

class ActivationRequest(BaseModel):
    appUid: str
    accountId: UUID
    accountName: Optional[str]
    cause: str
    access: List[ActivationAccess]
    subscription: Optional[Subscription]

class ActivationResponse(BaseModel):
    status: str
