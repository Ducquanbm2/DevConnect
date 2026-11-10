# Kết nối repository local với GitHub

Workspace Codex hiện tại không ghi được vào `.git`, vì vậy hãy chạy các lệnh sau trong thư mục project trên máy local của bạn.

## Trường hợp GitHub repository đang rỗng

Thay URL bên dưới bằng URL SSH hoặc HTTPS của repository vừa tạo:

```bash
cd /path/to/DevConnect
git init -b main
git remote add origin <GITHUB_REPOSITORY_URL>
git add .
git commit -m "chore: bootstrap DevConnect project"
git push -u origin main
git switch -c develop
git push -u origin develop
```

Sau đó vào GitHub bật branch protection cho `main` và `develop` theo [Development Process](DEVELOPMENT_PROCESS.md).

## Trường hợp GitHub repository đã có README hoặc commit đầu tiên

Clone repository trước, chép các file cấu hình/tài liệu này vào thư mục clone, rồi chạy:

```bash
git add .
git commit -m "chore: bootstrap DevConnect project"
git push origin main
git switch -c develop
git push -u origin develop
```

Không dùng `git push --force` để giải quyết khác lịch sử nếu chưa thống nhất với cả nhóm.
