# Khảo sát Toán 11

---

## Đại số & Giải tích

### Hàm số lượng giác và phương trình lượng giác

#### Góc lượng giác và đơn vị radian

- Góc lượng giác: góc có hướng quay (dương: ngược chiều kim đồng hồ; âm: cùng chiều)
- Đơn vị radian: 1 rad = góc ở tâm chắn cung có độ dài bằng bán kính
- Đổi đơn vị: 180° = pi rad; 1rad = 1/180°
  - Từ độ sang radian: alpha(rad) = alpha(°) x pi / 180
  - Từ radian sang độ: alpha(°) = alpha(rad) x 180 / pi
- Ví dụ: 60° = pi/3 rad; 90° = pi/2 rad; 45° = pi/4 rad.
- Hỏi: 1 rad bằng khoảng bao nhiêu độ? (≈ 57,3°)
- Độ dài cung tròn: l = r.alpha, với alpha đơn vị radian
- Đường tròn lượng giác có tâm là 0 và bán kính r = 1 

Dạng 1. Mối liên hệ giữa độ và rađian
Dạng 2. Độ dài cung lượng giác
Dạng 3. Biểu diễn góc lượng giác trên đường tròn lượng giác

#### Giá trị lượng giác (mở rộng)

- Đường tròn lượng giác: điểm M(cos(alpha); sin(alpha)) trên đường tròn đơn vị, bán kính bằng 1
- Dấu của sin, cos, tan, cot theo từng góc phần tư:
  - Góc phần tư I: sin > 0, cos > 0
  - Góc phần tư II: sin > 0, cos < 0
  - Góc phần tư III: sin < 0, cos < 0
  - Góc phần tư IV: sin < 0, cos > 0
- Công thức lượng giác cơ bản:
  - sin^2(a) + cos^2(a) = 1
  - tan(a) = sin(a) / cos(a); cot(a) = cos(a) / sin(a) = 1 / tan(a); tan(a).cot(a) = 1
  - 1 + tan^2(a) = 1 / cos^2(a); 1 + cot^2(a) = 1 / sin^2(a)
- Các góc liên quan đặc biệt
  - Đối nhau (cos - đối): cos(-a) = cos(a), sin(-a) = -sin(a), tan(-a) = -tan(a), cot(-a) = -cot(a)
  - Bù nhau (sin - bù): sin(pi - a) = sin(a), cos(pi - a) = -cos(a), tan(pi - a) = -tan(a), cot(pi - a) = -cot(a)
  - Phụ nhau (phụ - chéo): sin(pi/2 - a) = cos(a), cos(pi/2 - a) = sin(a), tan(pi/2 - a) = cot(a), cot(pi/2 - a) = tan(a)
  - Hơn kém pi: sin(pi + a) = -sin(a), cos(pi + a) = -cos(a), tan(pi + a) = tan(a), cot(pi + a) = cot(a)
  - Hơn kém pi/2: sin(pi/2 + a) = cos(a), cos(pi/2 + a) = -sin(a), tan(pi/2 + a) = -cot(a), cot(pi/2 + a) = -tan(a)

Dạng 1. Tính giá trị lượng giác của 1 góc lượng giác
Dạng 2. Tính giá trị lượng giác liên quan góc đặc biệt
Dạng 3. Rút gọn biểu thức lượng giác
Dạng 4. Giá trị lớn nhất – giá trị nhỏ nhất

#### Công thức lượng giác

- Công thức cộng:
  - sin(a + b) = sin(a).cos(b) + cos(a).sin(b)
  - sin(a - b) = sin(a).cos(b) - cos(a).sin(b)
  - cos(a + b) = cos(a).cos(b) - sin(a).sin(b)
  - cos(a - b) = cos(a).cos(b) + sin(a).sin(b)
  - tan(a + b) = (tan(a) + tan(b))/(1 - tan(a).tan(b))
  - tan(a - b) = (tan(a) - tan(b))/(1 + tan(a).tan(b))
- Công thức nhân đôi:
  - sin(2a) = 2.sin(a).cos(a)
  - cos(2a) = cos^2(a) - sin^2(a) = 2cos^2(a) - 1 = 1 - 2sin^2(a)
  - tan(2a) = 2.tan(a)/(1 - tan^2(a))
