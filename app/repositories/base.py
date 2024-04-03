from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.services.logger_config import logger


class BaseRepository:
    def __init__(self, db: Session, model):
        self.db = db
        self.model = model

    @staticmethod
    def handle_integrity_error(error: IntegrityError, db: Session):
        db.rollback()
        error_message = str(error.orig)
        logger.error(f"IntegrityError occurred: {error_message}")
        return None

    def get_by_id(self, id: int):
        try:
            return self.db.query(self.model).get(id)
        except IntegrityError as e:
            self.handle_integrity_error(e, self.db)

    def get_all(self, skip: int = 0, limit: int = 20):
        try:
            return self.db.query(self.model).offset(skip).limit(limit).all()
        except IntegrityError as e:
            self.handle_integrity_error(e, self.db)

    def create(self, obj_data: dict):
        try:
            obj = self.model(**obj_data)
            self.db.add(obj)
            self.db.commit()
            self.db.refresh(obj)
            return obj
        except IntegrityError as e:
            self.handle_integrity_error(e, self.db)

    def update(self, id: int, obj_data: dict):
        try:
            obj = self.db.query(self.model).get(id)
            if obj:
                for key, value in obj_data.items():
                    setattr(obj, key, value)
                self.db.commit()
                self.db.refresh(obj)
            return obj
        except IntegrityError as e:
            self.handle_integrity_error(e, self.db)

    def delete(self, id: int):
        try:
            obj = self.db.query(self.model).get(id)
            if obj:
                self.db.delete(obj)
                self.db.commit()
            return obj
        except IntegrityError as e:
            self.handle_integrity_error(e, self.db)
