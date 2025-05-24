from datetime import datetime

from pydantic import BaseModel, EmailStr

from .user_schemas import UserResponse
from src.enums.role_enum import RoleEnum as Role


class RegisterUser(BaseModel):
    username: str
    password: str
    email: EmailStr


class LoginUser(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'
    user: UserResponse


class DecodedJwt(BaseModel):
    user_id: int
    role: Role
    exp: datetime
