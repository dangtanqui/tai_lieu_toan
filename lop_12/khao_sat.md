# Khảo sát Toán 12

---

## Đại số & Giải tích

### Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số

#### Tính đơn điệu của hàm số

- Hàm số y = f(x) gọi là đồng biến trên K nếu ∀ x1, x2 ∈ K, x1 < x2 ⇒ f(x1) < f(x2).
- Hàm số y = f(x) gọi là nghịch biến trên K nếu ∀ x1, x2 ∈ K, x1 < x2 ⇒ f(x1) > f(x2).
- Hàm số đồng biến hoặc nghịch biến gọi là đơn điệu.
- f'(x) > 0 trên khoảng (a; b) → f(x) đồng biến trên (a; b)
- f'(x) < 0 trên khoảng (a; b) → f(x) nghịch biến trên (a; b)
- Cách xét:
 - Tìm TXĐ
 - Tính f'(x), tìm xi mà f'(x) = 0 hoặc không xác định
 - Lập bảng biến thiên
- Ví dụ: Xét sự đồng biến, nghịch biến của y = x^3 - 3x + 2.

#### Cực trị của hàm số

- Tồn tại h > 0 sao cho f(x) < f(x0) với mọi x thuộc (x0 - h; x0 + h) và x khác x0 thì f(x) đạt cực đại tại x0.
- Tồn tại h > 0 sao cho f(x) > f(x0) với mọi x thuộc (x0 - h; x0 + h) và x khác x0 thì f(x) đạt cực tiểu tại x0.
- Các điểm cực đại và cực tiểu gọi là cực trị.
- Điểm cực đại: f'(x) đổi dấu từ + sang - khi x qua x0 → x0 là cực đại
- Điểm cực tiểu: f'(x) đổi dấu từ - sang + khi x qua x0 → x0 là cực tiểu
- Quy tắc 2 (dùng đạo hàm cấp hai): vì f'' thể hiện độ cong (f'' > 0 lỗi, f'' < 0 lõm)
  - Với f'(x0) = 0 và f''(x0) < 0 → cực đại
  - Với f'(x0) = 0 và f''(x0) > 0 → cực tiểu
- Cách tìm:
 - Tìm TXĐ
 - Tính f'(x), tìm x0 mà f'(x) = 0 hoặc không xác định
 - Lập bảng biến thiên hoặc tìm f''(x0)

DẠNG 1: XÉT TÍNH ĐƠN ĐIỆU CỦA HÀM SỐ CHO BỞI BIỂU THỨC
DẠNG 2: XÉT TÍNH ĐƠN ĐIỆU CỦA HÀM HỢP CHO BỞI BBT HOẶC ĐỒ THỊ CỦA HÀM SỐ y = f(x) HOẶC y = f′(x).
DẠNG 3: TÌM ĐK CỦA THAM SỐ ĐỂ HÀM SỐ ĐỒNG BIẾN, NGHỊCH BIẾN TRÊN MỘT MIỀN CHO TRƯỚC.
DẠNG 4: TÌM CỰC TRỊ CỦA HÀM SỐ CHO BỞI BIỂU THỨC.
DẠNG 5: RIÊNG VỀ CỰC TRỊ HÀM BẬC 3
DẠNG 6: RIÊNG VỀ CỰC TRỊ HÀM TRÙNG PHƯƠNG
DẠNG 7: CỰC TRỊ CỦA HÀM y = |f(x)|, y = f(|x|)
DẠNG 8: TÌM CỰC TRỊ CỦA HÀM SỐ KHI BIẾT BIỂU THỨC f(x), f'(x)
DẠNG 9: TÌM M ĐỂ HÀM SỐ ĐẠT CỰC TRỊ TẠI x = x0
- Tính f'(x0) = 0, tìm m
- Thế m vào f''(x0) nếu f''(x0) < 0 cực tiểu, f''(x0) < 0 cực đại
DẠNG 10: HÀM SỐ ĐA THỨC BẬC CAO, HÀM CĂN THỨC
DẠNG 11: TÌM M ĐỂ HÀM SỐ CÓ N CỰC TRỊ
- f'(x) có n nghiệm phân biệt
DẠNG 12: ĐƯỜNG THẲNG ĐI QUA 2 ĐIỂM CỰC TRỊ
- Thực hiện phép chia y cho y', phân tích ra: y = y'. q(x) + h(x)
- y0 = h(x0) vì y' tại x0 = 0
- (d): y = h(x)
DẠNG 13: TÌM M ĐỂ HÀM SỐ BẬC 3 CÓ CỰC TRỊ THỎA MÃN ĐIỀU KIỆN CHO TRƯỚC
DẠNG 14: TÌM M ĐỂ HÀM SỐ TRÙNG PHƯƠNG CÓ CỰC TRỊ THỎA MÃN ĐIỀU KIỆN CHO TRƯỚC
DẠNG 15: TÌM M ĐỂ HÀM SỐ BẬC 2 TRÊN BẬC 1 CÓ CỰC TRỊ THỎA MÃN ĐIỀU KIỆN CHO TRƯỚC
DẠNG 16: BÀI TOÁN CỰC TRỊ HÀM SỐ CHỨA DẤU TRỊ TUYỆT ĐỐI
- y = |f(x)| => y = sqrt(f^2(x))
- y' = 2.f(x).f'(x)/sqrt(f^2(x)) = 0 => f(x) = 0 hoặc f'(x) = 0
DẠNG 17: SỐ ĐIỂM CỰC TRỊ CỦA HÀM HỢP
- y = f(g(x)) => y' = g'(x).f'(g(x)) = 0 => g'(x) = 0 hoặc f'(g(x)) = 0
DẠNG 18: TÌM M ĐỂ HÀM SỐ f(g(x)) THỎA MÃN ĐIỀU KIỆN CHO TRƯỚC
DẠNG 19: TÌM CỰC TRỊ CỦA HÀM SỐ HỢP f(g(x)) HOẶC f(g(x)) + h(x) KHI BIẾT ĐỒ THỊ HÀM SỐ f(x) HOẶC f'(x) 

