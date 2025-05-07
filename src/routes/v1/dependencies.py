from src.controllers.expense_controller import ExpenseController
from src.controllers.payment_controller import PaymentController

# Expense dependencies
expense_controller = ExpenseController(None)  # TODO: reemplazar con instancia de ExpenseService

# Payment dependencies
payment_controller = PaymentController(None)  # TODO: reemplazar con instancia de PaymentService
