from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from app.models.base import DBBase


class DBRole(DBBase):
    __tablename__ = "roles"

    name = Column(String, unique=True)
    priority = Column(Integer, unique=True)
    description = Column(String)