- Công thức hạ bậc:
  - sin^2(a) = (1 - cos(2a)) / 2
  - cos^2(a) = (1 + cos(2a)) / 2
- Công thức biến đổi tích thành tổng 
  - cos(a).cos(b) = 1/2.[cos(a - b) + cos(a + b)]
  - sin(a).sin(b) = 1/2.[cos(a - b) - cos(a + b)]
  - sin(a).cos(b) = 1/2.[sin(a - b) + sin(a + b)]
- Công thức biến đổi tổng thành tích
  - cos(a) + cos(b) = 2.cos((a + b)/2).cos((a - b)/2)
  - cos(a) - cos(b) = -2.sin((a + b)/2).sin((a - b)/2)
  - sin(a) + sin(b) = 2.sin((a + b)/2).cos((a - b)/2)
  - sin(a) - sin(b) = 2.cos((a + b)/2).sin((a - b)/2)

Dạng 1. Công thức cộng
Dạng 2. Công thức nhân đôi
Dạng 3. Công thức biến đổi tích thành tổng
Dạng 4. Công thức biến đổi tổng thành tích

#### Hàm số lượng giác

- Hàm chẵn: f(-x) = f(x)
- Hàm lẻ: f(-x) = -f(x)
- Hàm số tuần hoàn: f(x + T) = f(x), T gọi là chu kỳ
- Hàm số sin: y = sin(x): TXĐ = R, giá trị thuộc [-1; 1], hàm lẻ và tuần hoàn với chu kỳ 2pi
- Hàm số cos: y = cos(x): TXĐ = R, giá trị thuộc [-1; 1], hàm chẵn và tuần hoàn với chu kỳ 2pi
- Hàm số tan: y = tan(x): TXĐ: x ≠ pi/2 + k.pi, hàm lẻ và tuần hoàn với chu kỳ pi
- Hàm số cot:y = cot(x): TXĐ: x ≠ k.pi, hàm lẻ với chu kỳ pi
- Hỏi: Đồ thị y = sin(x) và y = cos(x) khác nhau thế nào? (dịch pha pi/2)

Dạng 1. Tập xác định
Dạng 2. Tính chẵn - lẻ
Dạng 3. Tính tuần hoàn
Dạng 4. Giá trị lớn nhất - nhỏ nhất

#### Phương trình lượng giác cơ bản

- sin(x) = m (|m| <= 1): x = alpha + k.2pi hoặc x = pi - alpha + k.2pi (với alpha = arcsin(x), alpha thuộc [-pi/2; pi/2])
- cos(x) = m (|m| <= 1): x = alpha + k.2pi hoặc x = -alpha + k.2pi (với alpha = arccos(x), alpha thuộc [0; pi])
- tan(x) = m: x = alpha + k.pi (với alpha = arctan(x), alpha thuộc [-pi/2; pi/2])
- cot(x) = m: x = alpha + k.pi (với alpha = arccot(x), alpha thuộc [0; pi])
- Trong đó k là số nguyên (k thuộc Z).
- Ví dụ: Giải sin(x) = 1/2. Giải cos(2x) = 0.
- Phương trình dạng a.sin(x) + b.cos(x) = c:
  - Có nghiệm khi a^2 + b^2 >= c^2
  - Chia 2 vế cho sqrt(a^2 + b^2)
  - Đặt cos(alpha) = a/sqrt(a^2 + b^2), sin(alpha) = b/sqrt(a^2 + b^2)
  - Phương trình trở thành: sin(x).cos(alpha) + cos(x).sin(alpha) = c/sqrt(a^2 + b^2) = sin(x + alpha)
  - Đưa con số c/sqrt(a^2 + b^2) sang sin(beta) => x + alpha = beta + k.2pi hoặc x + alpha = pi - beta + k.2pi

Dạng 1. Phương trình sinx = a
Dạng 2. Phương trình cosx = a
Dạng 3. Phương trình tanx = a và cotx = a
Dạng 4. Phương trình có nghiệm thuộc khoảng – đoạn
Dạng 5. Bài toán thực tế liên quan phương trình lượng giác

### Dãy số

#### Dãy số, dãy số bị chặn, dãy đơn điệu

