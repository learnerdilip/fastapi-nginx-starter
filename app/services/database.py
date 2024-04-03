from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.services.config import get_settings

settings = get_settings()

POSTGRES_DATABASE_URL = f"{settings.database_type}://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}:{settings.database_port}/{settings.postgres_db}"

engine = create_engine(POSTGRES_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
