# DevConnect – Checklist Review, Quyền/Token và Phạm vi Agent

## 1. Thông tin task

- [ ] Task/Issue/PR: `______________________________`
- [ ] User Story / requirement: `US-__ / F-____-__`
- [ ] Người thực hiện và module phụ trách: `______________________________`
- [ ] Acceptance Criteria đã được ghi rõ và có thể kiểm chứng.
- [ ] Phạm vi file/thư mục được phép sửa đã được liệt kê.
- [ ] Các file/thư mục ngoài phạm vi đã được liệt kê rõ.
- [ ] Nếu task không chỉ rõ phạm vi hoặc có xung đột tài liệu, đã dừng để hỏi Tech Lead/owner.

## 2. Quy tắc bắt buộc cho agent – chỉ sửa trong phạm vi task

### 2.1. Trước khi sửa

- [ ] Đã đọc `docs/DEVELOPMENT_PROCESS.md`, `docs/ARCHITECTURE.md`, `docs/SYSTEM_DESIGN.md` và tài liệu yêu cầu liên quan.
- [ ] Đã kiểm tra `git status` và ghi nhận thay đổi có sẵn; không ghi đè thay đổi của người dùng.
- [ ] Đã xác định đúng nhánh task từ `develop`, theo quy ước `feature/`, `fix/`, `docs/` hoặc `chore/`.
- [ ] Đã xác định boundary của task: endpoint, service, model, schema, migration, UI và test nào thực sự liên quan.
- [ ] Đã tạo kế hoạch thay đổi ngắn gọn, gắn từng thay đổi với acceptance criteria.

### 2.2. Trong khi sửa

- [ ] Chỉ sửa file nằm trong allowlist của task hoặc file test/tài liệu bắt buộc đi kèm.
- [ ] Không tự ý refactor, đổi tên, format toàn bộ project hoặc sửa module của thành viên khác.
- [ ] Không thay đổi API contract, database schema, role, token strategy hoặc business rule nếu task không yêu cầu.
- [ ] Không sửa `.env`, secret, khóa ký JWT, dữ liệu production hoặc cấu hình triển khai ngoài phạm vi.
- [ ] Nếu phát hiện lỗi ngoài phạm vi, ghi thành finding/issue riêng; không “tiện tay” sửa trong cùng PR.
- [ ] Nếu thay đổi model/schema, đã kiểm tra yêu cầu Alembic migration và ownership của module.
- [ ] Nếu thêm endpoint hoặc business rule, đã thêm test tương ứng trong `backend/tests/`.
- [ ] Business logic và ownership check nằm ở `app/services/`, không nằm trong router hoặc chỉ ở frontend.
- [ ] Router chỉ parse request, gọi service và tạo response; không truy vấn SQLAlchemy trực tiếp.

### 2.3. Trước khi bàn giao

- [ ] `git diff --stat` chỉ chứa file thuộc task.
- [ ] `git diff --check` không có whitespace error hoặc file ngoài ý muốn.
- [ ] Mỗi thay đổi trong diff đều truy vết được tới requirement, bug hoặc test.
- [ ] Không có `.env`, token, password, log nhạy cảm, `node_modules/`, `.venv/`, `__pycache__/`, `.next/` hoặc ảnh test rác trong diff.
- [ ] PR chỉ giải quyết một User Story hoặc một sub-task tập trung.
- [ ] Nếu task phát sinh nhu cầu vượt phạm vi, đã dừng và yêu cầu phê duyệt trước khi tiếp tục.

## 3. Checklist review kiến trúc và API

- [ ] Frontend chỉ gọi REST API; không kết nối trực tiếp PostgreSQL.
- [ ] Backend giữ đúng luồng `endpoint/router → service → model/DB`.
- [ ] Pydantic schema xử lý request/response; không nhận các field nhạy cảm ngoài contract.
- [ ] Endpoint dùng tiền tố `/api/v1/...`.
- [ ] Response thành công dùng envelope `success`, `message` (nếu có), `data`.
- [ ] API danh sách có `page`, `page_size`, `meta`; mặc định 10 và tối đa 50.
- [ ] Response lỗi dùng `success: false` và `error.code/message/details`.
- [ ] Status code phù hợp: `201` tạo mới, `401` chưa xác thực/token sai, `403` thiếu quyền, `404` không tồn tại/không được tiết lộ, `409` trùng dữ liệu, `422` input không hợp lệ.
- [ ] Không dùng việc ẩn nút ở UI làm cơ chế bảo mật duy nhất.
- [ ] Public query luôn lọc đồng thời `PUBLISHED`, `is_hidden = false`, `deleted_at IS NULL`.
- [ ] Thay đổi nhiều bảng có transaction và rollback khi lỗi.
- [ ] Thay đổi schema có migration Alembic được review cùng PR.

