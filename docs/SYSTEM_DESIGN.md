# TÀI LIỆU THIẾT KẾ HỆ THỐNG (SYSTEM DESIGN DOCUMENT)
## DevConnect – Nền tảng chia sẻ kiến thức công nghệ và bài viết kỹ thuật

**Môn học:** Nhập môn Công nghệ Phần mềm  
**Phiên bản:** 1.0  
**Trạng thái:** Baseline cho Giai đoạn Thiết kế & Cài đặt

---

## Mục lục
1. [Thiết kế Cơ sở dữ liệu (ERD & Schema)](#1-thiết-kế-cơ-sở-dữ-liệu-erd--schema)
2. [Thiết kế Lớp (Class Diagram)](#2-thiết-kế-lớp-class-diagram)
3. [Sơ đồ Tuần tự (Sequence Diagrams)](#3-sơ-đồ-tuần-tự-sequence-diagrams)
4. [Đặc tả Giao diện Lập trình Ứng dụng (API Specification)](#4-đặc-tả-giao-diện-lập-trình-ứng-dụng-api-specification)

---

## 1. Thiết kế Cơ sở dữ liệu (ERD & Schema)

### 1.1. Sơ đồ Thực thể – Liên kết (ERD)

```mermaid
erDiagram
    USERS ||--o{ ARTICLES : "writes (author_id)"
    USERS ||--o{ SERIES : "creates (author_id)"
    USERS ||--o{ COMMENTS : "posts (user_id)"
    USERS ||--o{ VOTES : "casts (user_id)"
    USERS ||--o{ BOOKMARKS : "saves (user_id)"

    ARTICLES ||--o{ ARTICLE_TAGS : "has"
    TAGS ||--o{ ARTICLE_TAGS : "tagged_in"

    SERIES ||--o{ SERIES_ARTICLES : "contains"
    ARTICLES ||--o{ SERIES_ARTICLES : "belongs_to"

    ARTICLES ||--o{ COMMENTS : "has"
    COMMENTS ||--o{ COMMENTS : "replies_to (parent_id)"

    ARTICLES ||--o{ VOTES : "receives"
    ARTICLES ||--o{ BOOKMARKS : "bookmarked_in"

    USERS {
        int id PK
        string email UK "NOT NULL, UNIQUE"
        string username UK "NOT NULL, UNIQUE"
        string password_hash "NOT NULL"
        string full_name "NULLABLE"
        string bio "NULLABLE"
        string avatar_url "NULLABLE"
        string role "USER | ADMIN (default: USER)"
        boolean is_active "default: true"
        datetime created_at
        datetime updated_at
    }

    ARTICLES {
        int id PK
        int author_id FK "REFERENCES users(id)"
        string title "NOT NULL"
        string slug UK "NOT NULL, UNIQUE"
        string summary "NULLABLE"
        text content_markdown "NOT NULL"
        string cover_image_url "NULLABLE"
        string status "DRAFT | PUBLISHED"
        boolean is_hidden "default: false (Admin moderation)"
        int view_count "default: 0"
        datetime published_at "NULLABLE"
        datetime deleted_at "NULLABLE (Soft delete)"
        datetime created_at
        datetime updated_at
    }

    TAGS {
        int id PK
        string name "NOT NULL"
        string normalized_name UK "NOT NULL, UNIQUE (lowercase trimmed)"
        string slug UK "NOT NULL, UNIQUE"
        string description "NULLABLE"
        string color_hex "default: #3B82F6"
        datetime created_at
    }

    ARTICLE_TAGS {
        int article_id PK, FK "REFERENCES articles(id) ON DELETE CASCADE"
        int tag_id PK, FK "REFERENCES tags(id) ON DELETE CASCADE"
    }

    SERIES {
        int id PK
        int author_id FK "REFERENCES users(id)"
        string title "NOT NULL"
        string slug UK "NOT NULL, UNIQUE"
        text description "NULLABLE"
        datetime created_at
        datetime updated_at
    }

    SERIES_ARTICLES {
        int series_id PK, FK "REFERENCES series(id) ON DELETE CASCADE"
        int article_id PK, FK "REFERENCES articles(id) ON DELETE CASCADE"
        int position "NOT NULL (Order 1, 2, 3...)"
    }

    COMMENTS {
        int id PK
        int article_id FK "REFERENCES articles(id) ON DELETE CASCADE"
        int user_id FK "REFERENCES users(id)"
        int parent_id FK "NULLABLE, REFERENCES comments(id) ON DELETE CASCADE"
        text content "NOT NULL"
        boolean is_deleted "default: false"
        datetime created_at
        datetime updated_at
    }

    VOTES {
        int id PK
        int user_id FK "REFERENCES users(id) ON DELETE CASCADE"
        int article_id FK "REFERENCES articles(id) ON DELETE CASCADE"
        smallint value "1 (Upvote) | -1 (Downvote)"
        datetime created_at
        datetime updated_at
    }

    BOOKMARKS {
        int id PK
        int user_id FK "REFERENCES users(id) ON DELETE CASCADE"
        int article_id FK "REFERENCES articles(id) ON DELETE CASCADE"
        datetime created_at
    }
```

### 1.2. Ràng buộc Toàn vẹn CSDL (Database Constraints)
Để đảm bảo tuân thủ các quy tắc nghiệp vụ `BR-01` $\rightarrow$ `BR-10` và `NFR-06`:
1. **Bảng `users`**:
   * `uq_users_email`: Unique index trên `LOWER(email)`.
   * `ck_users_role`: `role IN ('USER', 'ADMIN')`.
2. **Bảng `articles`**:
   * `ck_articles_status`: `status IN ('DRAFT', 'PUBLISHED')`.
   * Index tìm kiếm trên `(status, is_hidden, deleted_at, published_at DESC)` để tối ưu truy vấn trang chủ và tìm kiếm (`NFR-01`).
3. **Bảng `tags` & `article_tags`**:
   * `uq_tags_normalized_name`: Unique constraint trên `normalized_name` (đã `trim()` và `lower()`, đáp ứng `BR-10`).
   * Khoá chính phức hợp `PRIMARY KEY (article_id, tag_id)`. Service kiểm tra tối đa 5 tag/bài (`BR-04`).
4. **Bảng `series_articles`**:
   * `uq_series_position`: `UNIQUE (series_id, position)` đảm bảo thứ tự bài viết trong chuỗi không bị trùng (`BR-08`).
5. **Bảng `votes`**:
   * `uq_votes_user_article`: `UNIQUE (user_id, article_id)` đảm bảo mỗi user chỉ vote 1 lần trên 1 bài (`BR-05`).
   * `ck_votes_value`: `value IN (1, -1)`.
6. **Bảng `bookmarks`**:
   * `uq_bookmarks_user_article`: `UNIQUE (user_id, article_id)` đảm bảo không lưu trùng bookmark (`BR-05`).

---

## 2. Thiết kế Lớp (Class Diagram)

Sơ đồ dưới đây biểu diễn kiến trúc phân tầng của Backend (**Models $\leftarrow$ Services $\leftarrow$ Routers**):

```mermaid
classDiagram
    class User {
        +int id
        +str email
        +str username
        +str password_hash
        +str role
        +bool is_active
    }

    class Article {
        +int id
        +int author_id
        +str title
        +str slug
        +str content_markdown
        +str status
        +bool is_hidden
        +datetime published_at
        +datetime deleted_at
    }

    class Tag {
        +int id
        +str name
        +str normalized_name
        +str slug
        +str color_hex
    }

    class Series {
        +int id
        +int author_id
        +str title
        +str slug
        +str description
    }

    class Comment {
        +int id
        +int article_id
        +int user_id
        +int parent_id
        +str content
    }

    class Vote {
        +int id
        +int user_id
        +int article_id
        +int value
    }

    class Bookmark {
        +int id
        +int user_id
        +int article_id
    }

    class AuthService {
        +register_user(db, payload) User
        +authenticate_user(db, email, password) TokenResponse
        +get_current_user(db, token) User
        +update_profile(db, user, payload) User
    }

    class ArticleService {
        +list_public_articles(db, q, tag, page, page_size) PaginatedArticles
        +get_article_by_slug(db, slug, current_user) ArticleDetail
        +create_article(db, author, payload) Article
        +update_article(db, author, article_id, payload) Article
        +change_status(db, author, article_id, status) Article
        +delete_article(db, author, article_id) void
    }

    class InteractionService {
        +cast_vote(db, user, article_id, value) VoteResult
        +toggle_bookmark(db, user, article_id) BookmarkResult
        +add_comment(db, user, article_id, content, parent_id) Comment
        +delete_comment(db, user, comment_id) void
    }

    class AdminService {
        +moderate_article(db, admin, article_id, action) Article
        +create_tag(db, admin, payload) Tag
        +update_tag(db, admin, tag_id, payload) Tag
        +delete_tag(db, admin, tag_id) void
    }

    User "1" --> "*" Article : writes
    User "1" --> "*" Series : owns
    Article "*" --> "*" Tag : tagged_with
    Series "*" --> "*" Article : orders
    Article "1" --> "*" Comment : contains
    Article "1" --> "*" Vote : receives
    Article "1" --> "*" Bookmark : saved_in

    AuthService ..> User : manages
    ArticleService ..> Article : manages
    ArticleService ..> Tag : attaches
    InteractionService ..> Comment : manages
    InteractionService ..> Vote : manages
    InteractionService ..> Bookmark : manages
    AdminService ..> Article : moderates
    AdminService ..> Tag : manages
```

---

## 3. Sơ đồ Tuần tự (Sequence Diagrams)

### 3.1. Luồng Đăng nhập & Xác thực JWT (US-11)

```mermaid
sequenceDiagram
    autonumber
    actor U as Người dùng
    participant FE as Next.js Frontend
    participant API as FastAPI AuthRouter
    participant SVC as AuthService
    participant DB as PostgreSQL

    U->>FE: Nhập Email & Mật khẩu, nhấn "Đăng nhập"
    FE->>API: POST /api/v1/auth/login {email, password}
    API->>SVC: authenticate_user(db, email, password)
    SVC->>DB: SELECT * FROM users WHERE LOWER(email) = LOWER(:email)
    DB-->>SVC: User record (hoặc NULL)
    alt Email không tồn tại hoặc sai mật khẩu
        SVC-->>API: Raise InvalidCredentialsError (401)
        API-->>FE: 401 Unauthorized {error: "INVALID_CREDENTIALS"}
        FE-->>U: Hiển thị thông báo lỗi
    else Thông tin hợp lệ
        SVC->>SVC: verify_password(plain, password_hash)
        SVC->>SVC: create_access_token(user_id, role)
        SVC-->>API: {access_token, token_type: "bearer", user}
        API-->>FE: 200 OK {success: true, data: {access_token, user}}
        FE-->>U: Lưu token & chuyển hướng về Trang chủ
    end
```

### 3.2. Luồng Tạo & Xuất bản Bài viết kèm Tag (US-06, US-07)

```mermaid
sequenceDiagram
    autonumber
    actor A as Tác giả (Đã đăng nhập)
    participant FE as Next.js (ByteMD Editor)
    participant API as FastAPI ArticleRouter
    participant SVC as ArticleService
    participant DB as PostgreSQL

    A->>FE: Soạn Markdown, chọn tối đa 5 Tag, nhấn "Xuất bản" (hoặc "Lưu nháp")
    FE->>API: POST /api/v1/articles (Header: Bearer JWT)
    API->>API: Verify JWT -> current_user
    API->>SVC: create_article(db, current_user, payload)
    alt Số lượng Tag > 5 (Vi phạm BR-04)
        SVC-->>API: Raise ValidationError("Tối đa 5 Tag mỗi bài")
        API-->>FE: 422 Unprocessable Entity
    else Hợp lệ
        SVC->>SVC: Sanitize Markdown/HTML & Sinh unique slug từ title
        SVC->>DB: BEGIN TRANSACTION
        SVC->>DB: INSERT INTO articles (author_id, title, slug, status, ...)
        SVC->>DB: INSERT INTO article_tags (article_id, tag_id)
        SVC->>DB: COMMIT
        DB-->>SVC: Article instance
        SVC-->>API: ArticleDetail
        API-->>FE: 201 Created {success: true, data: article}
        FE-->>A: Chuyển hướng tới trang chi tiết bài viết
    end
```

### 3.3. Luồng Bình luận 2 cấp (US-05 / BR-06)

```mermaid
sequenceDiagram
    autonumber
    actor U as Người dùng đã đăng nhập
    participant FE as Next.js Frontend
    participant API as FastAPI CommentRouter
    participant SVC as InteractionService
    participant DB as PostgreSQL

    U->>FE: Nhập nội dung bình luận (kèm parent_id nếu là trả lời)
    FE->>API: POST /api/v1/articles/{id}/comments {content, parent_id}
    API->>SVC: add_comment(db, current_user, article_id, content, parent_id)
    SVC->>DB: Kiểm tra bài viết tồn tại & đang PUBLISHED
    opt Có truyền parent_id (Trả lời bình luận)
        SVC->>DB: SELECT id, parent_id FROM comments WHERE id = :parent_id
        alt Bình luận cha đã có parent_id != NULL (Cấp 3 - Vi phạm BR-06)
            SVC-->>API: Raise BusinessRuleError("Chỉ hỗ trợ bình luận tối đa 2 cấp")
            API-->>FE: 400 Bad Request
        end
    end
    SVC->>DB: INSERT INTO comments (article_id, user_id, parent_id, content)
    DB-->>SVC: New Comment
    SVC-->>API: CommentSchema
    API-->>FE: 201 Created {success: true, data: comment}
    FE-->>U: Hiển thị bình luận mới ngay dưới bài viết
```

### 3.4. Luồng Upvote / Downvote Bài viết (US-04 / BR-05, BR-09)

```mermaid
sequenceDiagram
    autonumber
    actor U as Người dùng đã đăng nhập
    participant FE as Next.js Frontend
    participant API as FastAPI VoteRouter
    participant SVC as InteractionService
    participant DB as PostgreSQL

    U->>FE: Nhấn nút Upvote (+1) hoặc Downvote (-1)
    FE->>API: POST /api/v1/articles/{id}/vote {value: 1 | -1 | 0}
    API->>SVC: cast_vote(db, current_user, article_id, value)
    SVC->>DB: SELECT * FROM votes WHERE user_id = :uid AND article_id = :aid
    alt value == 0 hoặc trùng lựa chọn hiện tại (Hủy vote)
        SVC->>DB: DELETE FROM votes WHERE id = :vote_id
    else Chưa có vote
        SVC->>DB: INSERT INTO votes (user_id, article_id, value)
    else Đổi từ Upvote sang Downvote (hoặc ngược lại)
        SVC->>DB: UPDATE votes SET value = :new_value WHERE id = :vote_id
    end
    SVC->>DB: SELECT COALESCE(SUM(value), 0) FROM votes WHERE article_id = :aid
    DB-->>SVC: new_vote_score
    SVC-->>API: {user_vote, vote_score}
    API-->>FE: 200 OK {success: true, data: {user_vote, vote_score}}
    FE-->>U: Cập nhật điểm số trên giao diện
```

---

## 4. Đặc tả Giao diện Lập trình Ứng dụng (API Specification)

Tất cả các endpoint đều bắt đầu bằng `/api/v1`.

| Phân hệ | Method | Endpoint | Quyền | Mô tả & User Story |
|:---|:---:|:---|:---:|:---|
| **Health** | `GET` | `/api/v1/health` | Public | Kiểm tra trạng thái Backend & Database (`NFR-07`) |
| **Auth** (Quân) | `POST` | `/api/v1/auth/register` | Public | Đăng ký tài khoản mới (`US-11`) |
| | `POST` | `/api/v1/auth/login` | Public | Đăng nhập nhận JWT (`US-11`) |
| | `GET` | `/api/v1/users/me` | User | Lấy thông tin cá nhân hiện tại (`US-11`) |
| | `PATCH` | `/api/v1/users/me` | User | Cập nhật hồ sơ cá nhân (`US-11`) |
| **Articles** (Trường) | `GET` | `/api/v1/articles` | Public | Danh sách bài Published + Tìm kiếm `q` + Lọc `tag` + Phân trang (`US-01, US-02`) |
| | `GET` | `/api/v1/articles/{slug}` | Public / Owner | Xem chi tiết bài viết (`US-01`, Owner xem được `DRAFT`) |
| | `POST` | `/api/v1/articles` | User | Tạo bài viết mới (`DRAFT` hoặc `PUBLISHED` - `US-06, US-07`) |
| | `PUT` | `/api/v1/articles/{id}` | Owner | Cập nhật nội dung/trạng thái bài viết (`US-07`) |
| | `DELETE` | `/api/v1/articles/{id}` | Owner | Xóa bài viết của mình (`US-07`) |
| | `GET` | `/api/v1/me/articles` | User | Danh sách bài viết (cả `DRAFT` & `PUBLISHED`) của chính tác giả (`US-07`) |
| **Uploads** (Trường) | `POST` | `/api/v1/uploads/images` | User | Upload ảnh Markdown (PNG/JPG/WebP $\le$ 5MB - `US-06, NFR-05`) |
| **Series** (Trường) | `GET` | `/api/v1/series` | Public | Danh sách các Series học tập (`US-08`) |
| | `GET` | `/api/v1/series/{slug}` | Public | Xem chi tiết Series và danh sách bài theo thứ tự (`US-08`) |
| | `POST` | `/api/v1/series` | User | Tạo Series mới (`US-08`) |
| | `PUT` | `/api/v1/series/{id}` | Owner | Cập nhật Series & sắp xếp thứ tự bài viết (`US-08`) |
| | `DELETE` | `/api/v1/series/{id}` | Owner | Xóa Series của mình (`US-08`) |
| **Tags** (Trường) | `GET` | `/api/v1/tags` | Public | Lấy danh sách toàn bộ Tag (`US-02, US-10`) |
| **Comments** (Nguyên)| `GET` | `/api/v1/articles/{id}/comments` | Public | Lấy danh sách bình luận 2 cấp của bài viết (`US-05`) |
| | `POST` | `/api/v1/articles/{id}/comments` | User | Thêm bình luận gốc hoặc trả lời (`US-05`) |
| | `DELETE` | `/api/v1/comments/{id}` | Owner / Admin | Xóa bình luận của mình (`US-05`) |
| **Votes** (Nguyên) | `POST` | `/api/v1/articles/{id}/vote` | User | Upvote (`+1`), Downvote (`-1`) hoặc hủy vote (`0`) (`US-04`) |
| **Bookmarks**(Nguyên)| `GET` | `/api/v1/me/bookmarks` | User | Xem danh sách bài viết đã lưu (`US-03`) |
| | `POST` | `/api/v1/articles/{id}/bookmark` | User | Thêm / Bỏ lưu bài viết (`US-03`) |
| **Admin** (Trường) | `GET` | `/api/v1/admin/articles` | Admin | Liệt kê bài viết để kiểm duyệt (`US-09`) |
| | `PATCH` | `/api/v1/admin/articles/{id}/moderation` | Admin | Ẩn (`hide`), Hiện (`unhide`) hoặc Xóa (`delete`) bài vi phạm (`US-09`) |
| | `POST` | `/api/v1/admin/tags` | Admin | Tạo Tag mới (`US-10`) |
| | `PUT` | `/api/v1/admin/tags/{id}` | Admin | Sửa thông tin Tag (`US-10`) |
| | `DELETE` | `/api/v1/admin/tags/{id}` | Admin | Xóa Tag (`US-10`) |
