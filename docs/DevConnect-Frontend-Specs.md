# DEVCONNECT FRONTEND SPECIFICATIONS

## Đặc tả giao diện và prototype trên Figma

**Sản phẩm:** DevConnect - Nền tảng chia sẻ kiến thức công nghệ và bài viết kỹ thuật  
**Phiên bản đặc tả:** 1.0  
**Ngày cập nhật:** 08/11/2026  
**Nền tảng triển khai:** Next.js 16, React, TypeScript, TailwindCSS, ByteMD  
**Kích thước thiết kế bắt buộc:** 1440 px, 768 px và 375 px

---

## 1. Mục tiêu tài liệu

Tài liệu này là blueprint để thiết kế giao diện DevConnect trên Figma và bàn giao cho frontend. Thiết kế phải bao phủ đúng 11 User Story của Project Proposal, thể hiện đầy đủ trạng thái mặc định, tải dữ liệu, rỗng, lỗi, thành công và không đủ quyền.

Phạm vi giao diện gồm:

- Đăng ký, đăng nhập, đăng xuất và cập nhật hồ sơ.
- Đọc bài Published, tìm kiếm theo tiêu đề và lọc theo Tag.
- Soạn thảo Markdown, live preview, upload ảnh, lưu Draft và xuất bản.
- Quản lý bài viết và Series của tác giả.
- Bình luận hai cấp, vote và bookmark.
- Admin kiểm duyệt bài viết và quản lý Tag.

Không thiết kế cho chat, thông báo đẩy, theo dõi người dùng, thanh toán, gợi ý AI, ứng dụng mobile native, cộng tác nhiều tác giả hoặc quản lý tài khoản bởi Admin.

## 2. Định hướng trải nghiệm

DevConnect cần tạo cảm giác của một sản phẩm tri thức kỹ thuật: sáng, rõ ràng, tin cậy, nhiều khoảng trắng và ưu tiên khả năng đọc nội dung dài. Giao diện dùng nền trắng làm chủ đạo, xanh tươi làm điểm nhấn cho hành động và điều hướng; navy chỉ xuất hiện ở chữ quan trọng, code block và một số vùng phụ. Giao diện không mô phỏng mạng xã hội có feed dày đặc; trọng tâm là bài viết, mã nguồn, lộ trình Series và công cụ viết.

Các nguyên tắc thiết kế:

1. **Content first:** nội dung bài viết và mã nguồn luôn có độ tương phản, chiều rộng và khoảng cách dễ đọc.
2. **Action clarity:** mỗi màn hình có một hành động chính nổi bật; hành động nguy hiểm luôn cần xác nhận.
3. **Progressive disclosure:** tùy chọn nâng cao chỉ xuất hiện khi người dùng cần, đặc biệt trong editor và Admin Panel.
4. **State visibility:** Draft, Published và Hidden phải có màu, nhãn và mô tả rõ; không chỉ phân biệt bằng màu.
5. **Ownership visibility:** nút Sửa, Xóa, Xuất bản và quản lý Series chỉ xuất hiện khi người dùng có quyền phù hợp.
6. **Responsive by design:** thiết kế mobile là bố cục thích nghi, không phải bản desktop bị thu nhỏ.
7. **Accessible interaction:** thao tác chính dùng được bằng bàn phím; focus, lỗi và trạng thái được thể hiện rõ ràng.

## 3. Cấu trúc file Figma

Tạo một file Figma tên `DevConnect UI UX` với các Page sau:

| Page | Nội dung |
|:---|:---|
| `00 Cover` | Tên dự án, phiên bản, thành viên, liên kết prototype và trạng thái thiết kế. |
| `01 Foundations` | Color styles, typography, spacing, grid, radius, shadow, icon và quy tắc responsive. |
| `02 Components` | Component, variants, trạng thái và tài liệu sử dụng. |
| `03 Public` | Trang chủ, tìm kiếm, chi tiết bài, Series và hồ sơ công khai. |
| `04 Authentication` | Đăng nhập, đăng ký và các trạng thái xác thực. |
| `05 Member` | Hồ sơ cá nhân, bookmark, bình luận và vote. |
| `06 Author` | Dashboard bài viết, editor và quản lý Series. |
| `07 Admin` | Kiểm duyệt bài viết và quản lý Tag. |
| `08 Responsive` | Các frame tablet 768 px và mobile 375 px. |
| `09 Prototype Flows` | Các flow prototype hoàn chỉnh theo User Story. |
| `10 Handoff` | Screen map, annotation, token mapping, content mẫu và checklist bàn giao. |

Quy ước đặt tên frame:

```text
[Kích thước]/[Khu vực]/[Màn hình]/[Trạng thái]

Desktop/Public/Home/Default
Desktop/Public/Search/Empty
Desktop/Author/Editor/ValidationError
Mobile/Member/Article/Authenticated
Desktop/Admin/ArticleModeration/ConfirmHide
```

Quy ước component:

```text
Button/Primary/Medium/Default
Input/Text/Default/Focus
ArticleCard/Horizontal/Default
StatusBadge/Article/Draft
Dialog/Destructive/DeleteArticle
```

