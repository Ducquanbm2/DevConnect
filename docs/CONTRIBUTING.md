# Contributing to DevConnect

## Branches

- `main`: mã nguồn ổn định/release; không push trực tiếp.
- `develop`: nhánh tích hợp; mọi PR phát triển đi vào đây.
- `feature/DEV-123-description`: tính năng hoặc task mới.
- `fix/DEV-123-description`: sửa lỗi.
- `chore/DEV-123-description`: công việc kỹ thuật, tooling hoặc tài liệu.

Luôn cập nhật branch trước khi bắt đầu:

```bash
git fetch origin
git switch develop
git pull --ff-only origin develop
git switch -c feature/DEV-123-short-description
```

## Commit

Dùng Conventional Commits và ghi mã Jira:

```text
<type>(DEV-123): <short imperative description>
```

Các type chính: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `ci`.

Ví dụ:

```text
feat(DEV-123): add article draft endpoint
fix(DEV-145): prevent duplicate bookmarks
```

## Pull Request

- PR phải target `develop`, trừ release/hotfix đã được trưởng nhóm thống nhất.
- Liên kết issue Jira và mô tả cách kiểm thử.
- CI phải xanh.
- Cần ít nhất một peer review approval.
- Tác giả không tự merge PR của mình nếu chưa có approval.

## Definition of Done

Một task chỉ được coi là hoàn thành khi:

1. Acceptance Criteria đã được triển khai và kiểm thử.
2. Test liên quan đã được thêm hoặc cập nhật.
3. CI pass, không còn lỗi lint.
4. PR đã được review và merge vào `develop`.
5. Issue Jira được cập nhật trạng thái và ghi chú cần thiết.
