from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.schemas.user import UserResponse, UserCreate
from app.services.authentication import get_current_user
from app.services.database import get_db
from app.services.user import UserService

router = APIRouter()


@router.get("/self", response_model=UserResponse)
async def read_users_me(current_user: UserResponse = Depends(get_current_user)):
    return current_user


@router.post("/create", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserService(db).create_user(user)

    return UserResponse.model_validate(db_user)