#### Giá trị lớn nhất, nhỏ nhất

- Trên đoạn [a; b]: so sánh f(a), f(b) và các giá trị f(x) tại điểm cực trị bên trong
- GTLN = max; GTNN = min trong các giá trị đó
- Ví dụ: Tìm GTLN, GTNN của y = x^3 - 3x trên [-2; 2].
- Lập bảng biến thiên
- Hoặc tìm x0 trên đoạn với tính f' = 0 hoặc không tồn tại, tính f(x0), f(a), f(b) và tìm max, min

DẠNG 1. TÌM MAX-MIN TRÊN ĐOẠN BẰNG HÀM SỐ CỤ THỂ, BẢNG BIẾN THIÊN, ĐỒ THỊ HÀM SỐ CHO TRÊN ĐOẠN VÀ KHOẢNG.
DẠNG 2: TÌM MAX- MIN BẰNG PHƯƠNG PHÁP ĐỔI BIẾN
DẠNG 3: MỘT SỐ BÀI TOÁN CÓ CHỨA THAM SỐ m
DẠNG 4: PHƯƠNG PHÁP ĐẶT ẨN PHỤ ĐỂ GIẢI QUYẾT BÀI TOÁN TÌM ĐIỀU KIỆN CỦA THAM SỐ m SAO CHO PHƯƠNG TRÌNH f(x, m) = 0 CÓ NGHIỆM (CÓ ỨNG DỤNG GTLN, GTNN )
DẠNG 5: PHƯƠNG PHÁP ĐẶT ẨN PHỤ ĐỂ GIẢI QUYẾT BÀI TOÁN TÌM ĐIỀU KIỆN CỦA THAM SỐ m ĐỂ BẤT PHƯƠNG TRÌNH CÓ NGHIỆM HOẶC NGHIỆM ĐÚNG VỚI MỌI x ∈ K (CÓ ỨNG DỤNG GTLN, GTNN)
DẠNG 6: BÀI TOÁN THỰC TẾ
- Bất đẳng thức AM - GM (cô-si): a + b >= 2.sqrt(a.b) xảy ra dấu = khi a = b
- Bất đẳng thức Bunhiacopxki: |a.x + b.y| <= sqrt((a^2 + b^2) . (x^2 + y^2)) xảy ra dấu = khi a.y = b.x
DẠNG 7: XÁC ĐỊNH GIÁ TRỊ LỚN NHẤT – GIÁ TRỊ NHỎ NHẤT CỦA HÀM SỐ THÔNG QUA ĐỒ THỊ, BẢNG BIẾN THIÊN
DẠNG 8: XÁC ĐỊNH GIÁ TRỊ LỚN NHẤT – GIÁ TRỊ NHỎ NHẤT CỦA HÀM SỐ TRÊN ĐOẠN
DẠNG 9: XÁC ĐỊNH GIÁ TRỊ LỚN NHẤT – GIÁ TRỊ NHỎ NHẤT CỦA HÀM SỐ TRÊN KHOẢNG
- Với 2 đầu mút tính lim x -> a+ và lim x -> b-
DẠNG 10: XÁC ĐỊNH M ĐỂ GTLN-GTNN CỦA HÀM SỐ THỎA MÃN ĐIỀU KIỆN CHO TRƯỚC
DẠNG 11: ĐỊNH M ĐỂ GTLN-GTNN CỦA HÀM SỐ CHỨA DẤU GIÁ TRỊ TUYỆT ĐỐI THỎA MÃN ĐIỀU KIỆN CHO TRƯỚC (khó)
DẠNG 12: GIÁ TRỊ LỚN NHẤT – GIÁ TRỊ NHỎ NHẤT HÀM ẨN, HÀM HỢP
DẠNG 13: ỨNG DỤNG GTLN-GTNN GIẢI BÀI TOÁN THỰC TẾ

