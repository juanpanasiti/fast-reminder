from src.schemas.payment_schemas import NewPaymentRequest, UpdatePaymentRequest, PaymentResponse, PaymentPaginatedResponse
from src.exceptions.server_exceptions import InternalServerError, NotImplemented
from src.exceptions.base_http_exception import BaseHTTPException


class PaymentController():
    def __init__(self, payment_service):
        self.payment_service = payment_service

    async def get_paginated(self, page: int, limit: int) -> PaymentPaginatedResponse:
        try:
            # return await self.payment_service.get_paginated(page, limit)
            raise NotImplemented('Endpoint get paginated not implemented', exception_code='PAYMENT_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al listar pagos',
                exception_code='PAYMENT_UNHANDLED_ERROR'
            )

    async def create(self, data: NewPaymentRequest) -> PaymentResponse:
        try:
            # return await self.payment_service.create(data)
            raise NotImplemented('Endpoint get paginated not implemented', exception_code='PAYMENT_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al crear el pago "{data.name}"',
                exception_code='PAYMENT_UNHANDLED_ERROR'
            )

    async def get_by_id(self, payment_id: int) -> PaymentResponse:
        try:
            # return await self.payment_service.get_by_id(payment_id)
            raise NotImplemented('Endpoint get paginated not implemented', exception_code='PAYMENT_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al obtener el pago #{payment_id}',
                exception_code='PAYMENT_UNHANDLED_ERROR'
            )

    async def update(self, payment_id: int, data: UpdatePaymentRequest) -> PaymentResponse:
        try:
            # return await self.payment_service.update(payment_id, data)
            raise NotImplemented('Endpoint get paginated not implemented', exception_code='PAYMENT_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al actualizar el pago #{payment_id}',
                exception_code='PAYMENT_UNHANDLED_ERROR'
            )

    async def delete(self, payment_id: int) -> None:
        try:
            # return await self.payment_service.delete(payment_id)
            raise NotImplemented('Endpoint get paginated not implemented', exception_code='PAYMENT_ENDPOINT_NOT_IMPLEMENTED')
        except BaseHTTPException as ex:
            raise ex
        except Exception as ex:
            raise InternalServerError(
                message=f'Error al eliminar el pago #{payment_id}',
                exception_code='PAYMENT_UNHANDLED_ERROR'
            )
