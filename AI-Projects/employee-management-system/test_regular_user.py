from database.connection import SessionLocal
from auth.user_service import UserService

db = SessionLocal()

try:
    service = UserService(db)

    user = service.register_user(
        email="employee@gmail.com",
        password="Employee@123"
    )

    print("Regular user created!")
    print("Email:", user.email)
    print("Role:", user.role)

finally:
    db.close()