Mọi frame chính dùng Auto Layout. Component dùng variant properties thay vì tạo nhiều component rời có cùng cấu trúc.

## 4. Design system

### 4.1. Màu sắc

#### Màu thương hiệu white-first

| Token | Giá trị | Công dụng |
|:---|:---:|:---|
| `surface.white` | `#FFFFFF` | Nền chính của page, card và form. |
| `surface.canvas` | `#F7FBFE` | Nền tổng thể rất nhạt, tạo tách lớp nhẹ giữa page và card. |
| `brand.navy.950` | `#0B1F3A` | Footer, code theme và tiêu đề có độ tương phản cao; không dùng làm nền chính. |
| `brand.navy.900` | `#0F2948` | Body text chính, heading và icon quan trọng. |
| `brand.blue.700` | `#0878B5` | Link, button chữ nhỏ và trạng thái hover có yêu cầu tương phản cao. |
| `brand.blue.600` | `#0B8ACB` | Primary button, focus và hành động chính trên nền trắng. |
| `brand.blue.500` | `#19A8E8` | Điểm nhấn tươi, icon, illustration và gradient nhẹ; không dùng cho text nhỏ trên nền trắng. |
| `brand.blue.100` | `#E5F6FD` | Nền selected, chip nhẹ, banner thông tin. |
| `brand.blue.50` | `#F1FAFE` | Nền section phụ và hover nhẹ. |

#### Màu trung tính

| Token | Giá trị | Công dụng |
|:---|:---:|:---|
| `neutral.950` | `#102033` | Body text chính khi cần độ tương phản cao. |
| `neutral.700` | `#374151` | Text phụ cấp cao. |
| `neutral.500` | `#64748B` | Metadata, placeholder. |
| `neutral.300` | `#CBD5E1` | Border và divider. |
| `neutral.200` | `#E2E8F0` | Border nhẹ, skeleton. |
| `neutral.100` | `#F1F7FA` | Nền component phụ. |
| `neutral.50` | `#F8FCFE` | Nền input và vùng phụ rất nhạt. |

#### Màu ngữ nghĩa

| Token | Giá trị | Công dụng |
|:---|:---:|:---|
| `success.600` | `#16835B` | Published, thành công. |
| `success.100` | `#DCFCE7` | Nền success badge. |
| `warning.700` | `#C66715` | Draft, cảnh báo. |
| `warning.100` | `#FEF3C7` | Nền warning badge. |
| `danger.700` | `#B73737` | Xóa, lỗi, Hidden. |
| `danger.100` | `#FEE2E2` | Nền lỗi và badge nguy hiểm. |
| `info.600` | `#0369A1` | Thông tin và trạng thái trung gian. |

Không dùng màu làm tín hiệu duy nhất. Mỗi trạng thái phải có text hoặc icon đi kèm.

### 4.2. Quy tắc áp dụng white-first

- Tối thiểu 70% diện tích mỗi màn hình là trắng hoặc `surface.canvas`.
- Header desktop dùng nền trắng, logo xanh và border dưới nhẹ; không dùng header navy toàn chiều rộng.
- Primary button dùng `brand.blue.600`; chữ trắng, không dùng xanh tươi quá sáng cho chữ nhỏ.
- Card dùng nền trắng, border `neutral.300` và shadow rất nhẹ; không tô nền xanh cho toàn bộ card.
- Tag dùng nền `brand.blue.100` và chữ `brand.blue.700`.
- Hero dùng nền trắng hoặc gradient rất nhẹ từ trắng sang `brand.blue.50`; chỉ có một vùng xanh làm điểm nhấn.
- Navy chỉ dùng cho heading, chữ quan trọng, code block, footer và sidebar Admin khi cần phân biệt khu vực.
- Khi cần trạng thái selected, ưu tiên nền xanh nhạt + border xanh thay vì nền xanh đậm toàn khối.

### 4.3. Typography

Sử dụng `Inter` cho UI và nội dung; sử dụng `JetBrains Mono` cho mã nguồn và nội dung Markdown dạng code.

| Style | Font | Size / Line height | Weight | Công dụng |
|:---|:---|:---:|:---:|:---|
| `Display/L` | Inter | 48 / 56 | 700 | Hero desktop. |
| `Heading/H1` | Inter | 36 / 44 | 700 | Tiêu đề trang. |
| `Heading/H2` | Inter | 28 / 36 | 700 | Tiêu đề section. |
| `Heading/H3` | Inter | 22 / 30 | 650 | Tiêu đề card/khối. |
| `Heading/H4` | Inter | 18 / 26 | 650 | Tiêu đề nhỏ. |
| `Body/L` | Inter | 18 / 30 | 400 | Nội dung bài viết. |
| `Body/M` | Inter | 16 / 24 | 400 | UI body mặc định. |
| `Body/S` | Inter | 14 / 20 | 400 | Metadata và helper text. |
| `Label/M` | Inter | 14 / 20 | 600 | Button, label và table header. |
| `Label/S` | Inter | 12 / 16 | 600 | Badge và caption. |
| `Code/M` | JetBrains Mono | 14 / 22 | 400 | Code block. |

Nội dung bài viết desktop có chiều rộng tối đa 760 px. Không để dòng nội dung chính dài hơn khoảng 80 ký tự ở cỡ chữ 18 px.

