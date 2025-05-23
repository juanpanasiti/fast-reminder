import asyncio
import logging
from typing import List

from src.schemas.expense_schemas import NewExpenseRequest, UpdateExpenseRequest, ExpenseResponse, ExpensePaginatedResponse
from src.exceptions import app_exceptions as ae
from src.repositories.expense_repository import ExpenseRepository

logger = logging.getLogger(__name__)


class ExpenseService():
    def __init__(self, expense_repo: ExpenseRepository = ExpenseRepository()):
        self.expense_repo = expense_repo

    async def get_paginated(self, user_id: int, page: int, limit: int) -> ExpensePaginatedResponse:
        logger.debug(f'Obteniendo gastos paginados. Pagina: {page}, Limite: {limit}')
        criteria = {'user_id': user_id}
        expenses, total_count = await asyncio.gather(
            self.__get_expense_list(page, limit, criteria),
            self.__count(criteria),
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

    async def create(self, user_id: int, data: NewExpenseRequest) -> ExpenseResponse:
        logger.debug(f'Creando gasto: {data}')
        data_dict = data.model_dump(mode='json')
        data_dict.update(user_id=user_id)
        new_expense = await self.expense_repo.create(data_dict)
        logger.debug(f'Gasto creado: {new_expense}')
        return ExpenseResponse.model_validate(new_expense)

    async def get_by_id(self, user_id: int, expense_id: int) -> ExpenseResponse:
        logger.debug(f'Obteniendo gasto por ID: {expense_id}')
        expense = await self.expense_repo.get_one_by_criteria({'id': expense_id, 'user_id': user_id})
        if expense is None:
            raise ae.NotFoundError(f'El gasto #{expense_id} no existe')
        return ExpenseResponse.model_validate(expense)

    async def update(self, user_id: int, expense_id: int, data: UpdateExpenseRequest) -> ExpenseResponse:
        logger.debug(f'Actualizando gasto #{expense_id} con datos: {data}')
        expense = await self.expense_repo.update_one(
            {'id': expense_id, 'user_id': user_id},
            data.model_dump(mode='json', exclude_unset=True)
        )
        if expense is None:
            raise ae.NotFoundError(f'El gasto #{expense_id} no existe')
        return ExpenseResponse.model_validate(expense)

    async def delete(self, user_id: int, expense_id: int) -> None:
        logger.debug(f'Eliminando gasto #{expense_id}')
        deleted = await self.expense_repo.delete_one({'id': expense_id, 'user_id': user_id})
        if not deleted:
            raise ae.NotFoundError(f'El gasto #{expense_id} no existe')
        return None

    async def __count(self, criteria: dict) -> int:
        return await self.expense_repo.count(criteria)

    async def __get_expense_list(self, page: int, limit: int, criteria: dict) -> List[ExpenseResponse]:
        return await self.expense_repo.get_many(page, limit, criteria)
