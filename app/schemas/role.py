from typing import Optional
from pydantic import BaseModel


class Role(BaseModel):
    name: str
    priority: int
    description: Optional[str] = None


class RoleInDB(Role):
    id: int