## 4. Ma trận quyền cần kiểm thử

| Tác vụ | Guest | User/Author | Owner | Admin | Kết quả ngoài quyền |
|---|:---:|:---:|:---:|:---:|---|
| Health, register, login | Có | Có | Có | Có | – |
| Đọc/search/filter bài công khai | Có | Có | Có | Có | Draft/hidden/deleted không được lộ |
| `GET /users/me`, cập nhật profile | Không | Có | Có | Có | Guest: `401` |
| Tạo bài, upload ảnh, tạo Series | Không | Có | Có | Có | Guest: `401` |
| Sửa/xóa/chuyển trạng thái bài | Không | Không | Có | Theo chính sách owner/admin đã chốt | User khác: `403`; bài riêng tư của người khác: `404` |
| Đọc Draft | Không | Không | Có | Theo chính sách đã chốt | Không phải owner: `404` |
| Sửa/xóa Series | Không | Không | Có | Theo chính sách đã chốt | User khác: `403` |
| Bình luận, vote, bookmark | Không | Có | Có | Có | Guest: `401` |
| Xóa comment | Không | Chỉ comment của mình | Chỉ comment của mình | Có nếu contract cho phép | User khác: `403` |
| Hide/unhide/delete bài | Không | Không | Không | Có | User thường: `403` |
| Tạo/sửa/xóa Tag quản trị | Không | Không | Không | Có | User thường: `403` |

> Với mỗi endpoint bảo vệ, kiểm thử tối thiểu bằng bốn context: không token, User A, User B, Admin. Với endpoint owner, User A là owner và User B là non-owner của cùng một resource.

## 5. Checklist kiểm thử JWT và token

### 5.1. Token hợp lệ và vòng đời

- [ ] Login thành công trả JWT đúng `token_type` và có `exp`/thời hạn.
- [ ] Password được hash bằng cơ chế phù hợp; không lưu hoặc log plaintext.
- [ ] Token hợp lệ gọi được endpoint đúng role.
- [ ] Không có header `Authorization` → `401`.
- [ ] Sai scheme, ví dụ không phải `Bearer <token>` → `401`.
- [ ] Token rỗng, sai định dạng, thiếu claim bắt buộc hoặc không decode được → `401`.
- [ ] Token hết hạn (`exp` trong quá khứ) → `401`.
- [ ] Token có chữ ký sai → `401`; không chấp nhận việc sửa payload rồi dùng lại token.
- [ ] Token ký bằng thuật toán không nằm trong allowlist → `401`; không chấp nhận `alg=none`.
- [ ] Token của User bị thu hồi/hết hiệu lực theo chính sách phiên → bị từ chối.
- [ ] Token không được ghi vào log, response lỗi, request ID hoặc telemetry.

### 5.2. Không leo thang quyền

- [ ] Field `role=ADMIN` trong register bị bỏ qua hoặc từ chối; user mới luôn là `USER`.
- [ ] Field `role` trong update profile không thể đổi role.
- [ ] Sửa claim `sub` hoặc `role` bằng tay làm chữ ký không hợp lệ và bị từ chối.
- [ ] Quyền admin được xác định từ identity/role hợp lệ ở backend; không tin role do frontend gửi.
- [ ] Nếu role thay đổi sau khi phát hành token, hành vi token cũ đã được quy định và có test.
- [ ] User thường gọi mọi endpoint `/api/v1/admin/*` đều nhận `403`.
- [ ] Không thể dùng token của User A để đọc/sửa/xóa dữ liệu riêng của User B.
- [ ] Không thể thay `id`, `slug`, `author_id`, `user_id` trong request để vượt ownership.

### 5.3. Bảng test nhanh theo endpoint

| Nhóm endpoint | Không token | Token User | Token Owner | Token Admin |
|---|---|---|---|---|
| `/auth/register`, `/auth/login` | `2xx` hoặc `409/422` theo input | như guest | như guest | như guest |
| `/users/me`, `/me/*` | `401` | `2xx` và chỉ dữ liệu của mình | `2xx` | `2xx` |
| Article/Series owner | `401` | non-owner: `403`/`404` | `2xx` | theo policy đã chốt |
| Public article/search/tag/series | `2xx` nhưng chỉ dữ liệu công khai | cùng dữ liệu công khai | cùng dữ liệu công khai | cùng dữ liệu công khai |
| Vote/comment/bookmark | `401` | `2xx`, không trùng dữ liệu | `2xx` | `2xx` |
| Admin moderation/tag | `401` | `403` | `403` nếu không có role Admin | `2xx` |

## 6. Checklist theo BR-01 đến BR-10

