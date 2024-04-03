from typing import Optional
from sqlalchemy.orm import Session

from app.repositories.user import UserRepository
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(self.db)

    def get_user(self, user_id):
        return self.user_repository.get_by_id(user_id)

    def create_user(self, user: UserCreate):
        return self.user_repository.create_user(user)