### 4.4. Spacing, radius và shadow

- Spacing base: `4 px`.
- Dãy spacing: `4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80`.
- Khoảng cách mặc định giữa label và input: `8 px`.
- Khoảng cách giữa các field: `20 px`.
- Khoảng cách giữa section lớn: `48–64 px`.
- Radius button/input: `8 px`.
- Radius card: `12 px`.
- Radius modal: `16 px`.
- Pill/chip: `999 px`.
- Shadow card: `0 1px 3px rgba(15, 41, 72, 0.10)`.
- Shadow dropdown: `0 12px 30px rgba(15, 41, 72, 0.16)`.
- Focus ring: `0 0 0 3px rgba(22, 137, 216, 0.28)`.

### 4.5. Icon

Sử dụng một bộ icon thống nhất, ưu tiên Lucide Icons. Kích thước chuẩn là 16, 20 và 24 px; stroke 1.75–2 px. Icon không thay thế hoàn toàn text đối với hành động quan trọng như Xuất bản, Xóa hoặc Ẩn bài.

## 5. Grid và responsive

| Breakpoint thiết kế | Frame | Grid | Margin | Gutter | Container |
|:---|:---:|:---:|:---:|:---:|:---:|
| Desktop | 1440 px | 12 cột | 80 px | 24 px | 1280 px |
| Tablet | 768 px | 8 cột | 32 px | 20 px | 704 px |
| Mobile | 375 px | 4 cột | 16 px | 16 px | 343 px |

Quy tắc responsive:

- Header desktop chuyển thành top bar có menu sheet ở dưới 768 px.
- Sidebar dashboard/admin chuyển thành drawer trên tablet và mobile.
- Card bài viết horizontal chuyển sang vertical dưới 768 px.
- Editor desktop chia đôi 50/50; tablet có tab `Viết` và `Xem trước`; mobile chỉ hiển thị một tab tại một thời điểm.
- Table nhiều cột chuyển thành card list trên mobile, không thu nhỏ chữ để ép vừa màn hình.
- Code block có scroll ngang riêng, không làm trang tràn ngang.
- Modal desktop rộng 480–640 px; mobile dùng bottom sheet hoặc modal cách mép 16 px.
- Primary action quan trọng trên mobile có thể sticky ở cuối màn hình nếu không che nội dung.

## 6. Kiến trúc thông tin và route

### 6.1. Khu vực công khai

| Route | Màn hình | Quyền truy cập |
|:---|:---|:---|
| `/` | Trang chủ | Công khai |
| `/search?q=&tag=&page=` | Kết quả tìm kiếm và lọc | Công khai |
| `/articles/[slug]` | Chi tiết bài Published | Công khai |
| `/series/[slug]` | Chi tiết Series | Công khai |
| `/tags/[slug]` | Danh sách bài theo Tag | Công khai |
| `/users/[username]` | Hồ sơ công khai của tác giả | Công khai |
| `/login` | Đăng nhập | Khách |
| `/register` | Đăng ký | Khách |

### 6.2. Khu vực thành viên và tác giả

| Route | Màn hình | Quyền truy cập |
|:---|:---|:---|
| `/me` | Hồ sơ cá nhân | Đã đăng nhập |
| `/me/bookmarks` | Bài đã lưu | Đã đăng nhập |
| `/dashboard/articles` | Quản lý bài viết | Tác giả |
| `/editor/new` | Tạo bài mới | Tác giả |
| `/editor/[id]` | Chỉnh sửa bài sở hữu | Chủ sở hữu |
| `/dashboard/series` | Danh sách Series | Tác giả |
| `/dashboard/series/[id]` | Chỉnh sửa và sắp xếp Series | Chủ sở hữu |

### 6.3. Khu vực quản trị

| Route | Màn hình | Quyền truy cập |
|:---|:---|:---|
| `/admin/articles` | Kiểm duyệt bài viết | Admin |
| `/admin/tags` | Quản lý Tag | Admin |

Khi người dùng chưa đăng nhập thực hiện vote, bookmark hoặc bình luận, điều hướng tới `/login?next=<current-url>`. Sau đăng nhập thành công phải quay lại đúng trang trước đó.

## 7. Global navigation

### 7.1. Header desktop

- Chiều cao: 64 px; sticky ở đầu trang.
- Nền `surface.white`, border dưới `neutral.200`, shadow chỉ xuất hiện khi người dùng cuộn.
- Trái: logo DevConnect, liên kết về trang chủ.
- Giữa: ô tìm kiếm rộng 420–520 px, placeholder `Tìm bài viết theo tiêu đề...`.
- Phải khi chưa đăng nhập: `Đăng nhập`, button `Đăng ký`.
- Phải khi đã đăng nhập: button `Viết bài`, bookmark icon có tooltip, avatar menu.
- Avatar menu: Hồ sơ, Bài viết của tôi, Series, Bài đã lưu, Admin Panel nếu có quyền, Đăng xuất.
- Header không hiển thị menu Admin cho tài khoản thường.

### 7.2. Header mobile

