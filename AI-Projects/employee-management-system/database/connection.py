from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config.settings import settings


# DATABASE_URL = (
#     "postgresql+psycopg2://postgres:arunsql26@localhost:5432/"
#     "employee_management"
# )


engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()