- [ ] **BR-01:** register mặc định `USER`; không có đường đi công khai để tự cấp `ADMIN`.
- [ ] **BR-02:** chỉ owner sửa/xóa/đổi `DRAFT ↔ PUBLISHED`; non-owner bị chặn ở backend.
- [ ] **BR-03:** Draft chỉ owner xem; không xuất hiện home, search, tag hoặc profile công khai.
- [ ] **BR-04:** bài có 0, 5 và 6 tag; 6 tag bị từ chối và transaction không lưu dở dang.
- [ ] **BR-05:** cùng user/article không tạo vote hoặc bookmark trùng; có test đổi/hủy vote và unique constraint.
- [ ] **BR-06:** tạo comment gốc và reply cấp 2 thành công; reply vào reply bị chặn hoặc quy về root theo policy.
- [ ] **BR-07:** mọi API public loại bài Draft, hidden và deleted trong từng tổ hợp trạng thái.
- [ ] **BR-08:** Series chỉ chứa bài Published thuộc owner của Series; kiểm thử bài khác tác giả và bài Draft.
- [ ] **BR-09:** điểm bằng `upvote_count - downvote_count` sau tạo, đổi và hủy vote.
- [ ] **BR-10:** tên Tag được trim, so sánh không phân biệt hoa thường; duplicate trả `409` hoặc lỗi contract tương ứng.

## 7. Checklist theo NFR bảo mật và chất lượng

- [ ] **NFR-03:** không có plaintext password trong DB, log, exception hoặc test fixture commit vào repo.
- [ ] **NFR-04:** mọi endpoint bảo vệ kiểm tra JWT, role và ownership ở backend.
- [ ] **NFR-05:** Markdown/HTML được sanitize; upload chỉ PNG/JPEG/WebP, tối đa 5 MB, kiểm tra MIME và nội dung file, tên lưu trữ được sinh tự động.
- [ ] **NFR-06:** foreign key, unique constraint, transaction và rollback được kiểm chứng.
- [ ] **NFR-07:** `docker compose up` chạy được; health check phản ánh backend/database; volume giữ dữ liệu và `/uploads`.
- [ ] **NFR-10:** route/schema/service/model tách lớp; lint, pytest và peer review đạt; tổng test bao phủ US-01 đến US-11 và tối thiểu 30 test case theo kế hoạch.
- [ ] **NFR-11:** log có thời gian, method, path, status, request ID; log moderation có actor/object/result; không log token/password/nội dung nhạy cảm.
- [ ] **NFR-12:** có backup PostgreSQL và `/uploads`; đã thử restore và xác nhận bài viết/ảnh còn truy cập được.

## 8. Kiểm thử hồi quy và tiêu chí merge

- [ ] Backend: `ruff check .` pass.
- [ ] Backend: `pytest -v` pass; test mới có tên rõ và kiểm tra cả success/failure/permission.
- [ ] Frontend: `npm run lint`, `npm run typecheck` và `npm run build` pass khi task chạm frontend.
- [ ] API contract/Postman collection được cập nhật nếu endpoint hoặc response thay đổi.
- [ ] Manual smoke test trên Chrome và Firefox cho luồng bị ảnh hưởng.
- [ ] Không còn lỗi mức Critical/High liên quan auth, quyền, ownership, token hoặc lộ dữ liệu.
- [ ] CI GitHub Actions xanh hoàn toàn.
- [ ] PR có ít nhất một approval từ Tech Lead hoặc thành viên liên quan; tác giả không tự merge.
- [ ] Migration đã chạy thử upgrade và rollback/restore theo khả năng của task.
- [ ] Reviewer đã ghi rõ: phạm vi đã kiểm tra, test đã chạy, rủi ro còn lại và issue ngoài phạm vi.

## 9. Biên bản kết quả

| Hạng mục | Kết quả | Bằng chứng / link |
|---|---|---|
| Scope audit | PASS / FAIL | |
| JWT/token tests | PASS / FAIL | |
| Permission/ownership tests | PASS / FAIL | |
| BR-01 → BR-10 | PASS / FAIL / N/A | |
| NFR liên quan | PASS / FAIL / N/A | |
| Unit/API/integration tests | PASS / FAIL | |
| Lint/typecheck/build/CI | PASS / FAIL / N/A | |
| Security findings | None / Open | |
| Quyết định | APPROVE / REQUEST CHANGES / BLOCK | |

### Quy tắc dừng

Nếu phát hiện token có thể giả mạo, endpoint bảo vệ thiếu kiểm tra backend, lộ Draft/dữ liệu người khác, user thường gọi được Admin API, hoặc diff vượt phạm vi đã phê duyệt: **BLOCK merge**, ghi finding tái hiện được và chuyển cho Tech Lead/owner. Không tự mở rộng task để xử lý các thay đổi lớn khi chưa có phê duyệt.