- Chiều cao: 56 px.
- Nền trắng, logo xanh, icon menu màu `brand.navy.900`.
- Logo bên trái; search icon và avatar/menu icon bên phải.
- Nhấn search mở màn hình tìm kiếm toàn chiều rộng.
- Nhấn menu mở navigation drawer từ phải.

### 7.3. Footer

- Logo và mô tả ngắn.
- Liên kết: Trang chủ, Chủ đề, Viết bài, Điều khoản sử dụng giả lập cho đồ án.
- Dòng bản quyền và phiên bản.
- Không đặt chức năng nghiệp vụ quan trọng chỉ trong footer.

## 8. Component inventory

### 8.1. Button

Variants: `Primary`, `Secondary`, `Ghost`, `Danger`, `Link`.  
Sizes: `Small 32`, `Medium 40`, `Large 48`.  
States: `Default`, `Hover`, `Pressed`, `Focus`, `Disabled`, `Loading`.

Quy tắc:

- Mỗi khu vực hành động chỉ có một Primary button.
- Button Loading giữ nguyên chiều rộng và không cho nhấn lại.
- Danger button chỉ dùng cho thao tác có hậu quả mất dữ liệu hoặc loại nội dung khỏi công khai.

### 8.2. Form controls

Tạo component cho Text Input, Password Input, Textarea, Search Input, Select, Multi-select Tag, Checkbox, Radio, Toggle và File Upload.

Mỗi control có các trạng thái:

- Empty, Filled, Hover, Focus, Disabled, Read-only.
- Error với error text cụ thể.
- Success chỉ dùng khi cần xác nhận dữ liệu từ server.
- Loading đối với search/select gọi API.

Label đặt phía trên control. Trường bắt buộc có ký hiệu và mô tả bằng text, không chỉ dùng dấu sao mà không giải thích.

### 8.3. Article components

- `ArticleCard/Vertical`: thumbnail, Tag, tiêu đề, tóm tắt hai dòng, tác giả, ngày và thời gian đọc.
- `ArticleCard/Horizontal`: dùng cho tìm kiếm và bookmark.
- `ArticleMeta`: avatar, tác giả, ngày xuất bản, thời gian đọc.
- `ArticleStatusBadge`: Draft, Published, Hidden.
- `VoteControl`: upvote, score, downvote; selected state cho từng lựa chọn.
- `BookmarkButton`: icon + text tùy ngữ cảnh; saved/unsaved/loading.
- `SeriesNavigation`: Bài trước, vị trí hiện tại, Bài sau.

### 8.4. Feedback components

- Toast: success, error, warning, info; tự đóng sau 4–6 giây trừ lỗi cần đọc lâu.
- Inline alert: dùng cho lỗi quyền, lỗi upload và cảnh báo nội dung.
- Empty state: icon/illustration nhẹ, tiêu đề, mô tả và một hành động phù hợp.
- Skeleton: Article Card, Article Detail, Comment và Table.
- Dialog: Confirm Delete, Confirm Hide, Confirm Unpublish và Unsaved Changes.

### 8.5. Comment components

- Comment cấp 1 có avatar, tên, thời gian, nội dung, Trả lời và Xóa nếu thuộc sở hữu.
- Reply cấp 2 thụt 32 px desktop, 16 px mobile.
- Không hiển thị nút Trả lời ở reply cấp 2.
- Comment đã xóa nhưng còn reply hiển thị `Bình luận này đã được xóa`.
- Composer có textarea, bộ đếm ký tự, Cancel và Submit.

### 8.6. Data display cho dashboard/admin

- Data Table desktop: header, row, pagination, sorting indicator nếu có, bulk action không nằm trong MVP.
- Mobile Card Row: label/value và menu thao tác.
- Filter Bar: search, status, Tag và clear filter.
- Pagination: Previous, page numbers, Next; giữ filter trên URL.

## 9. Danh sách frame cần thiết kế

Mỗi màn hình chính phải có ít nhất frame desktop 1440 px và mobile 375 px. Những frame có dấu `*` cần thêm bản tablet 768 px.

| ID | Frame | Trạng thái bắt buộc | US |
|:---:|:---|:---|:---:|
| UI-01 | Home `*` | Default, Loading, Empty | US-01, US-02 |
| UI-02 | Search Results `*` | Results, Empty, Error, Filtered | US-02 |
| UI-03 | Article Detail `*` | Guest, Authenticated, In Series, Hidden/404 | US-01, 03, 04, 05, 08 |
| UI-04 | Login | Default, Error, Loading | US-11 |
| UI-05 | Register | Default, Validation Error, Success | US-11 |
| UI-06 | Public Profile | With Articles, Empty | US-01 |
| UI-07 | My Profile | View, Edit, Saving, Error | US-11 |
| UI-08 | Bookmarks | List, Empty, Removed Article | US-03 |
| UI-09 | Author Dashboard `*` | All, Draft, Published, Empty | US-07 |
| UI-10 | Markdown Editor `*` | New, Edit Draft, Saving, Validation Error, Unsaved | US-06, US-07 |
| UI-11 | Series List | List, Empty | US-08 |
| UI-12 | Series Editor `*` | Create, Reorder, Validation Error | US-08 |
| UI-13 | Series Detail | Default, No Previous/Next | US-08 |
| UI-14 | Admin Articles `*` | List, Filtered, Confirm Hide, Confirm Delete | US-09 |
| UI-15 | Admin Tags `*` | List, Create, Edit, Duplicate, Confirm Delete | US-10 |
| UI-16 | System States | 401, 403, 404, 500, Offline | Toàn hệ thống |

