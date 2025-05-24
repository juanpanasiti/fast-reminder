import asyncio
import logging
from typing import List

from src.schemas.user_schemas import UserResponse, UserPaginatedResponse
from src.exceptions import app_exceptions as ae
from src.repositories.user_repository import UserRepository

logger = logging.getLogger(__name__)


class UserService():
    def __init__(self, user_repo: UserRepository = UserRepository()):
        self.user_repo = user_repo

    async def get_paginated(self, page: int, limit: int) -> UserPaginatedResponse:
        logger.debug(f'Obteniendo usuarios paginados. Pagina: {page}, Limite: {limit}')
        users, total_count = await asyncio.gather(
            self.__get_user_list(page, limit),
            self.__count(),
        )
        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Pagina {page} no existe')
        logger.debug(f'Usuarios obtenidos: {len(users)}')
        return UserPaginatedResponse(
            results=users,
            meta={
                'current_page': page,
                'total_pages': total_pages,
                'total_items': total_count,
                'items_per_page': limit,
                'has_next_page': page < total_pages,
                'has_previous_page': page > 1,
            }
        )

   
    async def __count(self) -> int:
        return await self.user_repo.count()

    async def __get_user_list(self, page: int, limit: int) -> List[UserResponse]:
        return await self.user_repo.get_many(page, limit)
