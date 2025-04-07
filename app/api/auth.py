from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
import httpx
import os

router = APIRouter()

CLIENT_ID = os.getenv("MS_CLIENT_ID", "your-client-id")
CLIENT_SECRET = os.getenv("MS_CLIENT_SECRET", "your-client-secret")
REDIRECT_URI = os.getenv("MS_REDIRECT_URI", "https://yourdomain.com/callback")

@router.get("/authorize")
def authorize():
    return RedirectResponse(
        f"https://login.moysklad.ru/app/oauth/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    )

@router.get("/callback")
async def callback(request: Request):
    code = request.query_params.get("code")
    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.moysklad.ru/api/remap/1.2/security/token", data={
            "grant_type": "authorization_code",
            "code": code,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI
        })
        response.raise_for_status()
        token_data = response.json()
        # на этом этапе сохрани token_data["access_token"]
        return token_data
