# Quy trình Phát triển & Bộ Quy tắc Bắt buộc (Team Rules) – DevConnect

> **Tài liệu này là hiến pháp kỹ thuật của dự án DevConnect.**
> Mọi thành viên trong nhóm (**Quân, Trường, Việt, Nguyên**) và các công cụ hỗ trợ lập trình (AI Coding Assistants) **BẮT BUỘC** phải tuân thủ 100% các quy định dưới đây. Mọi Pull Request vi phạm quy tắc sẽ bị từ chối merge.

---

## 1. Phân công Trách nhiệm & Phạm vi Module

Không ai tự ý sửa code nằm ngoài module được giao nếu chưa trao đổi với người phụ trách và Technical Lead.

| Thành viên | MSSV | Vai trò | Phạm vi phụ trách chính (Modules & User Stories) |
|:---|:---:|:---|:---|
| **Nguyễn Đức Quân** | 24120218 | **Project Lead / Tech Lead** | • Kiến trúc hệ thống, Docker Compose, CI/CD, Database Schema & Migration<br>• Module `auth` & `users` (**US-11 / F-AUTH-01**)<br>• Review & Merge toàn bộ Pull Request vào `develop` và `main` |
| **Trần Nhật Trường** | 24120486 | **Backend Developer** | • Module `articles` CRUD & Draft/Published lifecycle (**US-01, US-07**)<br>• Module `series` (**US-08**), `tags` (**US-10**), `search` (**US-02**)<br>• Module `admin` kiểm duyệt bài viết (**US-09**) & API Upload ảnh (**US-06**) |
| **Trần Lê Đức Việt** | 24120245 | **Frontend Developer** | • UI/UX (Figma), Layout chung, Design System (TailwindCSS)<br>• Trang chủ, Đọc bài viết, Tìm kiếm/Lọc Tag (**US-01, US-02**)<br>• Trình soạn thảo Markdown ByteMD (**US-06**), Quản lý bài & Series UI (**US-07, US-08**) |
| **Trần Văn Nguyên** | 24120205 | **Fullstack Developer & QA** | • Backend + Frontend cho `comments` 2 cấp (**US-05**), `votes` (**US-04**), `bookmarks` (**US-03**)<br>• Lập Test Plan, viết $\ge$ 30 Test Cases, viết Unit Test (`pytest`) và kiểm thử tích hợp |

---

## 2. Quy trình Quản lý Mã nguồn (Git Workflow)

### 2.1. Chiến lược Phân nhánh (Gitflow rút gọn)
* **`main`**: Nhánh sản phẩm ổn định (Production/Release). **TUYỆT ĐỐI KHÔNG** push trực tiếp. Chỉ nhận merge từ `develop` khi kết thúc Milestone/Sprint.
* **`develop`**: Nhánh tích hợp chính của nhóm. Mọi tính năng mới đều phải tách nhánh từ `develop` và tạo Pull Request (PR) quay về `develop`.
* **Nhánh công việc (Working Branches)**: Phải đặt tên theo đúng cú pháp:
  * Tính năng mới: `feature/US-xx-<mo-ta-ngan>` hoặc `feature/DEV-xx-<mo-ta-ngan>` (VD: `feature/US-11-jwt-auth`, `feature/US-07-article-crud`)
  * Sửa lỗi: `fix/US-xx-<mo-ta-loi>` (VD: `fix/US-04-duplicate-vote`)
  * Cấu hình / Tài liệu / Refactor: `chore/DEV-xx-<mo-ta>` hoặc `docs/DEV-xx-<mo-ta>`

### 2.2. Quy trình 5 bước mỗi khi bắt đầu làm 1 Task
```bash
# Bước 1: Luôn lấy code mới nhất từ develop về máy
git fetch origin
git switch develop
git pull --ff-only origin develop

# Bước 2: Tạo nhánh riêng cho task của mình
git switch -c feature/US-07-article-lifecycle

# Bước 3: Code, chạy thử nghiệm và kiểm tra lint/test ở local
# Bước 4: Commit theo chuẩn Conventional Commits (xem mục 2.3)
# Bước 5: Push nhánh lên GitHub và tạo Pull Request vào nhánh `develop`
git push -u origin feature/US-07-article-lifecycle
```

### 2.3. Quy chuẩn Commit Message (Conventional Commits)
Mọi commit message **BẮT BUỘC** tuân theo định dạng:
```text
<type>(<scope/ticket>): <mô tả ngắn gọn bằng tiếng Anh hoặc tiếng Việt không dấu, viết thường đầu câu>
```
* **`<type>` hợp lệ**:
  * `feat`: Thêm tính năng mới
  * `fix`: Sửa bug
  * `docs`: Thêm/sửa tài liệu
  * `refactor`: Tái cấu trúc code (không đổi logic nghiệp vụ)
  * `test`: Thêm hoặc sửa unit test / integration test
  * `chore`: Thay đổi cấu hình build, docker, thư viện
