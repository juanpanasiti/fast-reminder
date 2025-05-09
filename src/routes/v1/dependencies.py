from src.controllers.expense_controller import ExpenseController
from src.controllers.payment_controller import PaymentController
from src.services.expense_service import ExpenseService
from src.services.payment_service import PaymentService

# Expense dependencies
expense_service = ExpenseService(None)  # TODO: reemplazar con instancia de ExpenseRepository
expense_controller = ExpenseController(expense_service)

# Payment dependencies
payment_service = PaymentService(None)  # TODO: reemplazar con instancia de PaymentRepository
payment_controller = PaymentController(payment_service)
