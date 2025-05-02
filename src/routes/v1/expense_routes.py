from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(
    prefix='/expenses',
    responses={
        400: {'description': 'Bad Request. Revisa la info del body y/o parámetros'},
        401: {'description': 'Unauthorized. Credenciales inválidas o no enviadas'},
        403: {'description': 'Forbidden. No tienes acceso a este recurso'},
        500: {'description': 'Internal Server Error. Error del servidor no manejado, contacta al sysadmin'},
        501: {'description': 'Not implemented. Esta función no está implementada aún, pero lo estará en futuras versiones.'},
    }
)


@router.get(
    '',  # Path
    name='Lista paginada',  # Se muestra al lado de la ruta en la docu
    description='Lista de gastos paginada',  # Se muestra debajo de la ruta
    summary='Listado de gastos paginados',  # Se muestra al lado de la ruta, pero reemplaza al name
    response_description='Retorna un objeto con la lista de resultado y la info de la paginación.',  # Descripción de la respuesta exitosa
    status_code=200,  # Código de estado de la respuesta exitosa
    responses={
        400: {'description': 'Bad Request. Revisa los parámetros de paginación o filtrado.'},
    }
)
async def get_paginated():
    # TODO: Implementar paginación
    # TODO: Implementar filtros
    # TODO: Implementar tipo de respuesta
    return {
        'results': [
            {
                'id': 1,
                'name': 'Factura de celular',
                'description': 'Factura claro. En marzo 2026 vence descuento sobre la línea.',
                'periodicity_in_months': 1,
                'last_payment_date': '2025-04-05',
                'next_payment_date': None,
                'estimated_next_payment_date': '2026-05-05',
                'payments': [],
                'has_pending_payments': False,
                'created_at': '2025-05-02T17:33:00Z',
                'updated_at': '2025-05-02T17:33:00Z',
            }
        ],
        'meta': {
            'current_page': 1,
            'total_pages': 1,
            'total_items': 1,
            'items_per_page': 10,
            'has_next_page': False,
            'has_previous_page': False,
        }
    }


@router.post(
    '',
    name='Crear nuevo gasto',
    status_code=201,
    responses={
        201: {'description': 'Nuevo gasto creado'},
        400: {'description': 'Revisa el body request'},
    }
)
async def create():
    # TODO: Recibir la data para crear el gasto.
    # Campos a recibir:
    # - name: str
    # - description: str (opcional)
    # - periodicity_in_months: int
    # - last_payment_date: date (optional)
    # - next_payment_date: date (optional)
    # - estimated_next_payment_date: date (optional)
    return {
        'id': 1,
        'name': 'Factura de celular',
        'description': 'Factura claro. En marzo 2026 vence descuento sobre la línea.',
        'periodicity_in_months': 1,
        'last_payment_date': '2025-04-05',
        'next_payment_date': None,
        'estimated_next_payment_date': '2026-05-05',
        'payments': [],
        'has_pending_payments': False,
        'created_at': '2025-05-02T17:33:00Z',
        'updated_at': '2025-05-02T17:33:00Z',
    }


@router.get(
    '/{expense_id}',
    name='Obtener gasto por ID',
    responses={
        200: {'description': 'Gasto encontrado'},
        404: {'description': 'Gasto no encontrado'},
    }
)
async def get_by_id(expense_id: Annotated[int, Path(ge=1, description='ID del gasto a buscar', title='ID del gasto')]):
    # TODO: Implementar búsqueda por ID
    return {
        'id': expense_id,
        'name': 'Factura de celular',
        'description': 'Factura claro. En marzo 2026 vence descuento sobre la línea.',
        'periodicity_in_months': 1,
        'last_payment_date': '2025-04-05',
        'next_payment_date': None,
        'estimated_next_payment_date': '2026-05-05',
        'payments': [],
        'has_pending_payments': False,
        'created_at': '2025-05-02T17:33:00Z',
        'updated_at': '2025-05-02T17:33:00Z',
    }


@router.patch(
    '/{expense_id}',
    name='Actualizar datos del pago por ID',
    responses={
        200: {'description': 'Gasto actualizado'},
        404: {'description': 'Gasto para actualizar no encontrado'},
    }
)
async def update_by_id(expense_id: Annotated[int, Path(ge=1, title='ID del gasto')]):
    # TODO: Implementar la actualización por ID
    # Campos a recibir:
    # - name: str (opcional)
    # - description: str (opcional)
    # - periodicity_in_months: int (opcional)
    # - last_payment_date: date (optional)
    # - next_payment_date: date (optional)
    # - estimated_next_payment_date: date (optional)
    return {
        'id': 1,
        'name': 'Factura de celular',
        'description': 'Factura claro. En marzo 2026 vence descuento sobre la línea.',
        'periodicity_in_months': 1,
        'last_payment_date': '2025-04-05',
        'next_payment_date': None,
        'estimated_next_payment_date': '2026-05-05',
        'payments': [],
        'has_pending_payments': False,
        'created_at': '2025-05-02T17:33:00Z',
        'updated_at': '2025-05-02T17:33:00Z',
    }


@router.delete(
    '/{expense_id}',
    name='Borrar un gasto por ID',
    status_code=204,
    responses={
        204: {'description': 'Gasto borrado'},
        404: {'description': 'Gasto para borrar no encontrado'},
    }
)
async def delete_by_id(expense_id: Annotated[int, Path(ge=1, title='ID del gasto')]) -> None:
    # TODO: Implementar borrado por ID
    return None
