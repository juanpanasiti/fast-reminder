import asyncio
import logging
from typing import List

from src.schemas.payment_schemas import NewPaymentRequest, UpdatePaymentRequest, PaymentResponse, PaymentPaginatedResponse
from src.exceptions import app_exceptions as ae
from src.repositories.payment_repository import PaymentRepository

logger = logging.getLogger(__name__)


class PaymentService():
    def __init__(self, payment_repo: PaymentRepository = PaymentRepository()):
        self.payment_repo = payment_repo

    async def get_paginated(self, page: int, limit: int) -> PaymentPaginatedResponse:
        logger.debug(f'Obteniendo pagos paginados. Pagina: {page}, Limite: {limit}')
        payments, total_count = await asyncio.gather(
            self.__get_payment_list(page, limit),
            self.__count(),
        )
        total_pages = (total_count // limit) + (0 if total_count % limit == 0 else 1)
        total_pages = 1 if (page == 1 and total_count == 0) else total_pages

        if page > total_pages:
            raise ae.NotFoundError(f'Pagina {page} no existe')
        logger.debug(f'Pagos obtenidos: {len(payments)}')
        return PaymentPaginatedResponse(
            results=payments,
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
        new_payment = await self.payment_repo.create(data.model_dump(mode='json'))
        logger.debug(f'Pago creado: {new_payment}')
        return new_payment

    async def get_by_id(self, payment_id: int) -> PaymentResponse:
        logger.debug(f'Obteniendo pago por ID: {payment_id}')
        payment = await self.payment_repo.get_one_by_criteria({'id': payment_id})
        if payment is None:
            raise ae.NotFoundError(f'El pago #{payment_id} no existe')
        return PaymentResponse.model_validate(payment)

    async def update(self, payment_id: int, data: UpdatePaymentRequest) -> PaymentResponse:
        logger.debug(f'Actualizando pago: {data}')
        payment = await self.payment_repo.update_one({'id': payment_id}, data.model_dump(mode='json', exclude_unset=True))
        if payment is None:
            raise ae.NotFoundError(f'El pago #{payment_id} no existe')

    async def delete(self, payment_id: int) -> None:
        logger.debug(f'Eliminando pago: {payment_id}')
        deleted = await self.payment_repo.delete_one({'id': payment_id})
        if not deleted:
            raise ae.NotFoundError(f'El pago #{payment_id} no existe')

    async def __count(self) -> int:
        return await self.payment_repo.count()

    async def __get_payment_list(self, page: int, limit: int) -> List[PaymentResponse]:
        return await self.payment_repo.get_many(page, limit)