## 10. Đặc tả màn hình

### 10.1. UI-01 Trang chủ

**Mục tiêu:** giúp người dùng hiểu sản phẩm, tìm bài và mở nội dung nhanh.  
**Route:** `/`  
**Actor:** Khách, người dùng đã đăng nhập.

#### Bố cục desktop

1. Header toàn cục.
2. Hero gọn, cao khoảng 280–340 px:
   - Eyebrow: `Cộng đồng chia sẻ kiến thức công nghệ`.
   - H1: `Học hỏi, chia sẻ và phát triển cùng DevConnect`.
   - Search Input lớn và button `Tìm kiếm`.
   - Không đặt carousel trong hero.
3. Section `Chủ đề nổi bật`: tối đa 8 Tag chip.
4. Main content hai cột tỷ lệ 8/4:
   - Trái: `Bài viết mới nhất`, danh sách Article Card.
   - Phải: `Series nổi bật` hoặc `Chủ đề đang được quan tâm`.
5. Pagination ở cuối danh sách nếu trang chủ sử dụng phân trang.
6. Footer.

#### Mobile

- Hero rút gọn, search chiếm toàn chiều rộng.
- Tag chip cuộn ngang.
- Nội dung một cột; sidebar chuyển xuống sau bài viết.
- Article Card dùng dạng vertical.

#### Tương tác

- Submit search điều hướng `/search?q=<keyword>&page=1`.
- Nhấn Tag điều hướng `/search?tag=<slug>&page=1`.
- Nhấn card mở `/articles/[slug]`.

### 10.2. UI-02 Kết quả tìm kiếm

**Route:** `/search?q=&tag=&page=`  
**Mục tiêu:** cho phép kết hợp từ khóa, một Tag và phân trang 10 bài/trang.

#### Bố cục

- H1 `Kết quả tìm kiếm`.
- Search Input hiển thị từ khóa hiện tại.
- Filter Tag và button `Xóa bộ lọc`.
- Dòng kết quả: `Tìm thấy 24 bài viết`.
- Danh sách Article Card horizontal.
- Pagination cuối danh sách.

#### Trạng thái

- Loading: 5 Article Card skeleton.
- Empty: `Không tìm thấy bài viết phù hợp`; cho phép xóa Tag hoặc từ khóa.
- Error: mô tả ngắn + button `Thử lại`.
- Khi đổi từ khóa/Tag, `page` trở về 1.

### 10.3. UI-03 Chi tiết bài viết

**Route:** `/articles/[slug]`  
**Mục tiêu:** tối ưu trải nghiệm đọc, tương tác và điều hướng Series.

#### Bố cục desktop

- Breadcrumb: Trang chủ / Tag hoặc Series / Tên bài.
- Header bài: Tag, H1, tóm tắt, Article Meta.
- Layout 8/4:
  - Nội dung chính rộng tối đa 760 px.
  - Rail phải sticky: Vote, Bookmark, Table of Contents hoặc thông tin Series.
- Nội dung Markdown hỗ trợ heading, list, table, blockquote, ảnh và code block.
- Series Navigation sau nội dung.
- Khu vực bình luận sau Series Navigation.

#### Trạng thái theo quyền

- Guest thấy nút Vote/Bookmark/Bình luận nhưng khi nhấn sẽ được yêu cầu đăng nhập.
- Người dùng đã đăng nhập thấy selected state của vote và bookmark.
- Chủ bài thấy menu `Sửa bài` và `Đưa về Draft`.
- Bài Draft không dùng layout công khai; chủ sở hữu xem preview từ editor/dashboard.
- Bài Hidden/Deleted trả 404 công khai, không để lộ tiêu đề hoặc nội dung.

#### Mobile

- Rail chuyển thành action bar bên dưới metadata.
- Table of Contents là accordion.
- Vote và Bookmark không che nội dung khi cuộn.

### 10.4. UI-04 và UI-05 Đăng nhập, đăng ký

**Routes:** `/login`, `/register`  
**Mục tiêu:** hoàn thành xác thực nhanh, giữ đường dẫn quay lại.

#### Layout

- Desktop: form card rộng 420–480 px, căn giữa; bên cạnh có panel thương hiệu tùy chọn.
- Mobile: full-width form, không dùng panel hình ảnh lớn.
- Login: Email, Mật khẩu, hiện/ẩn mật khẩu, button Đăng nhập, link Đăng ký.
- Register: Tên hiển thị, Email, Mật khẩu, Xác nhận mật khẩu, button Tạo tài khoản.

#### Validation

- Hiển thị lỗi dưới field, không dùng toast làm nơi duy nhất báo lỗi form.
- Email đã tồn tại dùng thông báo rõ nhưng không hiển thị dữ liệu tài khoản.
- Button submit chuyển Loading và chống gửi lặp.
- Sau đăng nhập thành công, quay lại `next` nếu hợp lệ; nếu không, về trang chủ.

