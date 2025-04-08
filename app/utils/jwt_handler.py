import jwt
from app.config import SECRET_KEY, APP_UID

def verify_jwt(token: str) -> bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload.get("sub") == APP_UID
    except jwt.PyJWTError:
        return False