#### Đường tiệm cận

- Tiệm cận ngang: y = L nếu lim f(x) = L khi x tiến tới +/- vô cực
- Tiệm cận đứng: x = a nếu lim f(x) = +/- vô cực khi x tiến tới a+/- (a+ đồ thị bên phải, a- đồ thị bên trái)
- Tiệm cận xiên: y = ax + b nếu lim [f(x) - (ax  + b)] = 0 khi x tiến tới +/- vô cực
  - a = lim [f(x) / x]; b = lim[f(x) - ax] khi x tiến tới +/- vô cực
  - Nếu a = 0 thì là tiệm cận ngang y = b
- Hỏi: Hàm y = (2x + 1) / (x - 1) có tiệm cận ngang và tiệm cận đứng nào?
- Hàm y = (ax + b) / (cx + d) có tiệm cận đứng x = -d/c, tiệm cận ngang y = a/c

DẠNG 1: TÌM TIỆM CẬN CỦA ĐỒ THỊ HÀM SỐ CHO BỞI CÔNG THỨC
DẠNG 2: TÌM TIỆM CẬN CỦA ĐỒ THỊ HÀM SỐ BIẾT BBT CỦA HÀM SỐ, ĐỒ THỊ CỦA HÀM SỐ ĐÓ HOẶC HÀM SỐ LIÊN QUAN
DẠNG 3: TIỆM CẬN CỦA ĐỒ THỊ HÀM SỐ HÀM HỢP
DẠNG 4: MỘT SỐ BÀI TOÁN VỀ TIỆM CẬN CHỨA THAM SỐ m
DẠNG 5: XÁC ĐỊNH ĐƯỜNG TIỆM CẬN THÔNG QUA BẢNG BIẾN THIÊN, ĐỒ THỊ
DẠNG 6: XÁC ĐỊNH ĐƯỜNG TIỆM CẬN ĐỒ THỊ HÀM SỐ THÔNG QUA HÀM SỐ CHO TRƯỚC

#### Khảo sát sự biến thiên và vẽ đồ thị hàm số

