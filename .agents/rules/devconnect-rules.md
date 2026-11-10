---
description: Strict architectural, coding, security, and git workflow rules for the DevConnect project
---

# DevConnect Project Rules (Mandatory for All Developers & AI Agents)

You are working on **DevConnect** – a Technical Knowledge Sharing & Blogging Platform built for the Introduction to Software Engineering course.

## 1. Tech Stack & Architecture Baseline
- **Frontend (`frontend/`)**: Next.js 16 (App Router, TypeScript), TailwindCSS, ByteMD (Markdown editor), Axios.
- **Backend (`backend/`)**: FastAPI (Python 3.11), SQLAlchemy 2.0 ORM, Pydantic v2, Alembic migrations, JWT Authentication.
- **Database**: PostgreSQL 15.
- **Infrastructure**: Docker & Docker Compose, Nginx reverse proxy.

## 2. Strict Layered Architecture Rules
1. **Backend Separation of Concerns (`Router -> Service -> Model`)**:
   - `backend/app/api/v1/endpoints/`: Route handlers ONLY parse requests, inject dependencies (`db`, `current_user`), call services, and return standardized responses. **NEVER write direct SQLAlchemy queries (`db.query`/`db.execute`) or complex business logic inside route handlers.**
   - `backend/app/services/`: Contains all business rules (`BR-01` through `BR-10`), ownership checks, and database transactions.
   - `backend/app/models/`: SQLAlchemy 2.0 declarative models with explicit constraints (`ForeignKey`, `UniqueConstraint`, `CheckConstraint`, `Index`).
   - `backend/app/schemas/`: Pydantic v2 schemas for request validation and response serialization.
2. **Frontend Separation of Concerns**:
   - Never access the database directly from Next.js. All data operations go through Backend REST API (`/api/v1/...`).
   - Never rely solely on client-side role/ownership checks; backend always enforces authorization.

## 3. Mandatory Business & Security Rules (`BR-01` -> `BR-10`)
- **BR-01 (Roles)**: New users default to `USER` role. `ADMIN` cannot be self-assigned via registration or profile update endpoints.
- **BR-02 (Ownership)**: Only the article owner (`article.author_id == current_user.id`) can update, delete, or transition state (`DRAFT` <-> `PUBLISHED`) of their article.
- **BR-03 (Draft Privacy)**: `DRAFT` articles are strictly visible ONLY to their owner. Never return drafts in public feeds, search, or tag filters.
- **BR-04 (Tag Limit)**: Maximum 5 tags per article.
- **BR-05 (Unique Vote & Bookmark)**: At most 1 vote (`+1` or `-1`) and 1 bookmark per `(user_id, article_id)` pair, enforced by DB `UniqueConstraint`.
- **BR-06 (2-Level Comments)**: Comments support root comments (`parent_id IS NULL`) and 1 level of replies (`parent_id` pointing to a root comment). Reject replies to a reply with `400 Bad Request`.
- **BR-07 (Public Visibility)**: Public endpoints only return articles where `status == 'PUBLISHED' AND is_hidden == False AND deleted_at IS NULL`.
- **BR-08 (Series Ownership)**: A series can only contain `PUBLISHED` articles owned by the same author.
- **BR-09 (Vote Score)**: `vote_score = count(upvotes) - count(downvotes)`.
- **BR-10 (Tag Normalization)**: Tag names are trimmed and compared case-insensitively for uniqueness.
- **Upload Security (NFR-05)**: Only allow PNG, JPEG, WebP up to 5 MB; validate file content/MIME and generate safe random filenames.

## 4. API Contract & Pagination Standards
- Base path: `/api/v1`
- Standard Success Envelope: `{"success": true, "message": "...", "data": ...}`
- Standard Paginated Envelope: `{"success": true, "data": [...], "meta": {"page": 1, "page_size": 10, "total_items": 0, "total_pages": 0}}` (default `page_size=10`, max `50`).
- Standard Error Envelope: `{"success": false, "error": {"code": "ERROR_CODE", "message": "...", "details": null}}`

## 5. Git & Workflow Discipline
- Never commit directly to `main` or `develop`.
- Branch naming: `feature/US-xx-short-description`, `fix/US-xx-short-description`, `chore/DEV-xx-short-description`.
- Commit format: `<type>(<scope>): <imperative summary>` (e.g., `feat(US-11): add jwt authentication endpoints`).
- Never commit `.env`, secrets, `__pycache__`, `.venv`, `node_modules`, or `.next`.
