from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from database.dependencies import get_db
from auth.user_service import UserService
from security.token import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/token")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db=Depends(get_db)
):
    service = UserService(db)

    user = service.authenticate_user(
        form_data.username,
        form_data.password
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )

    token = create_access_token(
        user_email=user.email,
        role=user.role
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }