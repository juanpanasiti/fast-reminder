import asyncio
from typing import List

from src.schemas.expense_schemas import NewExpenseRequest, UpdateExpenseRequest, ExpenseResponse, ExpensePaginatedResponse
from src.exceptions import app_exceptions as ae


class ExpenseService():
    def __init__(self, expense_repo):
        self.expense_repo = expense_repo

    async def get_paginated(self, page: int, limit: int) -> ExpensePaginatedResponse:
        expenses, total_count = await asyncio.gather(
            self.__get_expense_list(page, limit),
            self.__count(),
        )
        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Pagina {page} no existe')

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
        from datetime import datetime  # TODO: remove
        return ExpenseResponse(
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

    async def get_by_id(self, expense_id: int) -> ExpenseResponse:
        raise ae.NotFoundError(f'El gasto #{expense_id} no existe')

    async def update(self, expense_id: int, data: UpdateExpenseRequest) -> ExpenseResponse:
        raise ae.NotFoundError(f'El gasto #{expense_id} no existe')

    async def delete(self, expense_id: int) -> None:
        raise ae.NotFoundError(f'El gasto #{expense_id} no existe')

    async def __count(self) -> int:
        # TODO: llamar al repo y obtener el numero total de gastos
        return 0

    async def __get_expense_list(self, page: int, limit: int) -> List[ExpenseResponse]:
        # TODO: Llamar al repo y obtener el listado correspondiente
        return []
