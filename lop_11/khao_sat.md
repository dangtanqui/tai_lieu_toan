# Gợi ý Toán Lớp 11 (Kết nối tri thức)

> Tổng hợp kiến thức trọng tâm – chia Đại số & Giải tích / Hình học – dùng để ôn tập và rà soát lỗ hổng.

---

## Đại số & Giải tích

### Hàm số lượng giác và phương trình lượng giác

#### Góc lượng giác và đơn vị radian

- Góc lượng giác: góc có hướng quay (dương: ngược chiều kim đồng hồ; âm: cùng chiều)
- Đơn vị radian: 1 rad = góc ở tâm chắn cung có độ dài bằng bán kính
- Đổi đơn vị: 180° = pi rad
+ Từ độ sang radian: alpha(rad) = alpha(°) x pi / 180
+ Từ radian sang độ: alpha(°) = alpha(rad) x 180 / pi
- Ví dụ: 60° = pi/3 rad; 90° = pi/2 rad; 45° = pi/4 rad.
- Hỏi: 1 rad bằng khoảng bao nhiêu độ? (≈ 57,3°)

#### Giá trị lượng giác (mở rộng)

- Đường tròn lượng giác: điểm M(cos(alpha); sin(alpha)) trên đường tròn đơn vị
- Dấu của sin, cos, tan, cot theo từng góc phần tư:
+ Góc phần tư I: sin > 0, cos > 0
+ Góc phần tư II: sin > 0, cos < 0
+ Góc phần tư III: sin < 0, cos < 0
+ Góc phần tư IV: sin < 0, cos > 0
- Công thức lượng giác cơ bản:
+ sin^2(a) + cos^2(a) = 1
+ tan(a) = sin(a) / cos(a); cot(a) = cos(a) / sin(a)
+ 1 + tan^2(a) = 1 / cos^2(a); 1 + cot^2(a) = 1 / sin^2(a)
- Công thức cộng:
+ sin(a + b) = sin(a).cos(b) + cos(a).sin(b)
+ sin(a - b) = sin(a).cos(b) - cos(a).sin(b)
+ cos(a + b) = cos(a).cos(b) - sin(a).sin(b)
+ cos(a - b) = cos(a).cos(b) + sin(a).sin(b)
- Công thức nhân đôi:
+ sin(2a) = 2.sin(a).cos(a)
+ cos(2a) = cos^2(a) - sin^2(a) = 2cos^2(a) - 1 = 1 - 2sin^2(a)
- Công thức hạ bậc:
+ sin^2(a) = (1 - cos(2a)) / 2
+ cos^2(a) = (1 + cos(2a)) / 2
- Công thức biến đổi tổng thành tích, tích thành tổng (tra bảng khi cần)

#### Hàm số lượng giác

- y = sin(x): chu kỳ 2pi, TXĐ = R, giá trị thuộc [-1; 1], hàm lẻ
- y = cos(x): chu kỳ 2pi, TXĐ = R, giá trị thuộc [-1; 1], hàm chẵn
- y = tan(x): chu kỳ pi, TXĐ: x ≠ pi/2 + k.pi, hàm lẻ
- y = cot(x): chu kỳ pi, TXĐ: x ≠ k.pi, hàm lẻ
- Hỏi: Đồ thị y = sin(x) và y = cos(x) khác nhau thế nào? (dịch pha pi/2)

#### Phương trình lượng giác cơ bản

- sin(x) = m (|m| <= 1): x = alpha + k.2pi hoặc x = pi - alpha + k.2pi (với sin(alpha) = m)
- cos(x) = m (|m| <= 1): x = alpha + k.2pi hoặc x = -alpha + k.2pi (với cos(alpha) = m)
- tan(x) = m: x = alpha + k.pi (với tan(alpha) = m)
- cot(x) = m: x = alpha + k.pi (với cot(alpha) = m)
- Trong đó k là số nguyên (k thuộc Z).
- Ví dụ: Giải sin(x) = 1/2. Giải cos(2x) = 0.
- Phương trình dạng a.sin(x) + b.cos(x) = c: đưa về dạng cơ bản bằng phương pháp phụ.

### Dãy số

#### Dãy số, dãy số bị chặn, dãy đơn điệu

- Dãy số: hàm số u(n) với n là số tự nhiên, ký hiệu (un)
- Dãy tăng: u(n+1) > u(n), mọi n; dãy giảm: u(n+1) < u(n), mọi n
- Dãy bị chặn trên/dưới
- Ví dụ: Dãy un = 2n + 1 tăng hay giảm?

#### Cấp số cộng

