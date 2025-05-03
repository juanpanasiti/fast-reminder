from typing import Optional, List
from datetime import date, datetime

from pydantic import BaseModel, Field

from .paginated_schemas import PaginationMeta


class NewPaymentRequest(BaseModel):
    expense_id: int = Field(..., ge=1)
    amount: float = Field(..., gt=0)
    due_date: Optional[date] = None
    paid_date: Optional[date] = None
    notes: Optional[str] = Field('', max_length=500)


class UpdatePaymentRequest(BaseModel):
    expense_id: Optional[int] = Field(None, ge=1)
    amount: Optional[float] = Field(None, gt=0)
    due_date: Optional[date] = None
    paid_date: Optional[date] = None
    notes: Optional[str] = Field(None, max_length=500)

class PaymentResponse(BaseModel):
    id: int
    expense_id: int
    amount: float
    due_date: date
    paid_date: date
    status: str
    notes: str
    created_at: datetime
    updated_at: datetime


class PaymentPaginatedResponse(BaseModel):
    results: List[PaymentResponse]
    meta: PaginationMeta
