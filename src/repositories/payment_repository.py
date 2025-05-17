from .base_repository import BaseRepository
from src.database.models import PaymentModel


class PaymentRepository(BaseRepository):
    def __init__(self):
        super().__init__(PaymentModel)
