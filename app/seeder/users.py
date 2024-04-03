from cgi import test
from fastapi import Depends
from sqlalchemy.orm import Session


from app.schemas.user import UserCreate
from app.services.user import UserService

test_users = [
    {
        "username": "admin@ryberg.com",
        "email": "admin@ryberg.com",
        "password": "Robot2020",
        "full_name": "Ryberg Admin",
        "role": "admin",  # This is the role_id of the admin role
        "is_active": True,
    },
    {
        "username": "manager@ryberg.com",
        "email": "manager@ryberg.com",
        "password": "Robot2020",
        "full_name": "Ryberg manager",
        "role": "manager",
        "is_active": True,
    },
    {
        "username": "guest@ryberg.com",
        "email": "guest@ryberg.com",
        "password": "Robot2020",
        "full_name": "Ryberg guest",
        "role": "guest",
        "is_active": True,
    },
]

test_user_list = [UserCreate(**user) for user in test_users]


def seed_users(db: Session):
    for user in test_user_list:
        UserService(db).create_user(user)
    return "Users seeded"
