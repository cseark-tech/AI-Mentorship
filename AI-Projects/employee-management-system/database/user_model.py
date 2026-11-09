from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

from database.connection import Base


class UserModel(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    role = Column(
        String(50),
        nullable=False,
        default="user"
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True
    )