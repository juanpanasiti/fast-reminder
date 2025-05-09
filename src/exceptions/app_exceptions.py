from typing import Optional


class BaseAppExtension(Exception):
    default_message: str = 'UNKNOWN ERROR'

    def __init__(self, message: Optional[str] = None):
        self.message = message or self.default_message
        super().__init__(self.message)


class NotFoundError(BaseAppExtension):
    default_message = 'Recurso no encontrado'
