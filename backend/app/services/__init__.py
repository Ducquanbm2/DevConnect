"""
Service Layer (Business Logic)
------------------------------
Quy tắc bắt buộc:
- Toàn bộ logic nghiệp vụ (BR-01 -> BR-10), kiểm tra quyền sở hữu (Ownership)
  và truy vấn SQLAlchemy phải được viết tại các module trong thư mục này.
- Không viết trực tiếp câu lệnh query database ở tầng Router (api/v1/endpoints).
"""
