from fastapi import APIRouter

router = APIRouter(prefix='/expenses')


@router.get('', name='Lista paginada', description='LIsta de expenses paginada')
async def get_paginated():
    return []


@router.post('')
async def create():
    return {}


@router.get('/{expense_id}')
async def get_by_id(expense_id: int):
    return {}


@router.patch('/{expense_id}')
async def update_by_id(expense_id: int):
    return {}


@router.delete('/{expense_id}')
async def delete_by_id(expense_id: int):
    return None
