from fastapi import APIRouter

router = APIRouter(prefix='/payments')


@router.get('')
async def get_paginated():
    return []


@router.post('')
async def create():
    return {}


@router.get('/{payment_id}')
async def get_by_id(payment_id: int):
    return {}


@router.patch('/{payment_id}')
async def update_by_id(payment_id: int):
    return {}


@router.delete('/{payment_id}')
async def delete_by_id(payment_id: int):
    return None
