# DevConnect – Kiến trúc dự kiến

Tài liệu này là baseline kiến trúc trước khi bắt đầu viết source code. Mọi thay đổi lớn về boundary, công nghệ hoặc dữ liệu cần được cập nhật tại đây hoặc ghi thành Architecture Decision Record (ADR).

## 1. Kiến trúc tổng thể

DevConnect dự kiến dùng kiến trúc 3 tầng, triển khai theo mô hình client–server:

```text
Browser
   |
   v
Reverse Proxy / API Gateway
   |----------------------|
   v                      v
Frontend Web          Backend REST API
Next.js               FastAPI
                              |
                              v
                         PostgreSQL
```

### Các thành phần

| Thành phần | Trách nhiệm dự kiến | Công nghệ dự kiến |
|---|---|---|
| Web client | Hiển thị UI, điều hướng, gọi API, quản lý trạng thái giao diện | Next.js 16, React, TypeScript, TailwindCSS |
| API server | Auth, nghiệp vụ, phân quyền, validation, REST API | FastAPI, Python 3.11, SQLAlchemy |
| Database | Lưu trữ dữ liệu nghiệp vụ và ràng buộc toàn vẹn | PostgreSQL 15 |
| Migration | Version hóa thay đổi schema | Alembic |
| Reverse proxy | Routing `/` và `/api`, header, static/production entrypoint | Nginx |
| Delivery | Kiểm tra tự động và build/release | GitHub Actions |

## 2. Boundary dự kiến

### Frontend

Frontend chỉ chịu trách nhiệm về presentation và trải nghiệm người dùng. Không chứa business rule hoặc truy vấn trực tiếp PostgreSQL.

Các khu vực dự kiến:

```text
frontend/
├── app/                 # route và page
├── components/          # UI component dùng lại
├── features/            # auth, articles, comments, profile, admin...
├── lib/                 # API client, auth client, utility
├── types/               # kiểu dữ liệu phía client
└── public/              # asset tĩnh
```

### Backend

Backend chịu trách nhiệm về business rule, authentication/authorization, persistence và contract API.

Các khu vực dự kiến:

```text
backend/
├── app/
│   ├── api/             # route/controller và dependency
│   ├── core/            # config, security, error handling
│   ├── db/              # session, base model, repository primitives
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # request/response schemas
│   ├── services/        # business use cases
│   └── main.py          # application entrypoint
├── migrations/          # Alembic migrations
└── tests/               # unit/integration tests
```

## 3. Module nghiệp vụ dự kiến

- `auth`: registration, login, JWT, profile và role.
- `articles`: draft/published, ownership, public reading và moderation state.
- `tags`: tag catalog và quan hệ article–tag.
- `series`: series, thứ tự bài viết và navigation.
- `comments`: comment tối đa hai cấp, ownership và moderation.
- `votes`: mỗi user tối đa một vote/article, cho phép đổi lựa chọn.
- `bookmarks`: mỗi user tối đa một bookmark/article.
- `search`: tìm theo title, lọc tag và pagination.
- `admin`: moderation article và quản lý tag.

Mỗi module nên giữ route, schema, service, model/repository và test liên quan gần nhau; tránh để business logic trong route handler.

## 4. Luồng dữ liệu và nguyên tắc bảo mật

1. Browser gọi frontend hoặc `/api/*` qua reverse proxy.
2. Frontend gọi REST API bằng HTTP JSON.
3. Backend validate input bằng schema và kiểm tra JWT/role trước khi thực hiện use case.
4. Service xử lý nghiệp vụ; repository/model truy cập PostgreSQL.
5. Schema migration được tạo bằng Alembic và review cùng Pull Request.

Nguyên tắc bắt buộc:

- Không commit secret hoặc file `.env`.
- Password phải được hash; không lưu plaintext.
- JWT và permission check phải xử lý ở backend; frontend chỉ là lớp hiển thị.
- Draft chỉ trả về cho owner hoặc Admin theo rule nghiệp vụ.
- Các quan hệ cần uniqueness (vote, bookmark, tag normalized name) phải có database constraint, không chỉ kiểm tra ở UI.
- Upload file cần giới hạn loại file, kích thước và quyền truy cập trước khi triển khai thật.

## 5. Quyết định cần chốt trước khi code

- API contract và format lỗi thống nhất.
- Cách lưu ảnh: local storage cho development, object storage cho deployment nếu cần.
- Chiến lược refresh token/session.
- Pagination convention (`page/page_size` hoặc `cursor`).
- Soft delete hay hard delete cho từng loại dữ liệu.
- Quy tắc cấp tài khoản Admin ban đầu.
- Cách seed dữ liệu demo và reset database local.

Các quyết định này nên được ghi thành issue hoặc ADR trước khi module tương ứng bắt đầu.
