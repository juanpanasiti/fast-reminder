import logging

from src.exceptions.server_exceptions import InternalServerError
from src.exceptions.client_exceptions import NotFound
from src.exceptions.base_http_exception import BaseHTTPException
from src.exceptions import app_exceptions as ae
from src.services.auth_service import AuthService
from src.schemas.auth_schemas import RegisterUser, LoginUser, TokenResponse

logger = logging.getLogger(__name__)


class AuthController():
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service

    async def register(self, new_user: RegisterUser) -> TokenResponse:
        try:
            return await self.auth_service.register(new_user)
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error no contemplado en {__name__}.register(): ' + str(ex))
            raise InternalServerError(str(ex))
            

    async def login(self, credentials: LoginUser) -> TokenResponse:
        try:
            return await self.auth_service.login(credentials)
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            logger.critical(f'Error no contemplado en {__name__}.login(): ' + str(ex))
            raise InternalServerError(str(ex))
