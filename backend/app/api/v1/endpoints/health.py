from fastapi import APIRouter

from app.core.config import settings
from app.core.response import success_response

router = APIRouter()


@router.get("/health", summary="Kiểm tra trạng thái hệ thống (NFR-07)")
def health_check() -> dict:
    return success_response(
        data={
            "service": settings.PROJECT_NAME,
            "version": settings.VERSION,
            "environment": settings.ENVIRONMENT,
            "status": "healthy",
        },
        message="DevConnect API đang hoạt động bình thường.",
    )