- Dãy (un) là cấp số cộng nếu u(n+1) - u(n) = d (không đổi, d gọi là công sai)
- Số hạng tổng quát: un = u1 + (n - 1) x d
- Tổng n số hạng đầu: Sn = n x (u1 + un) / 2 = n x (2u1 + (n-1)d) / 2
- Tính chất: u(k) = (u(k-1) + u(k+1)) / 2
- Ví dụ: CSC có u1 = 3, d = 5. Tìm u10 và S10.

#### Cấp số nhân

- Dãy (un) là cấp số nhân nếu u(n+1) / u(n) = q (không đổi, q gọi là công bội, q ≠ 0)
- Số hạng tổng quát: un = u1 x q^(n-1)
- Tổng n số hạng đầu: Sn = u1 x (1 - q^n) / (1 - q) (khi q ≠ 1)
- Tính chất: u(k)^2 = u(k-1) x u(k+1)
- Ví dụ: CSN có u1 = 2, q = 3. Tìm u5 và S5.
- Hỏi: Lãi suất kép (tiền gửi ngân hàng) liên quan đến CSC hay CSN?

### Giới hạn

#### Giới hạn của dãy số

- Dãy (un) có giới hạn L: khi n tiến tới vô cùng, un tiến về L; ký hiệu lim(un) = L
- Các giới hạn cơ bản:
+ lim(c) = c (c là hằng số)
+ lim(1/n) = 0
+ lim(1/n^k) = 0 (k > 0)
- Dãy phân kỳ: không có giới hạn hữu hạn
- Giới hạn vô cực: lim(un) = +vô cực hoặc -vô cực
- Quy tắc tính: lim(un + vn) = lim(un) + lim(vn); lim(un x vn) = lim(un) x lim(vn)
- Dạng vô định: vô cực / vô cực → chia cho lũy thừa cao nhất
- Ví dụ: lim((3n^2 + 1) / (n^2 - 2)) = ?

#### Giới hạn của hàm số

- lim f(x) khi x tiến đến a: giá trị mà f(x) tiến về khi x gần a (x ≠ a)
- Giới hạn một bên: giới hạn bên trái và bên phải
- Giới hạn tại vô cực: lim f(x) khi x tiến đến +vô cực hoặc -vô cực
- Tiệm cận ngang: y = L nếu lim f(x) = L khi x tiến đến vô cực
- Tiệm cận đứng: x = a nếu lim f(x) = vô cực khi x tiến đến a
- Ví dụ: lim((x^2 - 1) / (x - 1)) khi x tiến đến 1 = ?

#### Hàm số liên tục

- f(x) liên tục tại x = a nếu: lim f(x) khi x tiến đến a = f(a)
- Hàm số liên tục trên đoạn [a; b]
- Hỏi: Hàm y = 1/x có liên tục tại x = 0 không?

### Đạo hàm

#### Khái niệm đạo hàm

- Đạo hàm của f(x) tại x0: f'(x0) = lim((f(x0 + h) - f(x0)) / h) khi h tiến đến 0
- Ý nghĩa hình học: f'(x0) là hệ số góc của tiếp tuyến với đồ thị tại điểm (x0; f(x0))
- Phương trình tiếp tuyến tại M(x0; y0): y - y0 = f'(x0) x (x - x0)
- Ý nghĩa vật lý: vận tốc tức thời v(t) = s'(t)

#### Bảng đạo hàm cơ bản

- (c)' = 0
- (x^n)' = n x x^(n-1)
- (sin(x))' = cos(x)
- (cos(x))' = -sin(x)
- (tan(x))' = 1 / cos^2(x)
- (cot(x))' = -1 / sin^2(x)

#### Quy tắc tính đạo hàm

- (u + v)' = u' + v'
- (u - v)' = u' - v'
- (u x v)' = u' x v + u x v'
- (u / v)' = (u' x v - u x v') / v^2
- Đạo hàm hàm hợp: (f(u))' = f'(u) x u'
- Ví dụ: Tính đạo hàm y = x^3 - 3x^2 + 2. Tính đạo hàm y = sin(2x + 1).
- Ví dụ: Viết phương trình tiếp tuyến của y = x^2 - 4x + 3 tại x = 1.

### Thống kê

- Bảng tần số, tần suất, tần số tích lũy
- Biểu đồ tần suất hình cột, biểu đồ đường gấp khúc tần suất
- Hỏi: Khi nào dùng biểu đồ cột, khi nào dùng biểu đồ tròn?

### Xác suất

#### Các quy tắc tính xác suất

- Xác suất có điều kiện: P(A|B) = P(A giao B) / P(B)
- Công thức nhân: P(A giao B) = P(B) x P(A|B)
- Hai biến cố độc lập: P(A giao B) = P(A) x P(B)
- Công thức xác suất toàn phần
- Ví dụ: Hộp có 3 bi đỏ, 7 bi xanh. Lấy lần lượt 2 bi không trả lại. Tính P(bi thứ 2 đỏ).

#### Biến ngẫu nhiên rời rạc

