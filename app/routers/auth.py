from fastapi import APIRouter
from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from sqlalchemy.orm import Session

from app.schemas.token import Token
from app.services.config import Settings
from app.services.database import get_db
from app.services.authentication import authenticate_user, create_access_token

router = APIRouter()


@router.post("/login")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
) -> Token:
    user = await authenticate_user(db, form_data.username, form_data.password)

    access_token = create_access_token(
        payload={"sub": user.username, "role": user.role}
    )

    return Token(access_token=access_token, token_type="bearer")
