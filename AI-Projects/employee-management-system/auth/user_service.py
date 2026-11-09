from sqlalchemy import select
from database.user_model import UserModel
from security.password import hash_password, verify_password


class UserService:

    def __init__(self, db):
        self.db = db

    def register_user(self, email, password, role="user"):

        existing_user = self.db.scalars(
            select(UserModel).where(
                UserModel.email == email
            )
        ).first()

        if existing_user:
            raise ValueError("Email already registered")

        user = UserModel(
            email=email,
            password_hash=hash_password(password),
            role=role
        )

        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception:
            self.db.rollback()
            raise

    def authenticate_user(self, email, password):

        user = self.db.scalars(
            select(UserModel).where(
                UserModel.email == email
            )
        ).first()

        if user is None:
            return None

        if not user.is_active:
            return None

        if not verify_password(password, user.password_hash):
            return None

        return user