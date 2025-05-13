import asyncio
import logging
from typing import List

from src.schemas.payment_schemas import NewPaymentRequest, UpdatePaymentRequest, PaymentResponse, PaymentPaginatedResponse
from src.exceptions import app_exceptions as ae

logger = logging.getLogger(__name__)


class PaymentService():
    def __init__(self, payment_repo):
        self.payment_repo = payment_repo

    async def get_paginated(self, page: int, limit: int) -> PaymentPaginatedResponse:
        logger.debug(f'Obteniendo pagos paginados. Pagina: {page}, Limite: {limit}')
        expenses, total_count = await asyncio.gather(
            self.__get_expense_list(page, limit),
            self.__count(),
        )
        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Pagina {page} no existe')
        logger.debug(f'Pagos obtenidos: {len(expenses)}')
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
        logger.debug(f'Creando pago: {data}')
        from datetime import datetime  # TODO: remove
        new_payment = PaymentResponse(
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
        logger.debug(f'Pago creado: {new_payment}')
        return new_payment

    async def get_by_id(self, expense_id: int) -> PaymentResponse:
        logger.debug(f'Obteniendo pago por ID: {expense_id}')
        raise ae.NotFoundError(f'El pago #{expense_id} no existe')

    async def update(self, expense_id: int, data: UpdatePaymentRequest) -> PaymentResponse:
        logger.debug(f'Actualizando pago: {data}')
        raise ae.NotFoundError(f'El pago #{expense_id} no existe')

    async def delete(self, expense_id: int) -> None:
        logger.debug(f'Eliminando pago: {expense_id}')
        raise ae.NotFoundError(f'El pago #{expense_id} no existe')

    async def __count(self) -> int:
        # TODO: llamar al repo y obtener el numero total de pagos
        return 0

    async def __get_expense_list(self, page: int, limit: int) -> List[PaymentResponse]:
        # TODO: Llamar al repo y obtener el listado correspondiente
        return []
