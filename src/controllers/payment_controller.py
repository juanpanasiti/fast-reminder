import logging

from src.schemas.payment_schemas import NewPaymentRequest, UpdatePaymentRequest, PaymentResponse, PaymentPaginatedResponse
from src.exceptions.server_exceptions import InternalServerError
from src.exceptions.client_exceptions import NotFound
from src.exceptions import app_exceptions as ae
from src.services.payment_service import PaymentService

logger = logging.getLogger(__name__)


class PaymentController():
    def __init__(self, payment_service: PaymentService):
        self.payment_service = payment_service

    async def get_paginated(self, page: int, limit: int) -> PaymentPaginatedResponse:
        try:
            return await self.payment_service.get_paginated(page, limit)
        except ae.NotFoundError as ex:
            logger.error(f'Pagina {page} no existe. Items por pagina: {limit}')
            raise NotFound(ex.message, 'PAYMENT_PAGE_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al listar pagos: {ex}')
            raise InternalServerError(
                message=f'Error al listar pagos',
                exception_code='PAYMENT_UNHANDLED_ERROR'
            )

    async def create(self, data: NewPaymentRequest) -> PaymentResponse:
        try:
            return await self.payment_service.create(data)
        except Exception as ex:
            logger.critical(f'Error desconocido al crear el pago: {ex}')
            raise InternalServerError(
                message=f'Error al crear el pago de $"{data.amount}"',
                exception_code='PAYMENT_UNHANDLED_ERROR'
            )

    async def get_by_id(self, payment_id: int) -> PaymentResponse:
        try:
            return await self.payment_service.get_by_id(payment_id)
        except ae.NotFoundError as ex:
            logger.error(f'El pago #{payment_id} no encontrado')
            raise NotFound(ex.message, 'PAYMENT_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al obtener el pago #{payment_id}: {ex}')
            raise InternalServerError(
                message=f'Error al obtener el pago #{payment_id}',
                exception_code='PAYMENT_UNHANDLED_ERROR'
            )

    async def update(self, payment_id: int, data: UpdatePaymentRequest) -> PaymentResponse:
        try:
            return await self.payment_service.update(payment_id, data)
        except ae.NotFoundError as ex:
            logger.error(f'El pago #{payment_id} no encontrado')
            raise NotFound(ex.message, 'PAYMENT_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al actualizar el pago #{payment_id}: {ex}')
            raise InternalServerError(
                message=f'Error al actualizar el pago #{payment_id}',
                exception_code='PAYMENT_UNHANDLED_ERROR'
            )

    async def delete(self, payment_id: int) -> None:
        try:
            return await self.payment_service.delete(payment_id)
        except ae.NotFoundError as ex:
            logger.error(f'El pago #{payment_id} no encontrado')
            raise NotFound(ex.message, 'PAYMENT_NOT_FOUND')
        except Exception as ex:
            logger.critical(f'Error desconocido al eliminar el pago #{payment_id}: {ex}')
            raise InternalServerError(
                message=f'Error al eliminar el pago #{payment_id}',
                exception_code='PAYMENT_UNHANDLED_ERROR'
            )