* **Ví dụ ĐÚNG**:
  * `feat(US-11): implement jwt login and register endpoints`
  * `fix(US-05): restrict nested comment depth to 2 levels`
  * `docs(design): add mermaid ERD and sequence diagrams`
* **Ví dụ SAI (CẤM DÙNG)**:
  * `update code`, `fix bug`, `done`, `asdf`, `commit lần 1`

### 2.4. Quy tắc Pull Request (PR) & Code Review
1. **PR nhỏ và tập trung**: Mỗi PR chỉ giải quyết 1 User Story hoặc 1 sub-task cụ thể (không gộp cả Frontend lẫn Backend của 3 chức năng khác nhau vào 1 PR khổng lồ).
2. **Không tự merge**: Tác giả PR **không được tự bấm Merge** khi chưa có ít nhất **1 lượt Approve** từ Tech Lead (Quân) hoặc thành viên liên quan.
3. **CI phải Xanh**: Mọi bước kiểm tra tự động (lint, typecheck, pytest) trên GitHub Actions phải Pass 100% trước khi merge.
4. **Không commit rác**: Tuyệt đối không commit file `.env`, thư mục `node_modules/`, `.venv/`, `__pycache__/`, `.next/`, hoặc file ảnh test rác vào Git.

---

## 3. Quy tắc Kiến trúc & Coding Standards

### 3.1. Nguyên tắc Kiến trúc 3 tầng (Strict 3-Tier Separation)
1. **Frontend (`frontend/`)**: Chỉ làm nhiệm vụ hiển thị giao diện (Presentation), quản lý state phía client và gọi HTTP REST API tới Backend.
   * **CẤM** kết nối trực tiếp tới PostgreSQL từ Next.js.
   * **CẤM** chỉ kiểm tra quyền ở giao diện (ẩn nút bấm) mà bỏ qua kiểm tra ở Backend.
2. **Backend (`backend/`)**: Tuân thủ nghiêm ngặt kiến trúc phân lớp (**Router $\rightarrow$ Service $\rightarrow$ Model/DB**):
   * **`app/api/v1/endpoints/` (Router/Controller)**: Chỉ nhận HTTP Request, parse Pydantic Schema, gọi `Service` và trả về HTTP Response. **CẤM** viết câu lệnh truy vấn SQLAlchemy (`db.query`, `db.execute`) trực tiếp trong file router.
   * **`app/services/` (Business Logic)**: Chứa toàn bộ quy tắc nghiệp vụ (`BR-01` $\rightarrow$ `BR-10`), kiểm tra quyền sở hữu (Ownership), xử lý transaction.
   * **`app/models/` (Data Layer)**: Định nghĩa bảng SQLAlchemy ORM và các ràng buộc cơ sở dữ liệu (`ForeignKey`, `UniqueConstraint`, `Index`).
   * **`app/schemas/` (DTO / Validation)**: Định nghĩa Pydantic v2 models cho Request Body, Query Params và Response Payload.

### 3.2. Chuẩn Giao tiếp API (API Contract)
Mọi REST API phải đặt dưới tiền tố `/api/v1/...` và tuân thủ chuẩn JSON:

1. **Response Thành công (Single Object / Action)**:
   ```json
   {
     "success": true,
     "message": "Thao tác thành công",
     "data": { ... }
   }
   ```
2. **Response Danh sách có Phân trang (Pagination - NFR-02)**:
   * Mặc định `page = 1`, `page_size = 10` (tối đa `page_size = 50`).
   ```json
   {
     "success": true,
     "data": [ ... ],
     "meta": {
       "page": 1,
       "page_size": 10,
       "total_items": 42,
       "total_pages": 5
     }
   }
   ```
3. **Response Lỗi (Error Format thống nhất)**:
   ```json
   {
     "success": false,
     "error": {
       "code": "ARTICLE_NOT_FOUND",
       "message": "Không tìm thấy bài viết hoặc bài viết đã bị ẩn.",
       "details": null
     }
   }
   ```
4. **Sử dụng đúng HTTP Status Code**:
   * `200 OK`: Lấy dữ liệu, cập nhật hoặc xóa thành công.
   * `201 Created`: Tạo mới tài nguyên thành công (Register, Tạo bài, Tạo comment...).
   * `400 Bad Request` / `422 Unprocessable Entity`: Dữ liệu đầu vào sai định dạng hoặc vi phạm quy tắc nghiệp vụ.
   * `401 Unauthorized`: Chưa đăng nhập hoặc JWT token hết hạn/không hợp lệ.
   * `403 Forbidden`: Đã đăng nhập nhưng không đủ quyền (VD: User thường gọi API Admin, hoặc sửa bài viết của người khác).
   * `404 Not Found`: Tài nguyên không tồn tại (hoặc khách truy cập bài `DRAFT` / `HIDDEN`).
   * `409 Conflict`: Trùng lặp dữ liệu (Email đã tồn tại, Tên Tag bị trùng).