- Biến ngẫu nhiên rời rạc X: nhận các giá trị x1, x2, ..., xn với xác suất tương ứng p1, p2, ..., pn
- Bảng phân phối xác suất: tổng các pi = 1
- Kỳ vọng: E(X) = tổng xi x pi (giá trị trung bình kỳ vọng)
- Phương sai: D(X) = tổng (xi - E(X))^2 x pi
- Độ lệch chuẩn: sigma = sqrt(D(X))
- Ví dụ: Gieo xúc xắc, X là số chấm. Tính E(X) và D(X).

---

## Hình học

### Đường thẳng và mặt phẳng trong không gian – Quan hệ song song

#### Các khái niệm mở đầu

- Điểm, đường thẳng, mặt phẳng trong không gian
- Các tính chất thừa nhận (tiên đề):
+ Qua 3 điểm không thẳng hàng xác định duy nhất 1 mặt phẳng
+ Nếu đường thẳng có 2 điểm thuộc mặt phẳng thì nằm trọn trong mặt phẳng
+ Hai mặt phẳng có 1 điểm chung thì có chung 1 đường thẳng (giao tuyến)
- Hình biểu diễn: cách vẽ hình không gian trên mặt phẳng

#### Hai đường thẳng song song trong không gian

- 3 vị trí tương đối của 2 đường thẳng: cắt nhau, song song, chéo nhau
- Hỏi: Hai đường thẳng chéo nhau khác song song chỗ nào? (không cùng mặt phẳng)
- Định lí: Qua 1 điểm ngoài đường thẳng a, có duy nhất 1 đường thẳng song song với a.
- Nếu 2 đường thẳng cùng song song với đường thẳng thứ ba thì song song với nhau.

#### Đường thẳng song song với mặt phẳng

- Đường thẳng a song song với mặt phẳng (P) nếu a không có điểm chung với (P)
- Dấu hiệu: a song song với (P) nếu a song song với 1 đường thẳng b nằm trong (P)
- Hỏi: Nếu đường thẳng a song song (P) thì mọi đường thẳng trong (P) có song song a không? (Không, chỉ những đường cùng phương)

#### Hai mặt phẳng song song

- Hai mặt phẳng (P) và (Q) song song nếu không có điểm chung
- Dấu hiệu: (P) chứa 2 đường thẳng cắt nhau cùng song song với (Q) → (P) // (Q)
- Tính chất: nếu 2 mp song song thì mọi mặt phẳng cắt chúng sẽ tạo ra 2 giao tuyến song song.

### Quan hệ vuông góc trong không gian

#### Đường thẳng vuông góc với mặt phẳng

- Đường thẳng a vuông góc với mặt phẳng (P) nếu a vuông góc với mọi đường thẳng trong (P)
- Dấu hiệu: a vuông góc với 2 đường thẳng cắt nhau trong (P) → a vuông góc (P)
- Hỏi: Muốn chứng minh đường thẳng vuông góc mặt phẳng cần chứng minh bao nhiêu cặp vuông góc? (2 cặp, 2 đường thẳng cắt nhau trong mp)

#### Định lí ba đường vuông góc

- Cho a vuông góc (P), a cắt (P) tại H, b nằm trong (P). Gọi b' là hình chiếu vuông góc lên (P):
+ b vuông góc b' ↔ b vuông góc hình chiếu

#### Góc giữa đường thẳng và mặt phẳng

- Hình chiếu của đường thẳng a lên mặt phẳng (P): a' (qua phép chiếu vuông góc)
- Góc giữa a và (P) = góc giữa a và a' (hình chiếu của a lên P)
- Góc này nằm trong khoảng [0°; 90°]
- Đặc biệt: a vuông góc (P) thì góc = 90°; a song song hoặc nằm trong (P) thì góc = 0°

#### Hai mặt phẳng vuông góc

- Góc nhị diện: góc tạo bởi 2 nửa mặt phẳng có chung 1 cạnh
- Góc nhị diện = góc giữa 2 nửa đường thẳng nằm trên 2 nửa mặt phẳng, cùng vuông góc với cạnh, xuất phát từ 1 điểm trên cạnh
- Hai mặt phẳng vuông góc: góc nhị diện = 90°
- Dấu hiệu: (P) chứa đường thẳng a vuông góc với (Q) → (P) vuông góc (Q)

#### Khoảng cách

- Khoảng cách từ điểm đến mặt phẳng
- Khoảng cách từ điểm đến đường thẳng
- Khoảng cách giữa đường thẳng và mặt phẳng song song
- Khoảng cách giữa 2 mặt phẳng song song
- Khoảng cách giữa 2 đường thẳng chéo nhau
- Ví dụ: Cho hình lập phương ABCD.A'B'C'D' cạnh a. Tính khoảng cách từ A đến mp (BDC').
