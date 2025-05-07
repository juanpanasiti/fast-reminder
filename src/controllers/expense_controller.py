from src.schemas.expense_schemas import NewExpenseRequest, UpdateExpenseRequest, ExpenseResponse, ExpensePaginatedResponse
from src.exceptions.server_exceptions import InternalServerError, NotImplemented
from src.exceptions.base_http_exception import BaseHTTPException


class ExpenseController():
    def __init__(self, expense_service):
        self.expense_service = expense_service

    async def get_paginated(self, page: int, limit: int) -> ExpensePaginatedResponse:
        try:
            # return await self.expense_service.get_paginated(page, limit)
            raise NotImplemented('Endpoint get paginated not implemented', exception_code='EXPENSE_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al listar gastos',
                exception_code='EXPENSE_UNHANDLED_ERROR'
            )

    async def create(self, data: NewExpenseRequest) -> ExpenseResponse:
        try:
            # return await self.expense_service.create(data)
            raise NotImplemented('Endpoint get paginated not implemented', exception_code='EXPENSE_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al crear el gasto "{data.name}"',
                exception_code='EXPENSE_UNHANDLED_ERROR'
            )

    async def get_by_id(self, expense_id: int) -> ExpenseResponse:
        try:
            # return await self.expense_service.get_by_id(expense_id)
            raise NotImplemented('Endpoint get paginated not implemented', exception_code='EXPENSE_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al obtener el gasto #{expense_id}',
                exception_code='EXPENSE_UNHANDLED_ERROR'
            )

    async def update(self, expense_id: int, data: UpdateExpenseRequest) -> ExpenseResponse:
        try:
            # return await self.expense_service.update(expense_id, data)
            raise NotImplemented('Endpoint get paginated not implemented', exception_code='EXPENSE_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al actualizar el gasto #{expense_id}',
                exception_code='EXPENSE_UNHANDLED_ERROR'
            )

    async def delete(self, expense_id: int) -> None:
        try:
            # return await self.expense_service.delete(expense_id)
            raise NotImplemented('Endpoint get paginated not implemented', exception_code='EXPENSE_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al eliminar el gasto #{expense_id}',
                exception_code='EXPENSE_UNHANDLED_ERROR'
            )
