
import jwt

from datetime import datetime, timedelta, timezone
from config.settings import settings

settings.ACCESS_TOKEN_EXPIRE_MINUTES
settings.JWT_SECRET
settings.JWT_ALGORITHM

if not settings.JWT_SECRET:
    raise RuntimeError("JWT_SECRET is not configured")

settings.JWT_ALGORITHM = "HS256"
settings.ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(
    user_email: str,
    role: str
) -> str:

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": user_email,
        "role": role,
        "exp": expire
    }

    token = jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM
    )

    return token


def verify_access_token(token: str):

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM]
        )

        return payload

    except jwt.InvalidTokenError:
        return None