- Dãy số: hàm số u(n) với n là số tự nhiên
- Dãy tăng: u(n+1) > u(n), mọi n; dãy giảm: u(n+1) < u(n), mọi n
- Dãy bị chặn trên: tồn tại M, u(n) <= M, mọi n; Dãy bị chặn dưới: tồn tại m, u(n) >= m, mọi n; Dãy bị chặn nếu bị chặn trên và dưới
- Ví dụ: Dãy un = 2n + 1 tăng hay giảm?

DẠNG 1: BIỂU DIỄN DÃY SỐ, TÌM CÔNG THỨC TỔNG QUÁT
DẠNG 2: TÌM SỐ HẠNG CỦA DÃY SỐ
DẠNG 3: XÉT TÍNH TĂNG, GIẢM CỦA DÃY SỐ
DẠNG 4: XÉT TÍNH BỊ CHẶN CỦA DÃY SỐ
DẠNG 5: TÍNH TỔNG CỦA DÃY SỐ
- Tính tổng của dãy số cách đều
- Tính tổng của dãy số bằng phương pháp khử liên tiếp
- Tính tổng bằng cách chuyển về phương trình có ẩn là tổng cần tính
- Tính tổng bằng cách đưa về các tổng đã biết
DẠNG 6: XÁC ĐỊNH CÔNG THỨC SỐ HẠNG TỔNG QUÁT CỦA DÃY SỐ

#### Cấp số cộng

- Dãy (un) là cấp số cộng nếu u(n+1) - u(n) = d (không đổi, d gọi là công sai)
- Dãy tăng: d > 0, dãy giảm: d < 0
- Số hạng tổng quát: u(n) = u(1) + (n - 1) x d
  - d = (u(p) - u(q)) / (p - q)
  - u(1) = u(p) - (p - 1) d
  - u(p) = (u(p + 1) + u(p - 1)) / 2
- Tổng n số hạng đầu: S(n) = n . (u(1) + u(n)) / 2 = n . (2u(1) + (n-1)d) / 2 = n.u(1) + (n.(n - 1).d) / 2
- Ví dụ: CSC có u1 = 3, d = 5. Tìm u10 và S10.

DẠNG 1: NHẬN DIỆN CẤP SỐ CỘNG
DẠNG 2: TÌM CÔNG THỨC CỦA CẤP SỐ CỘNG
DẠNG 4: TÌM HẠNG TỬ TRONG CẤP SỐ CỘNG
DẠNG 3: TÍNH TỔNG VÀ MỘT SỐ BÀI TOÁN LIÊN QUAN
Dạng 5: Chứng minh một dãy là cấp số cộng.
Dạng 6: Xác định các đại lượng của cấp số cộng
Dạng 7: Tổng n số hạng đầu tiên của cấp số cộng

#### Cấp số nhân

- Dãy u(n) là cấp số nhân nếu u(n+1) / u(n) = q (không đổi, q gọi là công bội, q ≠ 0)
- Số hạng tổng quát: u(n) = u(1) . q^(n-1)
- Tổng n số hạng đầu: S(n) = u(1) . (1 - q^n) / (1 - q) (khi q ≠ 1)
- Tính chất: u(k)^2 = u(k-1) . u(k+1)
- Ví dụ: CSN có u1 = 2, q = 3. Tìm u5 và S5.
- Hỏi: Lãi suất đơn/kép (tiền gửi ngân hàng) liên quan đến CSC hay CSN?

DẠNG 1: NHẬN DIỆN CẤP SỐ NHÂN
DẠNG 2: TÌM CÔNG THỨC CỦA CẤP SỐ NHÂN
DẠNG 3: TÌM HẠNG TỬ TRONG CẤP SỐ NHÂN
DẠNG 4: TÍNH TỔNG VÀ MỘT SỐ BÀI TOÁN LIÊN QUAN
Dạng 5: Chứng minh một dãy là cấp số nhân.
Dạng 6: Xác định các đại lượng của cấp số nhân
Dạng 7: Tổng n số hạng đầu tiên của cấp số nhân

### Giới hạn

#### Giới hạn của dãy số

