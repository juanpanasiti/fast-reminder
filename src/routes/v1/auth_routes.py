
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.schemas.auth_schemas import RegisterUser, TokenResponse
from .dependencies import auth_controller


router = APIRouter(
    prefix='/auth',
)


@router.post(
    '/register',
    status_code=201,
)
async def register_user(new_user: RegisterUser) -> TokenResponse:
    return await auth_controller.register(new_user)


@router.post(
    '/login',
)
async def login_user(credentials: OAuth2PasswordRequestForm = Depends()) -> TokenResponse:
    return await auth_controller.login(credentials)
