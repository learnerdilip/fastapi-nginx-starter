from cgi import test
from fastapi import Depends
from sqlalchemy.orm import Session

from app.services.role import RoleService
from app.schemas.role import Role

test_roles = [
    {"name": "admin", "priority": 10, "description": "Admins can perform any action"},
    {
        "name": "manager",
        "priority": 20,
        "description": "Managers can perform most actions, except for admin actions",
    },
    {"name": "guest", "priority": 30, "description": "Least privileged role"},
]

test_role_list = [Role(**role) for role in test_roles]


def seed_roles(db: Session):
    for role in test_role_list:
        RoleService(db).create_role(role)
    return "Users seeded"