- Dãy (un) có giới hạn L: khi n tiến tới vô cùng, un tiến về L; ký hiệu lim(un) = L
- Các giới hạn cơ bản:
  - lim(c) = c (c là hằng số)
  - lim n^k = + vô cùng (k > 0)
  - lim(1/n) = 0
  - lim(1/n^k) = 0 (k > 0)
  - lim(q^n) = 0 nếu |q| < 1
  - lim(q^n) = + vô cùng nếu q > 1
  - |u(n)| <= |v(n)| và lim(v(n)) = 0 => lim(u(n)) = 0
  - Nếu lim(u(n)) = a, lim(v(n)) = -/+ vô cùng => lim(u(n) / v(n)) = 0
  - Nếu lim(u(n)) = a > 0, lim(v(n)) = 0 => lim(u(n) / v(n)) = + vô cùng
  - Nếu lim(u(n)) = a > 0, lim(v(n)) = + vô cùng => lim(u(n) . v(n)) = + vô cùng
- Dãy phân kỳ: không có giới hạn hữu hạn
- Giới hạn vô cực: lim(un) = +vô cực hoặc -vô cực
- Quy tắc tính: 
 - lim(un + vn) = lim(un) + lim(vn); lim(un x vn) = lim(un) x lim(vn)
 - lim(k.u(n)) = k.lim(u(n))
 - lim(|u(n)|) = |lim(u(n))|
- Định lý kẹp: Nếu u(n) < v(n) < w(n) và lim(u(n)) = lim(w(n)) = a thì lim(v(n)) = a
- Dạng vô định:
  - Vô cực / vô cực → chia cho lũy thừa cao nhất
  - 0 / 0 -> Phân tích tử và mẫu thành nhân tử chung và rút gọn
  - Vô cực - vô cực -> Nhân lượng liên hợp để chuyển sang dạng phân thức 0/0 hoặc vô cực / vô cực
  - 0 . vô cực -> Chuyển sang dạng 0 / 0 hoặc vô cực / vô cực
  - 1^ vô cực, 0^0, vô cùng ^ 0
- Quy tắc L'Hospital: đạo hàm nhiều lần tử và mẫu để khử dạng 0/0 và vô cùng / vô cùng
- Ví dụ: lim((3n^2 + 1) / (n^2 - 2)) = ?
- Cấp số nhân lùi vô hạn: Vì |q| < 1 nên lim q^n = 0 => S = u1 / (1 - q)

DẠNG 1: CHỨNG MINH DÃY SỐ CÓ GIỚI HẠN 0
DẠNG 2: TÌM GIỚI HẠN BẰNG 0 CỦA DÃY SỐ
DẠNG 3: TÍNH GIỚI HẠN CỦA DÃY SỐ u(n) = P(n)/Q(n)
DẠNG 4: NHÂN VỚI MỘT LƯỢNG LIÊN HỢP
DẠNG 5: Dãy số (un) trong đó u(n) là một tổng hoặc một tích của n số hạng (hoặc n thừa số)
DẠNG 6: (un) cho bằng công thức truy hồi
DẠNG 7: GIỚI HẠN CỦA DÃY CHỨA ĐA THỨC HOẶC CĂN THEO n
DẠNG 8: GIỚI HẠN CỦA DÃY CHỨA LŨY THỪA BẬC n
DẠNG 9:. DÃY SỐ DẠNG PHÂN THỨC
- Phân thức bậc tử bé hơn bậc mẫu
- Phân thức bậc tử bằng bậc mẫu
- Phân thức bậc tử lớn hơn bậc mẫu
- Phân thức chứa căn
DẠNG 10: DÃY SỐ CHỨA CĂN THỨC
DẠNG 11: DÃY SỐ CHỨA LŨY THỪA
DẠNG 12: TỔNG CẤP SỐ NHÂN LÙI VÔ HẠNG
DẠNG 13: MỘT SỐ BÀI TOÁN KHÁC

#### Giới hạn của hàm số

- lim f(x) khi x tiến đến a: giá trị mà f(x) tiến về khi x gần a (x ≠ a)
- Giới hạn một bên:
  - Giới hạn bên trái: x0 > x
  - Giới hạn bên phải: x0 < x
  - lim f(x) = L khi x dần tới x0 thì lim f(x) = 0 khi x dần tới x+ hoặc x dần tới x-
