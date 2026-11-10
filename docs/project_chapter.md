# Project Charter

## Project Information
- **Project Name:** DevConnect – Nền tảng chia sẻ kiến thức công nghệ và bài viết kỹ thuật (Technical Knowledge Sharing & Blogging Platform)
- **Project Description:** DevConnect is a specialized web platform designed for software engineers, IT students, and technology enthusiasts to publish, share, and discover technical articles and tutorials. Addressing the limitations of general social media and generic blog platforms, DevConnect provides a native Markdown editor (ByteMD) with code syntax highlighting and live preview, structured multi-part learning series (Series), specialized topic tagging (Tags), and interactive community engagement features (2-level nested comments, upvote/downvote, bookmarking) alongside robust administrative moderation.
- **Project Goals:**
  - Develop a high-performance, responsive web application utilizing a clean 3-tier architecture (Next.js 16, FastAPI, PostgreSQL 15, Docker).
  - Deliver a native Markdown (GFM) authoring experience with live preview, multi-language code syntax highlighting, and inline image uploading.
  - Enable structured technical knowledge sharing via multi-article Series and fine-grained categorization via topic Tags.
  - Foster active technical discussions through interactive 2-level nested comments, voting (Upvote/Downvote), and personal bookmarks.
  - Implement role-based access control with administrative governance tools (article moderation, tag lifecycle management).
  - Complete the project within 15 academic weeks, adhering to software engineering standards with a 0 VNĐ budget leveraging free-tier developer tools and cloud services.
- **Target Users:**
  - **Guests / Readers (Unauthenticated):** Browse published articles with syntax highlighting, search articles by title, and filter articles by tags without creating an account.
  - **Authors / Developers (Authenticated Users):** Create and edit articles (Draft/Published workflow), organize articles into learning Series, bookmark favorites, cast votes, and participate in technical discussions via comments.
  - **Administrators (Admin):** Moderate content by hiding or removing violating posts and manage the platform tag catalog.
- **Timeline:** 15 weeks (Semester 1, Academic Year 2026–2027) + 2 weeks post-delivery maintenance
  - **Phase 1: Requirements Analysis (Weeks 1–3):** Requirements gathering, SRS specification ([ISO/IEC/IEEE 29148:2018](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29148%3Aed-2%3Av1%3Aen)), Use Case diagrams (UML 2.0), and 11 User Stories (US-01 → US-11).
  - **Phase 2: System Design (Weeks 4–6):** Database schema (ERD), Service Class Diagrams, API Specifications (Postman Collection), UI/UX wireframes and mockups (Figma), and development Docker Compose setup.
  - **Phase 3: Implementation & Integration (Weeks 7–11):** Backend REST APIs (FastAPI), Frontend client (Next.js 16 + TailwindCSS + ByteMD), database migrations (Alembic), and integration.
  - **Phase 4: Testing & Quality Assurance (Weeks 12–13):** Test Plan, ≥30 Test Cases, Unit Testing with pytest, manual functional testing, API testing, and bug fixing.
  - **Phase 5: Deployment, Handover & Maintenance (Weeks 14–15 + 2 weeks maintenance):** Docker/Nginx production deployment, User Guide documentation, final presentation demo, and GitHub release tag `v1.0.0`.

## Team
- **Project Lead:** Nguyễn Đức Quân (MSSV: 24120218)
- **Product Owner:** Nguyễn Đức Quân (MSSV: 24120218)
- **Technical Lead:** Nguyễn Đức Quân (MSSV: 24120218) – System Architecture, Database Design, Auth & User Management module
- **Developers:**
  - **Trần Nhật Trường (MSSV: 24120486)** – Backend Developer (Article, Series, Tag, and Search APIs)
  - **Trần Lê Đức Việt (MSSV: 24120245)** – Frontend Developer (UI/UX design, Next.js 16, TailwindCSS, ByteMD Editor)
  - **Trần Văn Nguyên (MSSV: 24120205)** – Fullstack Developer (Comment, Vote, and Bookmark modules)
- **QA / Testing:** Trần Văn Nguyên (MSSV: 24120205) – Test Plan, Test Cases (≥30), automated pytest unit tests, manual functional testing, and bug tracking

## Core Scope & Key Deliverables
- **Core User Stories (US-01 → US-11):**
  - `US-01 / F-ART-01`: Public article reading with Markdown syntax highlighting
  - `US-02 / F-SEARCH-01`: Search articles by title and filter by tags with pagination (10 articles/page)
  - `US-03 / F-BOOKMARK-01`: Save and manage personal bookmarked articles
  - `US-04 / F-VOTE-01`: Upvote / Downvote articles with public score calculation
  - `US-05 / F-CMT-01`: 2-level nested commenting on articles
  - `US-06 / F-EDITOR-01`: ByteMD Markdown editor with live preview and image upload
  - `US-07 / F-ART-02`: Article lifecycle management (Draft vs. Published states)
  - `US-08 / F-SERIES-01`: Group articles into sequential learning Series
  - `US-09 / F-MOD-01`: Admin moderation to hide/delete violating articles
  - `US-10 / F-TAG-01`: Admin tag catalog management
  - `US-11 / F-AUTH-01`: User registration, JWT login, profile management, and role-based permissions
- **Technology Stack:**
  - **Frontend:** Next.js 16 (React), TailwindCSS, ByteMD, Axios
  - **Backend:** FastAPI (Python 3.11), SQLAlchemy ORM, Alembic, JWT Authentication
  - **Database:** PostgreSQL 15
  - **Infrastructure & Tools:** Docker, Docker Compose, Nginx Reverse Proxy, GitHub Actions, Figma, Postman
- **Key Deliverables:**
  - Software Requirements Specification (SRS) & Use Case specifications
  - System Design Document (ERD, Class Diagram, API Spec)
  - High-fidelity Figma UI mockups
  - Full source code with Docker Compose configuration (GitHub release `v1.0.0`)
  - Test Plan, Test Cases, and pytest execution reports
  - User Guide & Final Presentation Slides (≥15 slides)

## Development Process
- **Methodology:** Scrum-lite (1-week sprints executed within broader course milestone phases)
- **Sprint Duration:** 1 week
- **Issue Tracking:** Jira & Notion (sprint backlog, task assignment, burndown tracking)
- **Source Control:** GitHub (Gitflow workflow: `main` for release, `develop` for integration, `feature/*` for tasks)
- **CI/CD:** GitHub Actions (automated linting, unit test execution, and Docker build validation)
- **Communication:** Discord (daily async updates, ad-hoc tech discussions) & Google Meet (weekly sprint planning, backlog refinement, and demo/retrospective)

## Working Agreements
- Every code change requires a Pull Request (PR) targeting `develop`; no direct pushes to `main` or `develop`.
- At least one peer review and approval is required before any PR can be merged.
- Every task must have clear Acceptance Criteria matching the corresponding User Story requirements before development begins.
- No direct push to main.
- CI pipeline must pass cleanly (all automated tests and build checks green) before merging.
- Database schema changes must include versioned Alembic migration scripts.
- Commit messages must follow Conventional Commits format (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`).
- All members must participate in weekly sprint meetings and promptly communicate blockers on Discord.