from typing import Optional

from pydantic import field_validator

from app.schemas import Base


class UserResponse(Base):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    role: Optional[str] = None

    @field_validator("username")
    def username_alphanumeric(cls, v):
        assert len(v) >= 3, "username must be at least 3 characters"
        return v


class UserCreate(UserResponse):
    password: str

    @field_validator("password")
    def password_length(cls, v):
        # for now we are using a simple password length validation
        assert len(v) >= 8, "password must be at least 8 characters"
        return v