- Giới hạn tại vô cực: lim f(x) khi x tiến đến +vô cực hoặc -vô cực
- Tiệm cận ngang: y = L nếu lim f(x) = L khi x tiến đến vô cực
- Tiệm cận đứng: x = a nếu lim f(x) = vô cực khi x tiến đến a
- Cho lim f(x) = L, lim g(x) = M khi x dần tới x0
  - lim (f(x) + g(x)) = L + M khi x dần tới x0
  - lim (f(x) . g(x)) = L . M khi x dần tới x0
  - Nếu f(x) >= 0 thì L >=0
- Đặc biệt: lim x = x0 và lim c = c khi x dần tới x0
- Nguyên lý kẹp: f(x) < g(x) < h(x) => lim f(x) = lim h(x) = L thì lim g(x) = L
- Ví dụ: lim((x^2 - 1) / (x - 1)) khi x tiến đến 1 = ?

DẠNG 1. HÀM SỐ CÓ GIỚI HẠN HỮU HẠN TẠI x0 KHÔNG CÓ DẠNG VÔ ĐỊNH
DẠNG 2. DẠNG VÔ ĐỊNH 0/0
DẠNG 3. DẠNG VÔ ĐỊNH ∞ / ∞
DẠNG 4. DẠNG VÔ ĐỊNH ∞ − ∞
DẠNG 5. DẠNG VÔ ĐỊNH 0 . ∞
DẠNG 6. GIỚI HẠN HỮU HẠN
DẠNG 7: GIỚI HẠN MỘT BÊN
DẠNG 8: GIỚI HẠN VÔ CỰC
DẠNG 9: LIÊN QUAN ĐẾN HÀM ẨN

#### Hàm số liên tục

- f(x) liên tục tại x = x0 nếu: lim f(x) = f(a) khi x tiến đến x0
- Hàm số không liên tục tại x0 gọi là gián đoạn tại x0
- Hàm số liên tục trên (a; b) nếu nó liên tục trên mọi điểm trong khoảng đó
- Hàm số liên tục trên [a; b] nếu nó liên tục trên (a; b) và tại 2 đầu mút
- Hỏi: Hàm y = 1/x có liên tục tại x = 0 không?
- Tính chất: giả sử f(x) và g(x) liên tục tại x0
  - f(x) +/- g(x) và f(x) . g(x) liên tục tại x0
  - f(x) / g(x) lien tục tại x0 nếu g(x) khác 0
- Hàm số f(x) liên tục trên [a; b] và f(a).f(b) < 0 thì tồn tại ít nhất một điểm c thuộc (a, b) sao cho f(c) = 0

DẠNG 1: HÀM SỐ LIÊN TỤC TẠI MỘT ĐIỂM
- Xét tính liên tục tại điểm của hàm số
- Điểm gián đoạn của hàm số
- Bài toán chứa tham số
DẠNG 2: HÀM SỐ LIÊN TỤC TRÊN MỘT KHOẢNG
- Xét tính liên tục trên khoảng của hàm số
- Bài toán chứa tham số
DẠNG 3: CHỨNG MINH PHƯƠNG TRÌNH CÓ NGHIỆM

### Hàm số mũ và hàm số logarit

#### Lũy thừa (mở rộng)

- Lũy thừa a^n = a.a....a (n thừa số a). a là cơ số, n là mũ số
- Lũy thừa với số mũ nguyên âm: a^(-n) = 1 / a^n (a ≠ 0)
- Lũy thừa với số mũ hữu tỉ: a^(m/n) = căn bậc n của a^m (a > 0)
- Tính chất lũy thừa (mở rộng cho số mũ thực):
  - a^x x a^y = a^(x+y)
  - a^x / a^y = a^(x-y)
  - (a^x)^y = a^(xy)
  - (a x b)^x = a^x x b^x
- Nếu a > 1 thì a^n > a^m khi n > m
- Nếu 0 < a < 1 thì a^n > a^m khi n < m

Dạng 1: Tính giá trị của biểu thức
DẠNG 2: BIẾN ĐỔI, RÚT GỌN, BIỂU DIỄN CÁC BIỂU THỨC 
DẠNG 3: BÀI TOÁN LÃI SUẤT KÉP – DÂN SỐ

#### Logarit

- log_a(b) = c nghĩa là a^c = b (a > 0, a ≠ 1, b > 0)
- Logarit tự nhiên: ln(x) = log_e(x) (e ≈ 2,718)
- Logarit thập phân: lg(x) = log_10(x)
- Tính chất:
  - log_a(1) = 0; log_a(a) = 1
  - log_a(xy) = log_a(x) + log_a(y)
  - log_a(x/y) = log_a(x) - log_a(y)
  - log_a(x^n) = n x log_a(x)
  - Đổi cơ số: log_a(b) = log_c(b) / log_c(a)
  - log_a(b) = 1 / log_b(a)
