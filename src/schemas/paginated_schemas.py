from pydantic import BaseModel


class PaginationMeta(BaseModel):
    current_page: int
    total_pages: int
    total_items: int
    items_per_page: int
    has_next_page: bool
    has_previous_page: bool
