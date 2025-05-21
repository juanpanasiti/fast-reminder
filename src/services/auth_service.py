import logging

from src.schemas.auth_schemas import RegisterUser, LoginUser, TokenResponse
from src.schemas.user_schemas import UserResponse
from src.exceptions.client_exceptions import BadRequest
from src.repositories.user_repository import UserRepository
from src.handlers.jwt_handler import jwt_handler

logger = logging.getLogger(__name__)


class AuthService():
    def __init__(self, user_repo: UserRepository = UserRepository()):
        self.user_repo = user_repo

    async def register(self, new_user: RegisterUser) -> TokenResponse:
        user_dict = await self.user_repo.create(new_user.model_dump())
        user = UserResponse(**user_dict)
        access_token = self.__get_token(user)
        return TokenResponse.model_validate({
            'user': user,
            'access_token': access_token,
        })

    async def login(self, credentials: LoginUser) -> TokenResponse:
        user = await self.user_repo.get_one_by_criteria({'username': credentials.username})
        if user is None:
            raise BadRequest('Error en username/password')
        is_pass_ok = await self.user_repo.check_password(user['id'], credentials.password)
        if not is_pass_ok:
            raise BadRequest('Error en username/password')
        user_response = UserResponse.model_validate(user)
        access_token = self.__get_token(user_response)
        return TokenResponse.model_validate({
            'user': user_response,
            'access_token': access_token,
        })

    def __get_token(self, user: UserResponse) -> str:
        payload = {
            'user_id': user.id
        }
        return jwt_handler.encode(payload)
