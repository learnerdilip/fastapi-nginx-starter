from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.repositories.user import UserRepository
from app.schemas.user import UserResponse
from app.services.password_helpers import verify_password
from app.services.database import get_db

from app.services.config import get_settings

settings = get_settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_access_token(payload: dict) -> str:
    payload_to_encode = payload.copy()

    token_expiration = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    payload_to_encode.update({"exp": token_expiration})
    encoded_jwt = jwt.encode(
        payload_to_encode, settings.jwt_secret_key, algorithm=settings.hashing_algorithm
    )

    return encoded_jwt


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> UserResponse:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid user",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token_payload = jwt.decode(
            token=token,
            key=settings.jwt_secret_key,
            algorithms=settings.hashing_algorithm,
        )

        username = token_payload.get("sub")
        current_user_role = token_payload.get(
            "role"
        )  # @TODO use this role to check if user has access to a route

        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    db_user = UserRepository(db).get_user_by_username(username)
    if db_user is None or db_user.is_active is False:
        raise credentials_exception

    return UserResponse.model_validate(db_user)


async def authenticate_user(db, username: str, password: str) -> UserResponse:
    db_user = UserRepository(db).get_user_by_username(username)

    if not db_user or not verify_password(password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username password combination is incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return UserResponse.model_validate(db_user)
