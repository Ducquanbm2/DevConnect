from fastapi import APIRouter

from app.api.v1.endpoints import health

api_router = APIRouter()

# Module 0: Health check (NFR-07)
api_router.include_router(health.router, tags=["Health"])

# Các thành viên sẽ đăng ký thêm router của mình tại đây:
# - Nguyễn Đức Quân (US-11): auth.router, users.router
# - Trần Nhật Trường (US-01, US-02, US-06..US-10): articles.router, series.router, tags.router, admin.router
# - Trần Văn Nguyên (US-03, US-04, US-05): comments.router, votes.router, bookmarks.router