- Ví dụ: log_2(8) = ?, log_3(1/9) = ?, lg(1000) = ?

#### Hàm số mũ

- y = a^x (a > 0, a ≠ 1)
- a > 1: hàm đồng biến; 0 < a < 1: hàm nghịch biến
- Đồ thị luôn qua điểm (0; 1)
- TXĐ: R; tập giá trị: (0; +vô cực)

#### Hàm số logarit

- y = log_a(x) (a > 0, a ≠ 1)
- TXĐ: (0; +vô cực); tập giá trị: R
- a > 1: đồng biến; 0 < a < 1: nghịch biến
- Đồ thị luôn qua điểm (1; 0)
- y = log_a(x) là hàm ngược của y = a^x

DẠNG 1: TÌM TẬP XÁC ĐỊNH CỦA HÀM SỐ MŨ – LOGARIT
DẠNG 2: ĐỒ THỊ
DẠNG 3: BÀI TOÁN LÃI SUẤT KÉP

#### Phương trình, bất phương trình mũ và logarit

- Phương trình mũ cơ bản: a^x = b → x = log_a(b)
- Phương trình logarit cơ bản: log_a(x) = b → x = a^b
- Điều kiện: biểu thức trong logarit phải > 0
- Bất phương trình: chú ý chiều bất đẳng thức phụ thuộc cơ số a > 1 hay 0 < a < 1
- Ví dụ: Giải 2^x = 16. Giải log_2(x - 1) = 3.
- Ví dụ: Giải 3^(2x-1) > 27.

DẠNG 1: PHƯƠNG TRÌNH MŨ
DẠNG 2: PHƯƠNG TRÌNH LOGARIT
DẠNG 3: BẤT PHƯƠNG TRÌNH MŨ
DẠNG 4: BẤT PHƯƠNG TRÌNH LOGARIT

### Đạo hàm

- Đạo hàm của f(x) tại x0: nếu tồn tại x0 sao cho tồn tại giới hạn hữu hạn lim((f(x0 + h) - f(x0)) / h) khi h tiến đến 0. Khi đó: f'(x0) = lim((f(x0 + h) - f(x0)) / h) khi h tiến đến 0
- Hàm số f(x) có đạo hàm trên (a; b) nếu nó có đạo hàm tại mọi điểm thuộc (a; b)
- Ý nghĩa hình học: f'(x0) là hệ số góc của tiếp tuyến với đồ thị tại điểm (x0; f(x0))
- Phương trình tiếp tuyến tại M(x0; y0): y - y0 = f'(x0) x (x - x0) với y0 = f(x0)
- Ý nghĩa vật lý: vận tốc tức thời v(t) = s'(t)
- Đạo hàm cơ bản
  - (c)' = 0
  - (x^n)' = n x x^(n-1)
  - (sin(x))' = cos(x)
  - (cos(x))' = -sin(x)
  - (tan(x))' = 1 / cos^2(x)
  - (cot(x))' = -1 / sin^2(x)
- Quy tắc tính đạo hàm
  - (u + v)' = u' + v'
  - (u - v)' = u' - v'
  - (u x v)' = u' x v + u x v'
  - (k.u)' = k.u'
  - (u / v)' = (u' x v - u x v') / v^2
  - (1/v)' = -v'/v^2
- Đạo hàm hàm hợp: (f(u))' = f'(u) x u'
- Ví dụ: Tính đạo hàm y = x^3 - 3x^2 + 2. Tính đạo hàm y = sin(2x + 1).
- Ví dụ: Viết phương trình tiếp tuyến của y = x^2 - 4x + 3 tại x = 1.
- Hàm mũ:
  - (e^x)' = e^x
  - (a^x)' = a^x . ln(a)
- Hàm logaric:
  - ln(x)' = 1/x
  - log_a(x)' = 1/(x.ln(a))
- Đạo hàm cấp 2: Nếu f'(x) có đạo hàm tại x0 thì đạo hàm f''(x) gọi là đạo hàm cấp 2
- Ý nghĩa vật lý: gia tốc tức thời a(t) = s''(t)

