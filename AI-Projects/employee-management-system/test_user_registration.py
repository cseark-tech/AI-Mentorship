from database.connection import SessionLocal
from auth.user_service import UserService

db = SessionLocal()

try:
    service = UserService(db)

    user = service.register_user(
        email="admin@gmail.com",
        password="Admin@123",
        role="admin"
    )

    print("User registered successfully!")
    print("User ID:", user.id)
    print("Email:", user.email)
    print("Role:", user.role)
    print("Password Hash:", user.password_hash)

except ValueError as error:
    print(error)

finally:
    db.close()