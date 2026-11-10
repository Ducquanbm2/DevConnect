# DevConnect – Nền tảng chia sẻ kiến thức công nghệ và bài viết kỹ thuật

DevConnect là nền tảng web chuyên biệt dành cho kỹ sư phần mềm, sinh viên CNTT và người yêu công nghệ để viết, chia sẻ và thảo luận các bài viết kỹ thuật có mã nguồn (Markdown + Syntax Highlighting + Series học tập).

---

## 1. Tài liệu Dự án (Chuẩn Quy trình Công nghệ Phần mềm)

Toàn bộ tài liệu đặc tả và quy tắc làm việc của nhóm nằm trong thư mục [`docs/`](docs/):

1. **Khởi tạo & Quản lý Dự án:**
   - [Project Charter](docs/project_chapter.md) – Tuyên bố dự án, phạm vi & phân công 4 thành viên.
   - [Project Proposal](docs/DevConnect-ProjectProposal.md) – Đề cương chi tiết 15 tuần.
2. **Phân tích Yêu cầu (SRS - Giai đoạn 1):**
   - [Báo cáo Phân tích Yêu cầu](docs/DevConnect-AnalysisReport.md) – Danh sách Stakeholder, 11 User Stories (`US-01` $\rightarrow$ `US-11`), 12 NFR, Quy tắc nghiệp vụ (`BR-01` $\rightarrow$ `BR-10`), Use Case Diagram & Đặc tả chi tiết 11 Use Case.
3. **Thiết kế Hệ thống (SDD - Giai đoạn 2):**
   - [Tài liệu Thiết kế Hệ thống](docs/SYSTEM_DESIGN.md) – Sơ đồ CSDL (ERD 9 bảng), Class Diagram, Sequence Diagrams và bảng Đặc tả RESTful API Contract.
   - [Kiến trúc Dự kiến](docs/ARCHITECTURE.md) – Kiến trúc 3 tầng (`Next.js` – `FastAPI` – `PostgreSQL`).
   - [Đặc tả Giao diện Frontend](docs/DevConnect-Frontend-Specs.md) – Thiết kế UI/UX & Prototype.
4. **Quy tắc Làm việc & Đóng góp (BẮT BUỘC ĐỌC):**
   - [**Bộ Quy tắc & Quy trình Phát triển (Team Rules)**](docs/DEVELOPMENT_PROCESS.md) – Phân công module, Gitflow, Conventional Commits, Kiến trúc 3 tầng, Chuẩn JSON API & 10 Quy tắc nghiệp vụ bất khả xâm phạm.
   - [Hướng dẫn Đóng góp nhanh](docs/CONTRIBUTING.md)
   - [Rules cho AI Coding Agent](AGENTS.md) (`.agents/rules/devconnect-rules.md`)

---

## 2. Cấu trúc Thư mục Dự án

```text
DevConnect/
├── backend/                  # FastAPI (Python 3.11) + SQLAlchemy 2.0 + Alembic
│   ├── app/
│   │   ├── api/v1/endpoints/ # Tầng HTTP Router/Controller (không viết SQL trực tiếp)
│   │   ├── core/             # Config, JWT Security, Exceptions, Standard Response
│   │   ├── db/               # SQLAlchemy Session & Declarative Base
│   │   ├── models/           # 9 Bảng ORM (User, Article, Tag, Series, Comment, Vote, Bookmark)
│   │   ├── schemas/          # Pydantic v2 Request/Response Schemas
│   │   ├── services/         # Tầng Business Logic & Ownership checks (BR-01 -> BR-10)
│   │   └── main.py           # FastAPI Application Entrypoint
│   └── tests/                # Pytest Unit & API Integration Tests
├── frontend/                 # Next.js 16 (App Router, TypeScript, TailwindCSS, ByteMD)
│   └── src/
│       ├── app/              # Next.js Pages & Layouts
│       ├── components/       # UI Components dùng chung
│       ├── features/         # Các phân hệ nghiệp vụ
│       ├── lib/              # Axios API Client (tự động đính kèm JWT)
│       └── types/            # TypeScript Interfaces đồng bộ với Backend
├── docs/                     # Tài liệu SRS, System Design, Team Rules
├── docker-compose.yml        # Khởi chạy PostgreSQL 15 + Backend + Frontend
└── .env.example              # File mẫu cấu hình biến môi trường
```

---

## 3. Hướng dẫn Khởi chạy Nhanh (Quick Start)

### Cách 1: Chạy toàn bộ bằng Docker Compose (Khuyên dùng)
```bash
# 1. Tạo file .env từ mẫu
cp .env.example .env

# 2. Khởi chạy PostgreSQL, Backend và Frontend
docker compose up --build
```
* **Frontend:** `http://localhost:3000`
* **Backend Swagger UI:** `http://localhost:8000/docs`
* **Health Check API:** `http://localhost:8000/api/v1/health`

### Cách 2: Chạy Backend & Test ở máy Local
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Chạy linter & unit test
ruff check .
pytest -v

# Chạy dev server
uvicorn app.main:app --reload --port 8000
```
