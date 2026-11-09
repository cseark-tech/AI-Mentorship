from database.connection import SessionLocal
from auth.user_service import UserService
from security.token import create_access_token


db = SessionLocal()

try:
    service = UserService(db)

    user = service.authenticate_user(
        email="admin@gmail.com",
        password="Admin@123"
    )

    if user is None:
        print("Invalid email or password")
    else:
        token = create_access_token(
            user_email=user.email,
            role=user.role
        )

        print("Login successful!")
        print("Email:", user.email)
        print("Role:", user.role)
        print("JWT Token:", token)

finally:
    db.close()