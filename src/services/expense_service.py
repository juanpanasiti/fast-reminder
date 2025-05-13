import asyncio
import logging
from typing import List

from src.schemas.expense_schemas import NewExpenseRequest, UpdateExpenseRequest, ExpenseResponse, ExpensePaginatedResponse
from src.exceptions import app_exceptions as ae

logger = logging.getLogger(__name__)


class ExpenseService():
    def __init__(self, expense_repo):
        self.expense_repo = expense_repo

    async def get_paginated(self, page: int, limit: int) -> ExpensePaginatedResponse:
        logger.debug(f'Obteniendo gastos paginados. Pagina: {page}, Limite: {limit}')
        expenses, total_count = await asyncio.gather(
            self.__get_expense_list(page, limit),
            self.__count(),
        )
        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Pagina {page} no existe')
        logger.debug(f'Gastos obtenidos: {len(expenses)}')
        return ExpensePaginatedResponse(
            results=expenses,
            meta={
                'current_page': page,
                'total_pages': total_pages,
                'total_items': total_count,
                'items_per_page': limit,
                'has_next_page': page < total_pages,
                'has_previous_page': page > 1,
            }
        )

    async def create(self, data: NewExpenseRequest) -> ExpenseResponse:
        logger.debug(f'Creando gasto: {data}')
        from datetime import datetime  # TODO: remove
        new_expense = ExpenseResponse(
            id=1,
            name=data.name,
            description=data.description,
            periodicity_in_months=data.periodicity_in_months,
            last_payment_date=data.last_payment_date,
            next_payment_date=data.next_payment_date,
            estimated_next_payment_date=data.estimated_next_payment_date,
            payments=[],
            has_pending_payments=False,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        logger.debug(f'Gasto creado: {new_expense}')
        return new_expense

    async def get_by_id(self, expense_id: int) -> ExpenseResponse:
        logger.debug(f'Obteniendo gasto por ID: {expense_id}')
        raise ae.NotFoundError(f'El gasto #{expense_id} no existe')

    async def update(self, expense_id: int, data: UpdateExpenseRequest) -> ExpenseResponse:
        logger.debug(f'Actualizando gasto #{expense_id} con datos: {data}')
        raise ae.NotFoundError(f'El gasto #{expense_id} no existe')

    async def delete(self, expense_id: int) -> None:
        logger.debug(f'Eliminando gasto #{expense_id}')
        raise ae.NotFoundError(f'El gasto #{expense_id} no existe')

    async def __count(self) -> int:
        # TODO: llamar al repo y obtener el numero total de gastos
        return 0

    async def __get_expense_list(self, page: int, limit: int) -> List[ExpenseResponse]:
        # TODO: Llamar al repo y obtener el listado correspondiente
        return []
