from typing import Annotated

from fastapi import APIRouter, Path, Query

from src.schemas.payment_schemas import NewPaymentRequest, UpdatePaymentRequest, PaymentResponse, PaymentPaginatedResponse
from .dependencies import payment_controller
router = APIRouter(
    prefix='/payments',
    responses={
        400: {'description': 'Bad Request. Revisa la info del body y/o parámetros'},
        401: {'description': 'Unauthorized. Credenciales inválidas o no enviadas'},
        403: {'description': 'Forbidden. No tienes acceso a este recurso'},
        500: {'description': 'Internal Server Error. Error del servidor no manejado, contacta al sysadmin'},
        501: {'description': 'Not implemented. Esta función no está implementada aún, pero lo estará en futuras versiones.'},
    }
)


@router.get(
    '',
    name='Lista paginada',
    description='Lista de pagos paginada',
    responses={
        200: {'description': 'Lista de pagos paginada'},
        400: {'description': 'Bad Request. Revisa los parámetros de paginación o filtrado.'},
    }
)
async def get_paginated(
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
) -> PaymentPaginatedResponse:
    return await payment_controller.get_paginated(page, limit)


@router.post(
    '',
    name='Crear nuevo pago',
    status_code=201,
    responses={
        201: {'description': 'Pago creado exitosamente'},
        400: {'description': 'Bad Request. Revisa la info del body y/o parámetros'},
    }
)
async def create(new_payment: NewPaymentRequest) -> PaymentResponse:
    return await payment_controller.create(new_payment)


@router.get(
    '/{payment_id}',
    name='Obtener pago por ID',
    responses={
        200: {'description': 'Pago encontrado'},
        404: {'description': 'Pago no encontrado'},
    }
)
async def get_by_id(payment_id: Annotated[int, Path(ge=1, title='ID del gasto')]) -> PaymentResponse:
    return await payment_controller.get_by_id(payment_id)


@router.patch(
    '/{payment_id}',
    name='Actualizar pago por ID',
    responses={
        200: {'description': 'Pago actualizado exitosamente'},
        400: {'description': 'Bad Request. Revisa la info del body y/o parámetros'},
        404: {'description': 'Pago no encontrado'},
    }
)
async def update_by_id(
    payment_id: Annotated[int, Path(ge=1, title='ID del gasto')],
    payment_data: UpdatePaymentRequest,
) -> PaymentResponse:
    return await payment_controller.update(payment_id, payment_data)


@router.delete(
    '/{payment_id}',
    name='Eliminar pago por ID',
    status_code=204,
    responses={
        204: {'description': 'Pago eliminado exitosamente'},
        404: {'description': 'Pago no encontrado'},
    }
)
async def delete_by_id(payment_id: Annotated[int, Path(ge=1, title='ID del gasto')]) -> None:
    return await payment_controller.delete(payment_id)
