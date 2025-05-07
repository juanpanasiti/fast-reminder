from typing import Optional, List
from datetime import date, datetime

from pydantic import BaseModel, Field
from pydantic_tooltypes import Partial

from .paginated_schemas import PaginationMeta


class NewExpenseRequest(BaseModel):
    name: str = Field(..., min_length=5, max_length=100)
    description: Optional[str] = Field('', max_length=500)
    periodicity_in_months: int = Field(..., ge=1, le=12)
    last_payment_date: Optional[date] = None
    next_payment_date: Optional[date] = None
    estimated_next_payment_date: Optional[date] = None

class UpdateExpenseRequest(Partial[NewExpenseRequest]):
    pass

# class UpdateExpenseRequest(BaseModel):
#     name: Optional[str] = Field(None, min_length=5, max_length=100)
#     description: Optional[str] = Field(None, max_length=500)
#     periodicity_in_months: Optional[int] = Field(None, ge=1, le=12)
#     last_payment_date: Optional[date] = None
#     next_payment_date: Optional[date] = None
#     estimated_next_payment_date: Optional[date] = None


class ExpenseResponse(BaseModel):
    id: int
    name: str
    description: str
    periodicity_in_months: int
    last_payment_date: Optional[date]
    next_payment_date: Optional[date]
    estimated_next_payment_date: Optional[date]
    payments: list = []
    has_pending_payments: bool
    created_at: datetime
    updated_at: datetime


class ExpensePaginatedResponse(BaseModel):
    results: List[ExpenseResponse]
    meta: PaginationMeta
