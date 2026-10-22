# Hướng dẫn chi tiết: tạo MP3 → tải lên GitHub bằng trình duyệt → gửi link cho học sinh

> Làm theo thứ tự **A → B → C → D → E → F**. Bước tạo **MP3 (phần C) làm TRƯỚC**, rồi mới tải tất cả lên GitHub (phần E).
> Tạo MP3 bằng CMD nhưng **không cần `cd`, không cần gõ đường dẫn** (chỉ kéo thả `tao_mp3.py` vào CMD); đưa lên GitHub bằng trình duyệt (kéo thả), không cần cài Git.

---

## A. Cài Python (làm 1 lần duy nhất)

Tải tại https://www.python.org/downloads/ → mở file vừa tải → **bắt buộc tick ô "Add python.exe to PATH"** ở màn hình đầu tiên → Install Now.
(Hoặc mở CMD gõ `winget install Python.Python.3.12`.)

Bạn cũng cần một **tài khoản GitHub** miễn phí (đăng ký tại https://github.com).

---

## B. Giải nén

Giải nén file zip ra **Desktop** để có thư mục `thi giua ky 13 18`. Mở ra phải thấy: `tao_mp3.py`, `index.html`, `README.md`, thư mục `js`, `data`, `audio` (đang trống), `tools`.
(Nếu mở ra lại thấy thêm một thư mục con cùng tên, đi vào thư mục con đó.)

---

## C. TẠO MP3 bằng CMD (làm trước khi tải lên GitHub)

Cách này **không cần `cd`, không cần gõ đường dẫn, không đụng tới user profile**. CMD mở ở đâu thì tạo thư mục `audio` mới ngay ở đó.

1. Máy có Internet. Nhấn phím **Windows**, gõ `cmd`, nhấn **Enter** (không cần đi đâu cả).
2. Trong cửa sổ CMD gõ chữ `python` rồi **một dấu cách** (đừng nhấn Enter).
3. Mở thư mục `thi giua ky 13 18` trên Desktop, **kéo file `tao_mp3.py` thả vào cửa sổ CMD**. Đường dẫn tự điền sau chữ `python`. Nhấn **Enter**.
4. Đợi 1–3 phút: máy tự cài thư viện, tự tạo thư mục `audio` mới rồi tạo từng file (`OK s01`, `OK s02`, … `s54`). Cuối cùng hiện `XONG: co 54/54 file MP3 trong: <đường dẫn thư mục audio>` và **thư mục `audio` tự mở ra**.
5. Nhấn Enter để đóng CMD.

**Chuyển thư mục `audio` vào thư mục bài thi:**
1. Cửa sổ vừa tự mở đang nằm trong thư mục `audio` mới. Bấm mũi tên lên (↑) để ra ngoài 1 cấp, chuột phải vào thư mục **`audio`** → **Cut** (cắt).
2. Mở thư mục `thi giua ky 13 18` trên Desktop. **Xoá thư mục `audio` trống cũ** trong đó. Rồi chuột phải chỗ trống → **Paste** (dán).
3. Mở `thi giua ky 13 18\audio`: phải thấy ngay `s01.mp3` … `s54.mp3` (54 file). Nếu thấy thêm một thư mục `audio` con thì kéo các file ra ngoài.

**Nghe thử:** bấm đúp `s01.mp3` (câu: 这封信是他从国外寄过来的。), giọng đọc chậm, rõ.

**Nếu CMD báo 403:** script đã tự nâng cấp thư viện. Nếu Microsoft vẫn từ chối, nó tự chuyển sang giọng dự phòng của Google (đọc nhanh hơn một chút) và vẫn tạo đủ 54 file.
**Nếu thiếu file (mạng yếu):** làm lại bước 1–3, script chỉ tạo các file còn thiếu trong thư mục `audio` đang có.
**Nếu CMD báo `'python' is not recognized`:** quay lại phần A, nhớ tick "Add python.exe to PATH", rồi mở CMD mới.

---

## D. Thử đề trên máy (trước khi tải lên)

Bấm đúp vào `index.html` trong thư mục `thi giua ky 13 18` (mở bằng Chrome/Edge). Nhập tên → Bắt đầu → bấm "▶ Nghe" ở một câu nghe: nghe được giọng vừa tạo là đạt. **Đừng bấm "Nộp bài"** khi thử. Nếu lỡ nộp, thêm `#reset` vào cuối địa chỉ trên thanh địa chỉ rồi nhấn Enter và tải lại trang.

---

## E. Tải lên GitHub bằng trình duyệt

### E1. Tạo kho (repository)
1. Vào https://github.com và đăng nhập.
2. Bấm dấu **+** ở góc trên bên phải → **New repository**.
3. **Repository name:** `thi-giua-ky` (viết không dấu, không cách).
4. Chọn **Public** (bắt buộc để trang web miễn phí hoạt động).
5. Không tick gì thêm → bấm **Create repository**.

### E2. Kéo thả file lên
1. Ở trang kho vừa tạo, bấm liên kết **uploading an existing file** (hoặc: nút **Add file** → **Upload files**).
2. Mở thư mục `thi giua ky 13 18` trong File Explorer. **Chọn tất cả bên trong** (Ctrl+A): `tao_mp3.py`, `index.html`, `README.md`, các thư mục `js`, `data`, `audio`, `tools`.
3. **Kéo thả** vào khung trên trang GitHub. (Phải kéo thả thư mục `audio` cùng nội dung, không kéo file zip.)
4. Đợi thanh tải chạy xong, danh sách file hiện đủ. Tổng khoảng 62 file, nằm trong giới hạn 100 file mỗi lần tải của GitHub.
5. Kéo xuống dưới, bấm **Commit changes** (nút xanh).

> Nếu GitHub báo quá nhiều file hoặc tải bị đứng: tải làm 2 lượt. Lượt 1: `index.html`, `README.md`, `tao_mp3.py`, `js`, `data`, `tools`. Lượt 2: vào lại **Add file → Upload files**, kéo riêng thư mục `audio`.

### E3. Kiểm tra đã lên đủ
Trang kho phải hiện: `audio`, `data`, `js`, `tools`, `index.html`, `README.md`. Bấm vào thư mục `audio` phải thấy **54 file** `s01.mp3 … s54.mp3`.

### E4. Bật trang web (GitHub Pages)
1. Trong kho, bấm tab **Settings** (hình bánh răng, trên cùng).
2. Thanh bên trái chọn **Pages**.
3. Mục **Build and deployment** → **Source:** chọn **Deploy from a branch**.
4. **Branch:** chọn `main`, thư mục `/ (root)` → bấm **Save**.
5. Đợi 1–2 phút, tải lại trang Settings → Pages sẽ hiện dòng:
   `Your site is live at https://TEN_GITHUB.github.io/thi-giua-ky/`
   (`TEN_GITHUB` là tên tài khoản GitHub của bạn.)

---

## F. Kiểm tra và gửi cho học sinh

1. Mở link `https://TEN_GITHUB.github.io/thi-giua-ky/` → thấy trang "期中考试 · Thi giữa kỳ".
2. Mở thử `https://TEN_GITHUB.github.io/thi-giua-ky/audio/s01.mp3` → nghe được giọng đọc (báo 404 nghĩa là MP3 chưa lên đủ, xem E2–E3).
3. Thử trên điện thoại: mở link, bấm "▶ Nghe", kiểm tra có tiếng (tắt chế độ im lặng).
4. **Không bấm "Nộp bài" khi thử** (hoặc thêm `#reset` vào cuối link để xoá).
5. Gửi link cho học sinh. Mỗi học sinh dùng Chrome/Edge/Safari trên máy của mình.

---

## G. Trong ngày thi

- Học sinh nhập họ tên → làm → "📮 Nộp bài" → **chụp màn hình trang kết quả** (hoặc copy chuỗi mã kết quả) gửi cho bạn.
- Trang kết quả có điểm tổng /300, điểm từng phần /100, số thứ tự câu sai và **hàng hoa nhỏ mờ `✿` ở góc dưới**: 1 hoa = lần thi đầu, 2 hoa = lần thứ hai… (đếm theo từng máy).
- Cho một học sinh thi lại: bảo họ mở link kèm `#reset` ở cuối, ví dụ `https://TEN_GITHUB.github.io/thi-giua-ky/#reset`, rồi mở lại link thường. Bộ đếm hoa không bị xoá.
- Nếu lỡ tải lại trang giữa chừng, bài tự lưu; nhập lại đúng họ tên để tiếp tục.

---

## H. Sửa đề / cập nhật sau này

1. Sửa trên máy: mở `js\data.js` bằng Notepad. Mỗi dòng: `bài|từ|nghĩa|câu ví dụ`. Từ phải xuất hiện nguyên văn trong câu. **Thêm câu mới ở CUỐI** (để số thứ tự audio cũ không lệch). Bố cục đề 18/18/18 chỉ đúng khi tổng đúng 54 từ.
2. Muốn đổi một câu cũ: xoá `audio\sXX.mp3` của câu đó (XX = số dòng).
3. Mở CMD, gõ `python ` rồi kéo thả file `tools\export_sentences.py` vào CMD → Enter (cập nhật `data\sentences.txt` và `tao_mp3.py`). Sau đó làm lại phần C (kéo thả `tao_mp3.py` mới); nhớ xoá các MP3 cũ cần thay trong `audio` ở thư mục dự án, hoặc chép MP3 mới vào ghi đè.
4. Lên GitHub: vào kho → **Add file → Upload files** → kéo thả các file đã đổi (`js\data.js`, `data\sentences.txt`, `tao_mp3.py` và các MP3 mới). File trùng tên sẽ được ghi đè. Muốn tải vào thư mục `audio`, mở thư mục `audio` trong kho trước rồi mới chọn Upload files. Bấm **Commit changes**.
5. Đợi 1–2 phút là web tự cập nhật.

---

## I. Lỗi thường gặp

| Hiện tượng | Cách xử lý |
|---|---|
| `'python' is not recognized` | Cài Python và tick "Add python.exe to PATH", rồi mở CMD mới. |
| Tạo MP3 báo `403 Invalid response status` | Microsoft chặn bản cũ hoặc đồng hồ máy sai. Script đã tự nâng cấp thư viện; nếu vẫn 403 thì tự chuyển sang giọng dự phòng của Google (đọc nhanh hơn, không chỉnh được tốc độ). Cũng nên kiểm tra đồng hồ Windows đúng giờ (Settings → Time & language → Sync now) và tắt VPN. |
| Tạo MP3 báo lỗi kết nối | Kiểm tra Internet, tắt VPN, chạy lại (file đã xong sẽ được bỏ qua). |
| Có file MP3 nhưng 0 KB | Xoá file đó rồi làm lại phần C. |
| Mở link GitHub Pages báo 404 | Chờ 1–2 phút. Kiểm tra E4 đã Save chưa, kho đã Public chưa, và `index.html` nằm ở **thư mục gốc** của kho (không nằm trong thư mục con). |
| Web chạy nhưng nghe giọng "máy tính" khác | MP3 chưa lên kho. Xem E3, tải lại thư mục `audio`. |
| Điện thoại không có tiếng | Tắt chế độ im lặng, tăng âm lượng, chạm vào nút ▶ Nghe. |
| Sau khi sửa file, web vẫn như cũ | Chờ 1–2 phút rồi nhấn Ctrl+F5 để tải lại. |

---

## Cấu trúc các file
```
tao_mp3.py                kéo thả vào CMD để tạo MP3 (tự sinh, đã chứa sẵn các câu)
index.html                bài thi
js/data.js                dữ liệu: từ, nghĩa, câu ví dụ
data/sentences.txt        câu để đọc (tự sinh từ data.js)
audio/s01.mp3 … s54.mp3   âm thanh câu nghe (bạn tạo ở phần C)
tools/export_sentences.py data.js → sentences.txt + tao_mp3.py
tools/tao_mp3_template.py mẫu để sinh tao_mp3.py
```
