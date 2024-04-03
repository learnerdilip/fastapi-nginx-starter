from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from app.models.base import DBBase


class DBUser(DBBase):
    __tablename__ = "users"

    username = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String, ForeignKey("roles.name"))  # default role should be guest role
