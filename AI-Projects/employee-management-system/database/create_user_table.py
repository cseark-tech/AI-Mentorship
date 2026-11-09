from database.connection import engine, Base
from database.models import EmployeeModel
from database.user_model import UserModel

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")