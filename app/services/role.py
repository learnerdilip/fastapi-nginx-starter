from typing import Optional
from sqlalchemy.orm import Session

from app.repositories.role import RoleRepository
from app.schemas.role import Role


class RoleService:
    def __init__(self, db: Session):
        self.db = db
        self.role_repository = RoleRepository(self.db)

    def get_role(self, role_id):
        return self.role_repository.get_role(role_id)

    def create_role(self, role):
        return self.role_repository.create_role(role)

    # role is greater if its priority is less
    def is_role_one_greater(self, role_id_1, role_id_2):
        role_1: Optional[Role] = self.get_role(role_id_1)
        role_2: Optional[Role] = self.get_role(role_id_2)
        if role_1 is None or role_2 is None:
            return False

        return role_1.priority <= role_2.priority
