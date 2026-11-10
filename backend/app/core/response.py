from math import ceil
from typing import Any


def success_response(data: Any = None, message: str = "Thành công") -> dict[str, Any]:
    """Standard single-item / action response envelope."""
    return {
        "success": True,
        "message": message,
        "data": data,
    }


def paginated_response(
    items: list[Any],
    page: int,
    page_size: int,
    total_items: int,
) -> dict[str, Any]:
    """Standard paginated response envelope (NFR-02)."""
    total_pages = ceil(total_items / page_size) if page_size > 0 else 0
    return {
        "success": True,
        "data": items,
        "meta": {
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages,
        },
    }