### 10.5. UI-06 và UI-07 Hồ sơ

#### Hồ sơ công khai `/users/[username]`

- Avatar, tên hiển thị, bio, ngày tham gia.
- Danh sách bài Published của tác giả.
- Không hiển thị email, Draft hoặc quyền Admin.

#### Hồ sơ cá nhân `/me`

- Tabs: `Hồ sơ`, `Bài đã lưu`.
- Form cập nhật avatar nếu có, tên hiển thị và bio.
- Email hiển thị read-only nếu backend không hỗ trợ đổi email.
- Không có control thay đổi role.
- Sau lưu hiển thị toast thành công; lỗi giữ lại dữ liệu đã nhập.

### 10.6. UI-08 Bookmark

**Route:** `/me/bookmarks`

- Danh sách Article Card horizontal có button `Bỏ lưu`.
- Bỏ lưu cập nhật ngay, có toast `Đã bỏ lưu bài viết` và Undo nếu frontend hỗ trợ an toàn.
- Empty state: `Bạn chưa lưu bài viết nào` + button `Khám phá bài viết`.
- Nếu bài không còn công khai, hiển thị item `Bài viết không còn khả dụng` và chỉ cho phép bỏ lưu.

### 10.7. UI-09 Author Dashboard

**Route:** `/dashboard/articles`

#### Layout desktop

- Sidebar: Bài viết, Series, Bookmark, Hồ sơ.
- Header trang: H1 `Bài viết của tôi`, button `Viết bài mới`.
- Summary cards: Tất cả, Published, Draft.
- Filter tabs: Tất cả, Published, Draft.
- Search theo tiêu đề trong nội dung của tác giả.
- Table: Tiêu đề, Trạng thái, Cập nhật, Tag, Thao tác.
- Row action: Xem trước, Sửa, Xuất bản/Đưa về Draft, Xóa.

#### Mobile

- Sidebar thành drawer.
- Summary card cuộn ngang hoặc grid 2 cột.
- Table chuyển thành card list; action nằm trong overflow menu.

#### Dialog

- Delete: hiển thị tên bài và hậu quả; button `Xóa bài viết` màu danger.
- Unpublish: giải thích bài sẽ bị loại khỏi tìm kiếm và Series công khai.

### 10.8. UI-10 Markdown Editor

**Routes:** `/editor/new`, `/editor/[id]`

#### Bố cục desktop

- Top bar sticky:
  - `Quay lại Dashboard`.
  - Trạng thái lưu: `Đã lưu lúc 20:15`, `Đang lưu...`, `Lưu thất bại`.
  - Button `Lưu nháp` và Primary `Xuất bản`.
- Metadata: Tiêu đề, Tóm tắt, Tag multi-select tối đa 5.
- ByteMD area chia đôi:
  - Trái: Markdown input.
  - Phải: live preview.
- Upload ảnh từ toolbar; hiển thị progress và lỗi ngay tại editor.
- Character count cho tiêu đề và nội dung nếu backend có giới hạn.

#### Responsive

- Tablet/mobile dùng segmented control `Viết | Xem trước`.
- Action bar mobile sticky ở đáy: `Lưu nháp`, `Xuất bản`.
- Khi bàn phím mobile mở, action bar không che vùng nhập.

#### Trạng thái và bảo vệ dữ liệu

- Draft cho phép dữ liệu tối thiểu theo contract; Published yêu cầu tiêu đề và nội dung hợp lệ.
- Thiếu field khi xuất bản: scroll/focus vào field lỗi đầu tiên.
- Điều hướng khi có thay đổi chưa lưu: dialog `Bạn có thay đổi chưa lưu`.
- JWT hết hạn: yêu cầu đăng nhập lại nhưng giữ nội dung phía client.
- Upload chỉ nhận PNG, JPEG, WebP tối đa 5 MB.

### 10.9. UI-11, UI-12 và UI-13 Series

#### Series List `/dashboard/series`

- H1 `Series của tôi`, button `Tạo Series`.
- Card hiển thị tên, mô tả, số bài, cập nhật gần nhất và thao tác.
- Empty state hướng dẫn tạo Series đầu tiên.

#### Series Editor `/dashboard/series/[id]`

- Field: Tên, Slug preview, Mô tả.
- Khối `Bài có thể thêm`: chỉ bài Published thuộc tác giả.
- Khối `Thứ tự trong Series`: drag handle, số thứ tự, tiêu đề và nút Gỡ.
- Có lựa chọn thay thế drag-and-drop bằng `Di chuyển lên/xuống` để hỗ trợ bàn phím.
- Không cho lưu một bài hai lần trong cùng Series.
- Button `Lưu thay đổi` có loading và success state.

#### Series Detail `/series/[slug]`

- Tên, mô tả, tác giả, số bài.
- Danh sách đánh số theo thứ tự.
- Chỉ hiển thị bài Published, không Hidden và chưa xóa.
- Trang bài trong Series có Bài trước/Bài sau; nút không có đích bị disabled hoặc không hiển thị.

### 10.10. UI-14 Admin kiểm duyệt bài viết

