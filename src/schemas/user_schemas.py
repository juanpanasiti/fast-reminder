from datetime import datetime
from typing import List

from pydantic import BaseModel, EmailStr

from src.enums.role_enum import RoleEnum as Role
from .paginated_schemas import PaginationMeta


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: Role
    created_at: datetime
    updated_at: datetime

class UserPaginatedResponse(BaseModel):
    results: List[UserResponse]
    meta: PaginationMeta
