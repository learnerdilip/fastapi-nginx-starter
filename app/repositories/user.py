from sqlalchemy.orm import Session

from app.models.user import DBUser
from app.services.password_helpers import get_password_hash
from app.schemas.user import UserCreate
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, DBUser)

    def get_user_by_username(self, username: str):
        return self.db.query(DBUser).filter(DBUser.username == username).first()

    def create_user(self, user: UserCreate):
        user_dict = user.model_dump()
        hashed_password = get_password_hash(user_dict.pop("password"))
        user_dict["hashed_password"] = hashed_password

        return self.create(user_dict)
