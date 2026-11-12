from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select

from database.dependencies import get_db
from database.user_model import UserModel
from security.token import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/token"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db=Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired authentication token",
        headers={"WWW-Authenticate": "Bearer"}
    )

    payload = verify_access_token(token)

    if payload is None:
        raise credentials_exception

    email = payload.get("sub")

    if not email:
        raise credentials_exception

    user = db.scalars(
        select(UserModel).where(UserModel.email == email)
    ).first()

    if user is None or not user.is_active:
        raise credentials_exception

    return user

def require_admin(
    current_user: UserModel = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    return current_user