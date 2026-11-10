from typing import Any


class AppError(Exception):
    """Base application exception that maps cleanly to the unified JSON error contract."""

    def __init__(
        self,
        code: str,
        message: str,
        status_code: int = 400,
        details: Any = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details


class NotFoundError(AppError):
    def __init__(self, code: str = "RESOURCE_NOT_FOUND", message: str = "Không tìm thấy tài nguyên.") -> None:
        super().__init__(code=code, message=message, status_code=404)


class UnauthorizedError(AppError):
    def __init__(self, code: str = "UNAUTHORIZED", message: str = "Vui lòng đăng nhập để tiếp tục.") -> None:
        super().__init__(code=code, message=message, status_code=401)


class ForbiddenError(AppError):
    def __init__(self, code: str = "FORBIDDEN", message: str = "Bạn không có quyền thực hiện thao tác này.") -> None:
        super().__init__(code=code, message=message, status_code=403)


class ConflictError(AppError):
    def __init__(self, code: str = "CONFLICT", message: str = "Dữ liệu đã tồn tại.") -> None:
        super().__init__(code=code, message=message, status_code=409)


class BusinessRuleError(AppError):
    def __init__(self, code: str = "BUSINESS_RULE_VIOLATION", message: str = "Vi phạm quy tắc nghiệp vụ.") -> None:
        super().__init__(code=code, message=message, status_code=400)
