from src.controllers.expense_controller import ExpenseController
from src.controllers.payment_controller import PaymentController
from src.controllers.auth_controller import AuthController
from src.services.expense_service import ExpenseService
from src.services.payment_service import PaymentService
from src.services.auth_service import AuthService

# Expense dependencies
expense_service = ExpenseService()
expense_controller = ExpenseController(expense_service)

# Payment dependencies
payment_service = PaymentService()
payment_controller = PaymentController(payment_service)

# Auth dependencies
auth_service = AuthService()
auth_controller = AuthController(auth_service)
