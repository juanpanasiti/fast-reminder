from fastapi import APIRouter

from .expense_routes import router as expense_router
from .payment_routes import router as payment_router


router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(expense_router, tags=['Expenses'])
router_v1.include_router(payment_router, tags=['Payments'], deprecated=True)