- Sơ đồ khảo sát hàm số:
  1. Tìm tập xác định
  2. Tính đạo hàm, giải f'(x) = 0 hoặc tìm những điểm đạo hàm không tồn tại
  3. Tìm giới hạn -/+ vô cực, tiệm cận
  4. Lập bảng biến thiên (Xét dấu f', chiều biến thiên)
  5. Tìm các điểm đặc biệt: giao Ox, Oy, điểm đối xứng
  6. Vẽ đồ thị
- Các dạng hàm số thường khảo sát:
  - Hàm bậc ba: y = ax^3 + bx^2 + cx + d
  - Hàm trùng phương: y = ax^4 + bx^2 + c
  - Hàm phân thức bậc nhất / bậc nhất: y = (ax + b) / (cx + d)
  - Hàm phân thức bậc hai / bậc nhất: y = (ax^2 + bx + c) / (px + q)
- Ví dụ: Khảo sát và vẽ đồ thị hàm số y = x^3 - 3x^2 + 2.
- Ứng dụng đồ thị
  - Dùng đồ thị biện luận số nghiệm phương trình f(x) = m
  - Tìm m để phương trình có 1 nghiệm, 2 nghiệm, 3 nghiệm
  - Ví dụ: Dựa vào đồ thị y = x^3 - 3x, tìm m để x^3 - 3x = m có 3 nghiệm phân biệt.

DẠNG 1: NHẬN DẠNG HÀM SỐ THƯỜNG GẶP THÔNG QUA ĐỒ THỊ
- Hàm số bật 3
- Hàm số trùng phương
- Hàm số nhất biến (bật nhất / bật nhất)
DẠNG 2: XÉT DẤU CỦA CÁC HỆ SỐ HÀM SỐ THÔNG QUA ĐỒ THỊ
DẠNG 3: ĐỒ THỊ HÀM SỐ CHỨA DẤU GIÁ TRỊ TUYỆT ĐỐI 
DẠNG 4: BÀI TOÁN TƯƠNG GIAO ĐỒ THỊ THÔNG QUA ĐỒ THỊ, BẢNG BIẾN THIÊN
DẠNG 5: BÀI TOÁN TƯƠNG GIAO ĐỒ THỊ THÔNG QUA HÀM SỐ CHO TRƯỚC
DẠNG 6: BÀI TOÁN TƯƠNG GIAO ĐƯỜNG THẲNG VỚI ĐỒ THỊ HÀM SỐ BẬC 3 
DẠNG 7: BÀI TOÁN TƯƠNG GIAO CỦA ĐƯỜNG THẲNG VỚI ĐỒ THỊ HÀM SỐ NHẤT BIẾN 
DẠNG 8: BÀI TOÁN TƯƠNG GIAO CỦA ĐƯỜNG THẲNG VỚI HÀM SỐ TRÙNG PHƯƠNG 

### Nguyên hàm – Tích phân

#### Nguyên hàm

- F(x) là nguyên hàm của f(x) nếu F'(x) = f(x)
- Nguyên hàm tổng quát: F(x) + C (C là hằng số), ký hiệu: Nguyên hàm f(x)dx
- Bảng nguyên hàm cơ bản:
  - Nguyên hàm của x^n = x^(n+1) / (n+1) + C (n ≠ -1)
  - Nguyên hàm của 1/x = ln|x| + C
  - Nguyên hàm của e^x = e^x + C
  - Nguyên hàm của a^x = a^x / ln(a) + C
  - Nguyên hàm của sin(x) = -cos(x) + C
  - Nguyên hàm của cos(x) = sin(x) + C
  - Nguyên hàm của 1/cos^2(x) = tan(x) + C
  - Nguyên hàm của 1/sin^2(x) = -cot(x) + C
- Tính chất:
  - Nguyên hàm (k.f) = k x nguyên hàm (f)
  - Nguyên hàm (f + g) = nguyên hàm (f) + nguyên hàm (g)
- Ví dụ: Tìm nguyên hàm của f(x) = 3x^2 - 2x + 1.
- Tính chất
  - f(x) liên tục trên K thì có nguyên hàm trên K
  - f(x)dx là vi phân của F(x), ký hiệu dF(x) = F'(x)dx = f(x)dx

#### Tích phân

- Tích phân từ a đến b của f(x)dx = F(b) - F(a) (F là nguyên hàm của f)
- Tính chất:
  - Tích phân từ a đến a = 0
  - Tích phân từ a đến b = - tích phân từ b đến a
  - Tích phân từ a đến b của k.f(x) = k. tích phân từ b đến a của f(x)
  - Tích phân từ a đến b của f(x) + g(x) = tích phân từ b đến a của f(x) + tích phân từ b đến a của g(x)
  - Tích phân từ a đến b = tích phân từ a đến c + tích phân từ c đến b
- Phương pháp tính:
  - Phương pháp đổi biến: đặt u = g(x)
  - Phương pháp tích phân từng phần: tích phân (u.dv) = u.v - tích phân (v.du)
- Ví dụ: Tính tích phân từ 0 đến 2 của (x^2 + 1)dx.

#### Ứng dụng tích phân

- Diện tích hình phẳng:
  - Giới hạn bởi đồ thị y = f(x), trục Ox và x = a, x = b: S = tích phân từ a đến b của |f(x)|dx
  - Giới hạn bởi 2 đồ thị y = f(x) và y = g(x): S = tích phân từ a đến b của |f(x) - g(x)|dx
- Thể tích vật thể: V = tích phân từ a đến b của S(x)dx với S(x) là diện tích mặt phẳng cắt vật thể và vuông góc với Ox
- Thể tích vật thể tròn xoay: V = pi x tích phân từ a đến b của f(x)^2 dx
- Ví dụ: Tính diện tích hình phẳng giới hạn bởi y = x^2 và y = x.

DẠNG 1: ỨNG DỤNG TICH PHAN DỂ TIM DIỆN TICH
DẠNG 2: ỨNG DỤNG TICH PHAN DỂ TIM THỂ TICH

---

## Xác suất có điều kiện

- Cho hai biến cố A và B. Xác suất của A trong điều kiện biết B đã xảy ra: P(A | B) = P(AB) / P(B)
- Nếu A, B độc lập thì P(A | B) = P(A)
- Công thức nhân xác suất: P(AB) = P(B) . P(A | B)
- Xác suất toàn phần: P(B) = P(A) . P(B | A) + P(A') . P(B | A') (A' là biến cố đối của A)
- Công thức Bayes: P(A | B) = P(A) . P(B | A) / P(B)
- Quy tắc:
  - P(A) + P(A') = 1
  - P(A | B) + P(A' | B) = 1
  - P(A giao B) + P(A giao B') = P(A)

DẠNG 1: TÍNH XÁC SUẤT CÓ ĐIỀU KIỆN SỬ DỤNG CÔNG THỨC.
DẠNG 2: TÍNH XÁC SUẤT CÓ ĐIỀU KIỆN SỬ DỤNG SƠ ĐỒ HÌNH CÂY.
DẠNG 3: MÔ TẢ CÔNG THỨC XÁC SUẤT TOÀN PHẦN THÔNG QUA BẢNG DỮ LIỆU THỐNG KÊ 2X2 VÀ SƠ ĐỒ HÌNH CÂY.
DẠNG 4: MÔ TẢ CÔNG THỨC BAYES THÔNG QUA BẢNG DỮ LIỆU THỐNG KÊ 2X2 VÀ SƠ ĐỒ HÌNH CÂY
DẠNG 5: CÔNG THỨC XÁC SUẤT TOÀN PHẦN VÀ CÔNG THỨC BAYES
DẠNG 6: CÁC BÀI TOÁN THỰC TẾ LIÊN QUAN ĐẾN CÔNG THỨC XÁC SUẤT TOÀN PHẦN
DẠNG 7: CÁC BÀI TOÁN THỰC TẾ LIÊN QUAN ĐẾN CÔNG THỨC BAYES.

---

## Hình học

### Vectơ và hệ trục tọa độ trong không gian

#### Vector trong không gian (lớp 10 là 2 chiều)

- Vectơ: đoạn thẳng có hướng, ký hiệu AB (mũi tên từ A đến B)
- Giá của vectơ: đường thẳng chứa vectơ
- Độ dài (mô-đun) của vectơ: |AB|
- Hai vectơ cùng phương: giá song song hoặc trùng nhau, a = kb
  - x2/x1 = y2/y1
- Hai vector cùng phương thì cùng hướng hoặc ngược hướng, a = kb
  - k = x2/x1
  - k > 0: cùng hướng
  - k < 0: ngược hướng
- Hai vectơ bằng nhau: cùng hướng và cùng độ dài, a = b
- Vectơ-không: có điểm đầu trùng điểm cuối, ký hiệu 0 (mũi tên)
- Vectơ đối: cùng độ dài, ngược hướng, a = -b

#### Phép cộng, trừ vectơ

- Quy tắc ba điểm: AB + BC = AC
- Quy tắc hình bình hành: AB + AD = AC (ABCD là hình bình hành)
- Quy tắc hình hộp: AB + AD + AA' = AC' (ABCD.A'B'C'D' là hình hộp)
- Phép trừ: AB - AC = CB
- Ví dụ: Cho tam giác ABC. Rút gọn: AB + BC + CA = ?
- Tính chất giao hoán: a + b = b + a
- Tính chất kết hợp: (a + b) + c = a + (b + c)
- Cộng vector 0: a + 0 = a

#### Nhân vectơ với số thực

- Vectơ cùng phương: a = k x b: cùng hướng với a nếu k > 0, ngược hướng với a nếu k < 0, độ dài |a| = |k| x |b|

#### Tọa độ trong không gian Oxyz

- Hệ tọa độ không gian Oxyz: 3 trục Ox, Oy, Oz vuông góc nhau
- Tọa độ điểm M(x; y; z); tọa độ vectơ a = (a1; a2; a3) = a1.i + a2.j + a3.k
- Vector AB = (xB - xA; yB - yA; zB - zA)
- Khoảng cách: |AB| = sqrt((xB - xA)^2 + (yB - yA)^2 + (zB - zA)^2)
- Trung điểm đoạn thẳng: M = ((xA + xB)/2; (yA + yB)/2; (zA + zB)/2)
- Tích 1 số: k.a = (k.a1, k.a2, k.a3)
- Trọng tâm tam giác: G = ((xA + xB + xC)/3; (yA + yB + yC)/3; (zA + zB + zC)/3)

DẠNG 1: XÁC ĐỊNH TỌA ĐỘ VECTƠ, XÁC ĐỊNH TỌA ĐỘ ĐIỂM, XÁC ĐỊNH TỌA ĐỘ ĐỈNH CỦA HÌNH BÌNH HÀNH VÀ HÌNH HỘP
DẠNG 2: XÁC ĐỊNH TỌA ĐỘ HÌNH CHIẾU VUÔNG GÓC CỦA MỘT ĐIỂM TRÊN TRỤC TỌA ĐỘ VÀ TRÊN MẶT PHẲNG TỌA ĐỘ
DẠNG 3: XÁC ĐỊNH TỌA ĐỘ CỦA VECTƠ VÀ ĐỘ DÀI CỦA ĐOẠN THẲNG
DẠNG 4: XÁC ĐỊNH TỌA ĐỘ ĐIỂM

#### Tích vô hướng

- a . b = |a| . |b| . cos(a, b) = a1.b1 + a2.b2 + a3.b3
- Hai vectơ vuông góc: a . b = 0
- Ứng dụng: tính góc giữa 2 vectơ, kiểm tra vuông góc

DẠNG 1: TÍCH VÔ HƯỚNG VÀ CÁC ỨNG DỤNG CỦA TÍCH VÔ HƯỚNG

#### Tích có hướng (tích vectơ)

- a x b = (a2.b3 - a3.b2; a3.b1 - a1.b3; a1.b2 - a2.b1)
- Ứng dụng: tìm vectơ vuông góc với 2 vectơ, tìm vectơ pháp tuyến mặt phẳng
- |a x b| = diện tích hình bình hành tạo bởi a và b
- |a x b| / 2 = diện tích tam giác tạo bởi a và b

DẠNG 1: XÁC ĐỊNH VECTƠ VÀ CHỨNG MINH ĐẲNG THỨC VECTƠ
DẠNG 2: CHỨNG MINH BA ĐIỂM THẲNG HÀNG, PHÂN TÍCH VECTƠ
DẠNG 3: GÓC GIỮA HAI VECTƠ. TÍCH VÔ HƯỚNG GIỮA HAI VECTƠ
DẠNG 4: ĐẲNG THỨC VÉC TƠ
DẠNG 5: PHÂN TÍCH VÉC TƠ THEO CÁC VÉC TƠ CHO TRƯỚC

### Phương pháp tọa độ trong không gian

#### Phương trình mặt phẳng

- Vectơ pháp tuyến n = (A; B; C): vuông góc với mặt phẳng
- Phương trình tổng quát: Ax + By + Cz + D = 0
- Phương trình mặt chắn: A, B, C nằm trên 3 trục tọa độ: x/a + y/b + z/c = 1
- Viết phương trình mặt phẳng khi biết:
  - 1 điểm + vectơ pháp tuyến
    - Trong không gian Oxyz, nếu mặt phẳng (α) đi qua điểm M0(x0; y0; z0) và có vectơ pháp tuyến n = (A; B; C) thì có phương trình là: A(x – x0) + B(y – y0) + C(z – z0) = 0 ⇔ Ax + By + Cz + D = 0, với D = −(Ax0 + By0 + Cz0).
  - 1 điểm + 2 vectơ chỉ phương a = (a1, a2, a3), b = (b1, b2, b3)
    - Tìm vectơ pháp tuyến: n = (a2.b3 - a3.b2, a3.b1 - a1.b3, a1.b2 - a2.b1)
    - Quay về dạng 1 
  - 3 điểm không thẳng hàng
    - Tìm 2 vector chỉ phương từ 3 điểm, quay về dạng 2
- 2 mặt phẳng vuông góc nếu 2 vector pháp tuyến vuông góc hay u . v = 0 => A.A' + B.B' + C.C' = 0
- 2 mặt phẳng song song nếu 2 vector pháp tuyến song song hoặc trùng nhau và D1 khác kD: hay u = kv và D1 khác kD' => A = kA', B = kB', C = kC', D1 khác kD' hay A/A' = B/B' = C/C' khác D/D'
- 2 mặt phẳng trùng nếu 2 vector pháp tuyến song song hoặc trùng nhau và D1 = kD: hay u = kv và D1 = kD' => A = kA', B = kB', C = kC', D1 = kD' hay A/A' = B/B' = C/C' = D/D'
- Khoảng cách từ điểm M(x0; y0; z0) đến mặt phẳng: d = |A.x0 + B.y0 + C.z0 + D| / sqrt(A^2 + B^2 + C^2)
- Góc giữa 2 mặt phẳng: cos(alpha) = |n1 . n2| / (|n1| x |n2|)
- Ví dụ: Viết phương trình mặt phẳng qua A(1; 0; 2) có vectơ pháp tuyến n = (2; -1; 3).

DẠNG 1: VIẾT PHƯƠNG TRÌNH MẶT PHẲNG KHI BIẾT MỘT ĐIỂM VÀ VECTƠ PHÁP TUYẾN CỦA NÓ.
DẠNG 2: Viết phương trình mặt phẳng đi qua 1 điểm và song song với 1 mặt phẳng cho trước.
DẠNG 3: VIẾT PHƯƠNG TRÌNH MẶT PHẲNG ĐI QUA 3 ĐIỂM A, B, C KHÔNG THẲNG HÀNG.
DẠNG 4: VIẾT PHƯƠNG TRÌNH MẶT PHẲNG QUA HAI DIỂM A, B VÀ VUÔNG GÓC VỚI MẶT PHẲNG. 
DẠNG 5: VIẾT PHƯƠNG TRÌNH MẶT PHẲNG QUA DIỂM A VÀ VUÔNG GÓC VỚI HAI MẶT PHẲNG
Dạng 6: Viết phương trình mặt phẳng song song với 1 mặt phẳng và cách một khoảng k cho trước.
DẠNG 7: KHOẢNG CÁCH TỪ MỘT ĐIỂM ĐẾN MỘT MẶT PHẲNG
DẠNG 8: VỊ TRÍ TƯƠNG ĐỐI HAI MẶT PHẲNG

#### Phương trình đường thẳng trong không gian

- Vectơ chỉ phương u = (a; b; c), đi qua điểm A(x0; y0, z0)
- Phương trình đường phẳng (tham số): { x = x0 + at; y = y0 + bt; z = z0 + ct }
- Phương trình đường phẳng (chính tắc): (x - x0)/a = (y - y0)/b = (z - z0)/c
- Phương trình đường thẳng đi qua hai điểm
  - Tìm vector chỉ phương từ 2 điểm, rồi tìm ptđt (x - x1)/(x2 - x1) = (y - y1)/(y2 - y1) = (z - z1)/(z2 - z1)
- Hai đường thẳng vuông góc: n1.n2 = 0 => a1,a2 + b1.b2 + c1.c2 = 0
- Vị trí tương đối giữa 2 đường thẳng: cắt, song song, chéo, trùng
  - Song song nếu vector chỉ phương cùng phương và 1 điểm ở đt 1 không nằm trên đt 2. Hay hệ pt tham số vô nghiệm
  - Trùng nếu vector chỉ phương cùng phương và 1 điểm ở đt 1 nằm trên đt 2. Hay hệ pt tham số vô số nghiệm
  - Cắt nhau nếu tích có hướng 2 vector chỉ phương khác 0 và vuông góc với vector tạo bởi 2 điểm trên 2 đường thẳng (tích = 0). Hay hệ pt tham số có 1 nghiệm duy nhất
  - Chéo nhau nếu tích có hướng 2 vector chỉ phương không vuông góc với vector tạo bởi 2 điểm trên 2 đường thẳng (tích khác 0). Hay hệ pt tham số vô nghiệm
- Vị trí tương đối giữa đường thẳng và mặt phẳng: cắt (1 điểm), song song, nằm trong mặt phẳng
- Giao điểm đường thẳng và mặt phẳng: thế tham số vào PT mặt phẳng
- Ví dụ: Tìm giao điểm đường thẳng { x = 1 + t; y = 2 - t; z = 3 + 2t } với mặt phẳng x + y + z - 6 = 0.
- Khoảng cách từ điểm đến đường thẳng: dùng tích có hướng
- Khoảng cách giữa 2 đường thẳng chéo nhau: dùng tích hỗn tạp
- Ví dụ: Tính khoảng cách từ A(1; 2; 3) đến mặt phẳng 2x - y + 2z - 6 = 0.

DẠNG 1: XÁC ĐỊNH VECTOR CHỈ PHƯƠNG CỦA ĐƯỜNG THẲNG
DẠNG 2: PHƯƠNG TRÌNH ĐƯỜNG THẲNG
DẠNG 3: VỊ TRÍ TƯƠNG ĐỐI

#### Công thức tính góc trong không gian

- Góc giữa 2 đường thẳng: cos(d, d') = |cos(u, v)| = |a.a' + b.b' + c.c'| / (sqrt(a^2 + b^2 + c^2) x sqrt(a'^2 + b'^2 + c'^2))
- Góc giữa đường thẳng và mặt phẳng: sin(d, P) = |cos(u, n)| = |a.A + b.B + c.C| / (sqrt(a^2 + b^2 + c^2) x sqrt(A^2 + B^2 + C^2))
- Góc giữa 2 mặt phẳng: cos(P, Q) = |cos(n, n')| = |A.A' + B.B' + C.C'| / (sqrt(A^2 + B^2 + C^2) x sqrt(A'^2 + B'^2 + C'^2))

DẠNG 1: GÓC GIỮA HAI ĐƯỜNG THẲNG
DẠNG 2: GÓC GIỮA ĐƯỜNG THẲNG VÀ MẶT PHẲNG
DẠNG 3: GÓC GIỮA HAI MẶT PHẲNG
DẠNG 4: TỌA ĐỘ HÓA BÀI TOÁN HÌNH HỌC KHÔNG GIAN

#### Phương trình mặt cầu

- Phương trình mặt cầu (loại 1): (x - a)^2 + (y - b)^2 + (z - c)^2 = R^2 (tâm I(a; b; c), bán kính R)
- Loại 2: x^2 + y^2 + z^2 + 2a.x + 2b.y + 2c.z + d = 0 với r = sqrt(a^2 + b^2 + c^2 - d)
- Diện tích mặt cầu: S = 4 x pi x R^2
- Thể tích hình cầu: V = (4/3) x pi x R^3
- Vị trí tương đối giữa điểm và mặt cầu:
  - M(x0, y0, z0) nằm trong mặt cầu: (x0 - a)^2 + (y0 - b)^2 + (z0 - c)^2 < R^2
  - M(x0, y0, z0) nằm ngoài mặt cầu: (x0 - a)^2 + (y0 - b)^2 + (z0 - c)^2 > R^2
  - M(x0, y0, z0) nằm trên mặt cầu: (x0 - a)^2 + (y0 - b)^2 + (z0 - c)^2 = R^2
- Vị trí tương đối giữa mặt phẳng và mặt cầu (d là khoảng cách từ tâm đến mặt phẳng):
  - d > R: không giao nhau
  - d = R: tiếp xúc (1 điểm)
  - d < R: cắt nhau (đường tròn giao tuyến có bán kính r = sqrt(R^2 - d^2))
- Vị trí tương đối giữa đường thẳng và mặt cầu (d là khoảng cách từ tâm đến mặt phẳng):
  - d > R: không cắt nhau
  - d = R: tiếp xúc (1 điểm)
  - d < R: cắt tại 2 điểm
- Ví dụ: Cho mặt cầu tâm I(1; 2; 3), R = 5. Viết phương trình mặt cầu. Tìm giao với mp x = 1.

DẠNG 1: XÁC ĐỊNH TÂM – BÁN KÍNH – NHẬN BIẾT PHƯƠNG TRÌNH MẶT CẦU
DẠNG 2: MẶT CẦU CÓ TÂM VÀ ĐI QUA MỘT ĐIỂM
DẠNG 3: MẶT CẦU CÓ ĐƯỜNG KÍNH
- Tìm trung điểm => Tâm
DẠNG 4: MẶT CẦU QUA 4 ĐIỂM KHÔNG ĐỒNG PHẲNG
- IA = IB = IC = ID lập hệ 3 phương trình => Tâm
DẠNG 5: MẶT CẦU CÓ TÂM THUỘC ĐƯỜNG THẲNG/MẶT PHẲNG
- Viết tọa độ tâm theo đường thẳng/mặt phẳng
- IA = IB lập hệ phương trình => Tâm
DẠNG 6: MẶT CẦU TIẾP XÚC ĐƯỜNG THẲNG/MẶT PHẲNG
DẠNG 7: BÀI TOÁN THỰC TẾ
