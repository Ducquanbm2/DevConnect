# AGENTS.md – DevConnect Project Guidelines

This file defines mandatory rules for all AI coding assistants (Antigravity, Cursor, Codex, Claude Code, GitHub Copilot) and contributors working in this repository.

- Always read `docs/DEVELOPMENT_PROCESS.md`, `docs/ARCHITECTURE.md`, and `docs/SYSTEM_DESIGN.md` before modifying or creating new modules.
- Follow the strict 3-tier architecture (`Next.js 16` -> `FastAPI REST API` -> `PostgreSQL 15`).
- In `backend/`, strictly separate `api/v1/endpoints` (HTTP layer), `services` (business logic & ownership checks), `models` (SQLAlchemy 2.0 ORM), and `schemas` (Pydantic v2).
- Enforce all 10 Business Rules (`BR-01` to `BR-10`) and Non-Functional Requirements (`NFR-01` to `NFR-12`) defined in `docs/DevConnect-AnalysisReport.md`.
- Every new endpoint or business rule must include corresponding `pytest` tests in `backend/tests/`.
