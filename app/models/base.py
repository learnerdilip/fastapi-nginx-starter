from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DBBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"
