from typing import Annotated

from fastapi import APIRouter, Path, Query

from src.schemas.payment_schemas import NewPaymentRequest, UpdatePaymentRequest

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
async def get_paginated(page: Annotated[int, Query(ge=1)] = 1, limit: Annotated[int, Query(ge=1, le=100)] = 10):
    return {
        'results': [
            {
                'id': 1,
                'expense_id': 1,
                'amount': 100.0,
                'due_date': '2025-05-05',
                'paid_date': '2025-05-05',
                'status': 'paid',
                'notes': 'Pago realizado con tarjeta de crédito.',
                'created_at': '2025-05-02T17:33:00Z',
                'updated_at': '2025-05-02T17:33:00Z',
            }
        ],
        'meta': {
            'current_page': page,
            'total_pages': 1,
            'total_items': 1,
            'items_per_page': limit,
            'has_next_page': False,
            'has_previous_page': False,
        }
    }


@router.post(
    '',
    name='Crear nuevo pago',
    status_code=201,
    responses={
        201: {'description': 'Pago creado exitosamente'},
        400: {'description': 'Bad Request. Revisa la info del body y/o parámetros'},
    }
)
async def create(new_payment: NewPaymentRequest):
    # TODO: Implementar creación de pago
    # Campost requeridos:
    # - expense_id: int
    # - amount: float
    # - due_date: date (opcional)
    # - paid_date: date (opcional)
    # - notes: str (opcional)
    return {
        'id': 1,
        'expense_id': 1,
        'amount': 100.0,
        'due_date': '2025-05-05',
        'paid_date': '2025-05-05',
        'status': 'paid',
        'notes': 'Pago realizado con tarjeta de crédito.',
        'created_at': '2025-05-02T17:33:00Z',
        'updated_at': '2025-05-02T17:33:00Z',
    }


@router.get(
    '/{payment_id}',
    name='Obtener pago por ID',
    responses={
        200: {'description': 'Pago encontrado'},
        404: {'description': 'Pago no encontrado'},
    }
)
async def get_by_id(payment_id: Annotated[int, Path(ge=1, title='ID del gasto')]):
    return {
        'id': payment_id,
        'expense_id': 1,
        'amount': 100.0,
        'due_date': '2025-05-05',
        'paid_date': '2025-05-05',
        'status': 'paid',
        'notes': 'Pago realizado con tarjeta de crédito.',
        'created_at': '2025-05-02T17:33:00Z',
        'updated_at': '2025-05-02T17:33:00Z',
    }


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
):
    return {
        'id': payment_id,
        'expense_id': 1,
        'amount': 100.0,
        'due_date': '2025-05-05',
        'paid_date': '2025-05-05',
        'status': 'paid',
        'notes': 'Pago realizado con tarjeta de crédito.',
        'created_at': '2025-05-02T17:33:00Z',
        'updated_at': '2025-05-02T17:33:00Z',
    }


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
    return None
