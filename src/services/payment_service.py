import asyncio
from typing import List

from src.schemas.payment_schemas import NewPaymentRequest, UpdatePaymentRequest, PaymentResponse, PaymentPaginatedResponse
from src.exceptions import app_exceptions as ae


class PaymentService():
    def __init__(self, payment_repo):
        self.payment_repo = payment_repo

    async def get_paginated(self, page: int, limit: int) -> PaymentPaginatedResponse:
        expenses, total_count = await asyncio.gather(
            self.__get_expense_list(page, limit),
            self.__count(),
        )
        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Pagina {page} no existe')

        return PaymentPaginatedResponse(
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

    async def create(self, data: NewPaymentRequest) -> PaymentResponse:
        from datetime import datetime  # TODO: remove
        return PaymentResponse(
            id=1,
            expense_id=data.expense_id,
            amount=data.amount,
            due_date=data.due_date,
            paid_date=data.paid_date,
            status='pending',
            notes=data.notes,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

    async def get_by_id(self, expense_id: int) -> PaymentResponse:
        raise ae.NotFoundError(f'El pago #{expense_id} no existe')

    async def update(self, expense_id: int, data: UpdatePaymentRequest) -> PaymentResponse:
        raise ae.NotFoundError(f'El pago #{expense_id} no existe')

    async def delete(self, expense_id: int) -> None:
        raise ae.NotFoundError(f'El pago #{expense_id} no existe')

    async def __count(self) -> int:
        # TODO: llamar al repo y obtener el numero total de pagos
        return 0

    async def __get_expense_list(self, page: int, limit: int) -> List[PaymentResponse]:
        # TODO: Llamar al repo y obtener el listado correspondiente
        return []