**Route:** `/admin/articles`  
**Quyền:** Admin.

#### Layout

- Admin sidebar khác biệt rõ với dashboard tác giả, có badge `ADMIN`.
- H1 `Kiểm duyệt bài viết`.
- Filter Bar: từ khóa, trạng thái Published/Hidden, Tag.
- Table: Bài viết, Tác giả, Trạng thái, Ngày cập nhật, Thao tác.
- Thao tác: Xem, Ẩn, Xóa.

#### Dialog

- Hide: yêu cầu lý do; giải thích bài sẽ biến mất khỏi danh sách, tìm kiếm, Series và URL công khai nhưng dữ liệu vẫn được giữ.
- Delete: xác nhận nguy hiểm, hiển thị tiêu đề bài; không dùng dialog giống Hide.
- Thành công cập nhật row và hiển thị toast.
- Lỗi 403 điều hướng tới trang Không đủ quyền.

Admin không được thiết kế chức năng sửa nội dung bài của tác giả hoặc đọc Draft của người khác.

### 10.11. UI-15 Admin quản lý Tag

**Route:** `/admin/tags`

- H1 `Quản lý Tag`, button `Tạo Tag`.
- Table: Tên, Slug, Màu, Số bài, Cập nhật, Thao tác.
- Create/Edit dùng modal hoặc side sheet với Tên, Màu và Mô tả.
- Preview Tag chip cập nhật trực tiếp khi chọn màu.
- Tên trùng sau trim và so sánh không phân biệt hoa/thường hiển thị inline error.
- Xóa Tag đang được dùng phải cho biết số bài bị gỡ liên kết và yêu cầu xác nhận.
- Xóa Tag không xóa bài viết.

### 10.12. UI-16 Trạng thái hệ thống

Thiết kế các trạng thái dùng chung:

- `401 Chưa đăng nhập`: CTA Đăng nhập và Quay lại.
- `403 Không đủ quyền`: mô tả quyền cần thiết, không hiển thị dữ liệu bảo vệ.
- `404 Không tìm thấy`: dùng cho bài Draft/Hidden/Deleted đối với người công khai.
- `500 Có lỗi xảy ra`: request ID nếu có, Thử lại và Về trang chủ.
- `Offline`: giữ nội dung editor nếu có, thông báo trạng thái mạng.
- `Empty`: nội dung cụ thể theo màn hình, không dùng một thông báo chung cho mọi nơi.

## 11. Prototype flows trên Figma

### Flow A Khách tìm và đọc bài

```text
Home → nhập từ khóa → Search Results → chọn Tag → Article Detail
```

Bao phủ US-01 và US-02. Prototype phải thể hiện query/filter hiện tại và thao tác quay lại vẫn giữ bộ lọc.

### Flow B Thành viên tương tác

```text
Article Detail Guest → Bookmark → Login → quay lại Article Detail
→ Bookmark Saved → Upvote → Comment → Reply
```

Bao phủ US-03, US-04, US-05 và US-11.

### Flow C Tác giả viết và xuất bản

```text
Author Dashboard → New Article → Editor → Upload Image
→ Save Draft → Dashboard Draft → Edit → Publish → Article Detail
```

Bao phủ US-06 và US-07. Cần thêm nhánh validation error khi thiếu tiêu đề hoặc nội dung.

### Flow D Quản lý Series

```text
Series List → Create Series → Add Published Articles
→ Reorder → Save → Series Detail → Article → Next Article
```

Bao phủ US-08.

### Flow E Admin kiểm duyệt

```text
Admin Articles → Filter → View Article → Hide Dialog
→ Confirm → Hidden State → Admin Tags → Create/Edit/Delete Tag
```

Bao phủ US-09 và US-10. Delete phải là nhánh riêng với cảnh báo mạnh hơn Hide.

## 12. Microcopy và nội dung mẫu

### 12.1. Quy tắc viết UI text

- Dùng tiếng Việt thống nhất, câu ngắn và trực tiếp.
- Button bắt đầu bằng động từ: `Lưu nháp`, `Xuất bản`, `Tạo Series`, `Xóa Tag`.
- Không dùng `OK` cho hành động quan trọng.
- Lỗi nói rõ vấn đề và cách sửa; không dùng `Có lỗi xảy ra` nếu biết nguyên nhân.
- Trạng thái dùng `Bản nháp`, `Đã xuất bản`, `Đã ẩn`; có thể kèm thuật ngữ Draft/Published trong tài liệu kỹ thuật nhưng UI ưu tiên tiếng Việt.

### 12.2. Nội dung mẫu cho Figma

- Tiêu đề bài: `Xây dựng REST API an toàn với FastAPI`.
- Tác giả: `Nguyễn An`.
- Tag: `Python`, `FastAPI`, `Backend`.
- Series: `FastAPI từ cơ bản đến triển khai`.
- Tóm tắt: `JWT, quyền sở hữu dữ liệu và cách tổ chức service rõ ràng trong FastAPI.`
- Bình luận: `Phần phân quyền có cần kiểm tra thêm ở frontend không?`.
- Empty bookmark: `Bạn chưa lưu bài viết nào. Hãy khám phá và lưu những nội dung hữu ích để đọc lại sau.`
- Search empty: `Không tìm thấy bài viết phù hợp với từ khóa và Tag hiện tại.`

