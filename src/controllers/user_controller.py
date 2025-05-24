import logging

from src.schemas.user_schemas import UserPaginatedResponse
from src.exceptions.server_exceptions import InternalServerError
from src.exceptions.client_exceptions import NotFound
from src.exceptions import app_exceptions as ae
from src.services.user_service import UserService

logger = logging.getLogger(__name__)


class UserController():
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def get_paginated(self, page: int, limit: int) -> UserPaginatedResponse:
        try:
            return await self.user_service.get_paginated(page, limit)
        except ae.NotFoundError as ex:
            logger.error(f'Pagina {page} no existe. Items por pagina: {limit}')
            raise NotFound(ex.message, 'USER_PAGE_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al listar usuarios: {ex}')
            raise InternalServerError(
                message=f'Error al listar usuarios',
                exception_code='USER_UNHANDLED_ERROR'
            )
