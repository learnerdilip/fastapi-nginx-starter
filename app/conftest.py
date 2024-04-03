import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import Generator

from app.main import app
from app.services.database import get_db
from app.models import Base

from app.schemas.user import UserCreate
from app.services.user import UserService

admin_test_user = {
    "username": "test_user@ryberg.com",
    "email": "test_user@ryberg.com",
    "password": "password",
    "full_name": "test user",
    "role": "admin",
    "is_active": True,
}


@pytest.fixture(scope="session")
def db_test_engine():
    # Create a test database in memory
    test_engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=test_engine)
    return test_engine


@pytest.fixture
def db_test_session(db_test_engine):
    # Create a new session for each test
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_test_engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def client(db_test_session):
    # Override the get_db dependency to return the test session
    app.dependency_overrides[get_db] = lambda: db_test_session

    return TestClient(app)


@pytest.fixture
def authenticated_test_client(db_test_session):
    app.dependency_overrides[get_db] = lambda: db_test_session

    # Create a test admin user
    UserService(db_test_session).create_user(UserCreate(**admin_test_user))

    auth_client = TestClient(app)
    login_data = {
        "username": admin_test_user.get("username", ""),
        "password": admin_test_user.get("password", ""),
    }
    response = auth_client.post("/auth/login", data=login_data)
    assert response.status_code == 200, response.text

    token = response.json().get("access_token")
    auth_client.headers = {
        **auth_client.headers,
        "Authorization": f"Bearer {token}",
    }

    return auth_client