## 13. Accessibility checklist

- Text thường đạt tương phản tối thiểu 4.5:1; text lớn tối thiểu 3:1.
- Focus state nhìn thấy rõ trên link, button, field, tab, menu và dialog.
- Thứ tự Tab đi theo thứ tự thị giác hợp lý.
- Icon button có accessible name/tooltip trong annotation.
- Form có label cố định; placeholder không thay cho label.
- Error liên kết với field và không chỉ hiển thị bằng màu.
- Dialog giữ focus bên trong và trả focus về trigger khi đóng.
- Drag-and-drop Series có thao tác thay thế bằng bàn phím.
- Code block có scroll riêng và nhãn ngôn ngữ nếu có.
- Ảnh nội dung có vùng annotation cho alt text.
- Touch target mobile tối thiểu 44 x 44 px.
- Animation tôn trọng reduced motion; không dùng hiệu ứng nhấp nháy.

## 14. Annotation cho frontend handoff

Mỗi frame hoàn chỉnh cần ghi chú:

- Route và quyền truy cập.
- User Story liên quan.
- Container/grid và breakpoint.
- Component được sử dụng.
- Dữ liệu động và giới hạn ký tự.
- Trạng thái loading, empty, error và disabled.
- Hành động điều hướng hoặc gọi API.
- Quy tắc ownership/role ảnh hưởng đến hiển thị.
- Hành vi mobile khác desktop.

Token trong Figma nên ánh xạ sang Tailwind semantic classes thay vì gắn trực tiếp tên màu vào component. Ví dụ:

```text
bg-primary       → brand.blue.600
text-primary     → neutral.950
text-secondary   → neutral.500
border-default   → neutral.300
bg-success       → success.100
text-danger      → danger.700
```

## 15. Ma trận truy vết UI và User Story

| User Story | Màn hình chính | Thành phần quan trọng |
|:---:|:---|:---|
| US-01 | Home, Article Detail, Public Profile | Article Card, Markdown Renderer, Article Meta |
| US-02 | Home, Search Results, Tag Results | Search Input, Tag Filter, Pagination |
| US-03 | Article Detail, Bookmarks | Bookmark Button, Article Card |
| US-04 | Article Detail | Vote Control |
| US-05 | Article Detail | Comment Composer, Comment Thread |
| US-06 | Markdown Editor | ByteMD, Upload, Preview |
| US-07 | Author Dashboard, Markdown Editor | Status Badge, Save Draft, Publish, Delete Dialog |
| US-08 | Series List, Series Editor, Series Detail | Reorder List, Series Navigation |
| US-09 | Admin Articles | Admin Table, Hide Dialog, Delete Dialog |
| US-10 | Admin Tags | Tag Table, Tag Form, Duplicate Error |
| US-11 | Login, Register, My Profile | Auth Form, Avatar Menu, Profile Form |

## 16. Definition of Done cho thiết kế Figma

Thiết kế được xem là hoàn tất khi:

- Có đủ 16 nhóm frame trong mục 9.
- Tất cả màn hình chính có desktop 1440 px và mobile 375 px.
- Home, Search, Article, Editor, Dashboard, Series Editor và Admin có bản responsive cần thiết.
- Design token được tạo bằng Variables/Styles, không dùng màu và spacing tùy ý.
- Component có variant và trạng thái đầy đủ; không detach component trong frame cuối nếu không cần thiết.
- Prototype chạy được trọn vẹn 5 flow A–E.
- Có loading, empty, error, success và destructive confirmation.
- Không hiển thị chức năng ngoài phạm vi hoặc sai quyền.
- Contrast, focus, keyboard flow và touch target đã được kiểm tra.
- Tên layer, component và frame tuân thủ quy ước.
- Page `10 Handoff` có screen map, route, breakpoint, token và annotation cho frontend.

---

## Phụ lục A. Thứ tự ưu tiên thiết kế

Nếu thời gian hạn chế, thực hiện theo thứ tự:

1. Foundations và component cốt lõi.
2. Home, Search Results và Article Detail.
3. Login, Register và My Profile.
4. Author Dashboard và Markdown Editor.
5. Series List, Series Editor và Series Detail.
6. Admin Articles và Admin Tags.
7. Responsive variants, system states và prototype flows.

## Phụ lục B. Các quyết định không được tự suy diễn trong Figma

- Không thêm role Moderator riêng; phiên bản hiện tại chỉ dùng User/Tác giả và Admin.
- Không thêm chức năng báo cáo nội dung nếu chưa được bổ sung vào requirement.
- Không cho Admin chỉnh sửa nội dung gốc hoặc đọc Draft của tác giả khác.
- Không cho người dùng tự chọn hoặc nâng role Admin.
- Không hiển thị Draft, Hidden hoặc Deleted trong vùng công khai.
- Không cho Series chứa bài Draft hoặc bài không thuộc quyền quản lý của tác giả.
- Không cho bình luận sâu hơn hai cấp.
- Không thiết kế nhiều lựa chọn vote ngoài Upvote, Downvote và hủy lựa chọn.
