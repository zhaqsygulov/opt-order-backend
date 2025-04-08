from app.models.activation import ActivationRequest, ActivationResponse

class VendorService:
    async def activate(self, app_id: str, account_id: str, request: ActivationRequest) -> ActivationResponse:
        print(f"Activated: {account_id} with token: {request.access[0].access_token}")
        return ActivationResponse(status="Activated")

    async def deactivate(self, app_id: str, account_id: str):
        print(f"Deactivated: {account_id}")
