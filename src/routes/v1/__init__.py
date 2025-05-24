from fastapi import APIRouter

from .expense_routes import router as expense_router
from .payment_routes import router as payment_router
from .auth_routes import router as auth_router
from .user_routes import router as user_router


router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(auth_router, tags=['Auth'])
router_v1.include_router(user_router, tags=['User'])
router_v1.include_router(expense_router, tags=['Expenses'])
router_v1.include_router(payment_router, tags=['Payments'])