---

## 4. Mười Quy tắc Nghiệp vụ & Bảo mật Bất khả xâm phạm (BR-01 $\rightarrow$ BR-10)

Mọi thành viên khi code Backend và Frontend phải đảm bảo 10 quy tắc sau:

1. **BR-01 (Phân quyền Role)**: Tài khoản đăng ký mới mặc định có `role = "USER"`. Quyền `"ADMIN"` chỉ được gán qua seed database hoặc cấu hình quản trị, tuyệt đối không cho phép truyền `role` trong API đăng ký/cập nhật profile.
2. **BR-02 (Quyền sở hữu - Ownership)**: Chỉ tác giả sở hữu bài viết (`author_id == current_user.id`) mới được phép chỉnh sửa, xóa hoặc đổi trạng thái `DRAFT` $\leftrightarrow$ `PUBLISHED` cho bài viết của mình.
3. **BR-03 (Bảo mật bản nháp)**: Bài viết ở trạng thái `DRAFT` chỉ hiển thị cho chính tác giả đó. Không bao giờ xuất hiện ở trang chủ, tìm kiếm, danh sách tag hay trang cá nhân công khai.
4. **BR-04 (Giới hạn Tag)**: Mỗi bài viết chỉ được gắn tối đa **5 Tags**.
5. **BR-05 (Chống trùng Vote & Bookmark)**: Mỗi người dùng chỉ có tối đa **1 Vote** (`+1` hoặc `-1`) và **1 Bookmark** trên 1 bài viết. Bắt buộc phải có `UniqueConstraint(user_id, article_id)` trong PostgreSQL.
6. **BR-06 (Bình luận tối đa 2 cấp)**: Bình luận chỉ gồm Bình luận gốc (`parent_id = NULL`) và Câu trả lời (`parent_id` trỏ tới bình luận gốc). Nếu người dùng cố tình reply vào một bình luận cấp 2, Backend phải chặn lại (`400 Bad Request`) hoặc tự động quy về bình luận gốc.
7. **BR-07 (Điều kiện hiển thị công khai)**: Các API công khai chỉ trả về bài viết thỏa mãn đồng thời: `status == 'PUBLISHED'` VÀ `is_hidden == False` VÀ `deleted_at IS NULL`.
8. **BR-08 (Quy tắc Series)**: Series chỉ được chứa các bài viết đã `PUBLISHED` của chính tác giả tạo Series đó.
9. **BR-09 (Tính điểm Vote)**: Điểm của bài viết (`vote_score`) = Tổng số Upvote (`+1`) trừ đi Tổng số Downvote (`-1`).
10. **BR-10 (Chuẩn hóa Tag)**: Tên Tag phải được `trim()` khoảng trắng thừa và kiểm tra không trùng lặp theo kiểu không phân biệt hoa thường (`case-insensitive`).

---

## 5. Quy tắc Cơ sở dữ liệu & Alembic Migration

1. **CẤM sửa bảng thủ công bằng pgAdmin/DBeaver** mà không tạo file migration.
2. Mọi thay đổi trong `backend/app/models/` phải đi kèm lệnh tạo Alembic migration:
   ```bash
   alembic revision --autogenerate -m "mo_ta_thay_doi"
   alembic upgrade head
   ```
3. File migration sinh ra phải được kiểm tra kỹ và commit chung vào Pull Request với model.

---

## 6. Định nghĩa Hoàn thành (Definition of Done - DoD)

Một tính năng (User Story) chỉ được chuyển sang cột **DONE** khi thỏa mãn đủ 6 tiêu chí:
- [ ] Code tuân thủ đúng kiến trúc phân tầng và naming convention.
- [ ] Đã xử lý đầy đủ cả kịch bản chính (Happy P  ath) và các kịch bản lỗi (Edge Cases / Alternate Flows) như trong báo cáo Phân tích yêu cầu.
- [ ] Đã viết Unit Test / API Test trong `backend/tests/` và chạy `pytest` xanh 100%.
- [ ] Giao diện Frontend tương thích responsive (Desktop & Mobile) và xử lý thông báo lỗi rõ ràng.
- [ ] Đã tạo Pull Request, vượt qua CI và được review/approve.
- [ ] Chạy thử nghiệm mượt mà trên `docker compose up`.
