from sqlalchemy.orm import Session

from app.models.role import DBRole
from app.repositories.base import BaseRepository
from app.schemas.role import Role


class RoleRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, DBRole)

    def create_role(self, role: Role):
        role_dict = role.model_dump()

        return self.create(role_dict)

    def get_role(self, role_id):
        return self.get_by_id(role_id)
