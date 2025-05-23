import logging

from src.schemas.expense_schemas import NewExpenseRequest, UpdateExpenseRequest, ExpenseResponse, ExpensePaginatedResponse
from src.exceptions.server_exceptions import InternalServerError
from src.exceptions.client_exceptions import NotFound
from src.exceptions import app_exceptions as ae
from src.services.expense_service import ExpenseService

logger = logging.getLogger(__name__)


class ExpenseController():
    def __init__(self, expense_service: ExpenseService):
        self.expense_service = expense_service

    async def get_paginated(self, user_id: int, page: int, limit: int) -> ExpensePaginatedResponse:
        try:
            return await self.expense_service.get_paginated(user_id, page, limit)
        except ae.NotFoundError as ex:
            logger.error(f'Pagina {page} no existe. Items por pagina: {limit}')
            raise NotFound(ex.message, 'EXPENSE_PAGE_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al listar gastos: {ex}')
            raise InternalServerError(
                message=f'Error al listar gastos',
                exception_code='EXPENSE_UNHANDLED_ERROR'
            )

    async def create(self, user_id: int, data: NewExpenseRequest) -> ExpenseResponse:
        try:
            return await self.expense_service.create(user_id, data)
        except Exception as ex:
            logger.critical(f'Error desconocido al crear el gasto: {ex}')
            raise InternalServerError(
                message=f'Error al crear el gasto "{data.name}"',
                exception_code='EXPENSE_UNHANDLED_ERROR'
            )

    async def get_by_id(self, user_id: int, expense_id: int) -> ExpenseResponse:
        try:
            return await self.expense_service.get_by_id(user_id, expense_id)
        except ae.NotFoundError as ex:
            logger.error(f'El gasto #{expense_id} no encontrado')
            raise NotFound(ex.message, 'EXPENSE_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al obtener el gasto #{expense_id}: {ex}')
            raise InternalServerError(
                message=f'Error al obtener el gasto #{expense_id}',
                exception_code='EXPENSE_UNHANDLED_ERROR'
            )

    async def update(self, user_id: int, expense_id: int, data: UpdateExpenseRequest) -> ExpenseResponse:
        try:
            return await self.expense_service.update(user_id, expense_id, data)
        except ae.NotFoundError as ex:
            logger.error(f'El gasto #{expense_id} no encontrado')
            raise NotFound(ex.message, 'EXPENSE_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al actualizar el gasto #{expense_id}: {ex}')
            raise InternalServerError(
                message=f'Error al actualizar el gasto #{expense_id}',
                exception_code='EXPENSE_UNHANDLED_ERROR'
            )

    async def delete(self, user_id: int, expense_id: int) -> None:
        try:
            return await self.expense_service.delete(user_id, expense_id)
        except ae.NotFoundError as ex:
            logger.error(f'El gasto #{expense_id} no encontrado')
            raise NotFound(ex.message, 'EXPENSE_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al eliminar el gasto #{expense_id}: {ex}')
            raise InternalServerError(
                message=f'Error al eliminar el gasto #{expense_id}',
                exception_code='EXPENSE_UNHANDLED_ERROR'
            )