DẠNG 1: TÍNH ĐẠO HÀM TẠI MỘT ĐIỂM
DẠNG 2: ĐẠO HÀM CỦA HÀM SỐ TRÊN 1 KHOẢNG
DẠNG 3: Ý NGHĨA CỦA ĐẠO HÀM
DẠNG 4: TÍNH ĐẠO HÀM TẠI ĐIỂM
DẠNG 5: TÍNH ĐẠO HÀM CỦA MỘT SỐ HÀM SỐ THƯỜNG GẶP
DẠNG 6: BÀI TOÁN TIẾP TUYẾN
DẠNG 7: TÍNH ĐẠO HÀM CỦA HÀM SỐ MŨ
DẠNG 8: TÍNH ĐẠO HÀM CỦA HÀM SỐ LOGARIT
DẠNG 9: TÍNH ĐẠO HÀM CẤP HAI
DẠNG 10: GIA TỐC

### Mẫu số liệu ghép nhóm

- Mẫu số liệu ghép nhóm: là mẫu số liệu cho dưới dạng bảng tần số của các nhóm số liệu. Mỗi nhóm số liệu là tập hợp gồm các giá trị của số liệu được ghép nhóm theo một tiêu chí xác định.
- Ghép nhóm mẫu số liệu
  1. Chia miền giá trị của mẫu số liệu thành một số nhóm theo tiêu chí cho trước.
  2. Đếm số giá trị của mẫu số liệu thuộc mỗi nhóm (tần số) và lập bảng thống kê cho mẫu số liệu ghép nhóm.
- Số trung bình của mẫu số liệu ghép nhóm: x ngang = (m1.x1 + m2.x2 + ... mn.xn)/n
  - n = m1 + m2 + ... + mn là cỡ mẫu
  - xi = (a(i) + a(i + 1)) / 2
- Trung vị của mẫu số liệu ghép nhóm:
  1. Xác định nhóm chứa trung vị. GS nhóm thứ p: [a(p), a(p + 1))
  2. Trung vị: M(e) = a(p) + (n/2 - (m1 + m2 + ... + m(n))) / m(p) . (a(p + 1) - a(p))
    - n là cỡ mẫu
    - m(p) là tần số nhóm p
    - Với p = 1, ta quy ước m1 + m2 + ... + m(p - 1) = 0
- Tứ phân vị của mẫu số liệu ghép nhóm:
  - Tứ phân vị thứ nhất Q1
    1. Xác định nhóm chứa Q1. GS nhóm thứ p: [a(p), a(p + 1))
    2. Q1 = a(p) + (n/4 - (m1 + m2 + ... + m(p - 1))) / m(p) . (a(p + 1) - a(p))
      - n là cỡ mẫu
      - m(p) là tần số nhóm p
      - Với p = 1, ta quy ước m1 + m2 + ... + m(p - 1) = 0
  - Tứ phân vị thứ hai Q2 = M(e)
  - Tứ phân vị thứ ba Q3
    1. Xác định nhóm chứa Q1. GS nhóm thứ p: [a(p), a(p + 1))
    2. Q3 = a(p) + (3n/4 - (m1 + m2 + ... + m(p - 1))) / m(p) . (a(p + 1) - a(p))
      - n là cỡ mẫu
      - m(p) là tần số nhóm p
      - Với p = 1, ta quy ước m1 + m2 + ... + m(p - 1) = 0
- Mốt của mẫu số liệu ghép nhóm:
  1. Xác định nhóm có tần số lớn nhất
  2. Mốt: M(0) = a(j) + (m(j) - m(j - 1)) / ((m(j) - m(j - 1)) + (m(j) - m(j + 1))) . h
    - m(j) là tần số của nhóm j, quy ước m(0) = m(k + 1) = 0
    - h là độ dài của nhóm

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
  - Qua 3 điểm không thẳng hàng xác định duy nhất 1 mặt phẳng
  - Nếu đường thẳng có 2 điểm thuộc mặt phẳng thì nằm trọn trong mặt phẳng
  - Hai mặt phẳng có 1 điểm chung thì có chung 1 đường thẳng (giao tuyến)
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
  - b vuông góc b' ↔ b vuông góc hình chiếu

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
