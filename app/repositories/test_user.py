from app.schemas.user import UserCreate
from app.conftest import admin_test_user
from app.services.user import UserService


def test_create_user(db_test_session):
    created_user = UserService(db_test_session).create_user(
        UserCreate(**admin_test_user)
    )

    assert created_user is not None, "User could not be created"

    assert created_user.username == admin_test_user["username"]
    assert created_user.email == admin_test_user["email"]
    assert created_user.full_name == admin_test_user["full_name"]
    assert created_user.role == admin_test_user["role"]
    assert created_user.is_active is admin_test_user["is_active"]
