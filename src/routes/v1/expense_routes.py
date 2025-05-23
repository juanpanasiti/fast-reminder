from typing import Annotated

from fastapi import APIRouter, Path, Query, Depends

from src.dependencies.auth_dependencies import get_token
from src.schemas.expense_schemas import NewExpenseRequest, UpdateExpenseRequest, ExpenseResponse, ExpensePaginatedResponse
from src.schemas.auth_schemas import DecodedJwt
from .dependencies import expense_controller


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
async def get_paginated(
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
    token: DecodedJwt = Depends(get_token)
) -> ExpensePaginatedResponse:
    return await expense_controller.get_paginated(token.user_id, page, limit)


@router.post(
    '',
    name='Crear nuevo gasto',
    status_code=201,
    responses={
        201: {'description': 'Nuevo gasto creado'},
        400: {'description': 'Revisa el body request'},
    }
)
async def create(new_expense: NewExpenseRequest, token: DecodedJwt = Depends(get_token)) -> ExpenseResponse:
    return await expense_controller.create(token.user_id, new_expense)


@router.get(
    '/{expense_id}',
    name='Obtener gasto por ID',
    responses={
        200: {'description': 'Gasto encontrado'},
        404: {'description': 'Gasto no encontrado'},
    }
)
async def get_by_id(
    expense_id: Annotated[int, Path(ge=1, description='ID del gasto a buscar', title='ID del gasto')],
    token: DecodedJwt = Depends(get_token)
) -> ExpenseResponse:
    return await expense_controller.get_by_id(token.user_id, expense_id)


@router.patch(
    '/{expense_id}',
    name='Actualizar datos del pago por ID',
    responses={
        200: {'description': 'Gasto actualizado'},
        404: {'description': 'Gasto para actualizar no encontrado'},
    }
)
async def update_by_id(
    expense_id: Annotated[int, Path(ge=1, title='ID del gasto')],
    expense_data: UpdateExpenseRequest,
    token: DecodedJwt = Depends(get_token)
) -> ExpenseResponse:
    return await expense_controller.update(token.user_id, expense_id, expense_data)


@router.delete(
    '/{expense_id}',
    name='Borrar un gasto por ID',
    status_code=204,
    responses={
        204: {'description': 'Gasto borrado'},
        404: {'description': 'Gasto para borrar no encontrado'},
    }
)
async def delete_by_id(
    expense_id: Annotated[int, Path(ge=1, title='ID del gasto')],
    token: DecodedJwt = Depends(get_token)
) -> None:
    return await expense_controller.delete(token.user_id, expense_id)
