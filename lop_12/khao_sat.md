# Khảo sát Toán 12

---

## Đại số & Giải tích

### Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số

#### Tính đơn điệu của hàm số

- Hàm số y = f(x) gọi là đồng biến trên K nếu ∀ x1, x2 ∈ K, x1 < x2 ⇒ f(x1) < f(x2).
- Hàm số y = f(x) gọi là nghịch biến trên K nếu ∀ x1, x2 ∈ K, x1 < x2 ⇒ f(x1) > f(x2).
- f'(x) > 0 trên khoảng (a; b) → f(x) đồng biến trên (a; b)
- f'(x) < 0 trên khoảng (a; b) → f(x) nghịch biến trên (a; b)
- Cách xét: tìm f'(x), giải f'(x) = 0, lập bảng xét dấu f'(x)
- Ví dụ: Xét sự đồng biến, nghịch biến của y = x^3 - 3x + 2.

#### Cực trị của hàm số

- Điểm cực đại: f'(x) đổi dấu từ + sang - khi x qua x0 → x0 là cực đại
- Điểm cực tiểu: f'(x) đổi dấu từ - sang + khi x qua x0 → x0 là cực tiểu
- Quy tắc 2 (dùng đạo hàm cấp hai): vì f'' thể hiện độ cong (f'' > 0 lỗi, f'' < 0 lõm)
- Với f'(x0) = 0: f''(x0) < 0 → cực đại; f''(x0) > 0 → cực tiểu

#### Giá trị lớn nhất, nhỏ nhất

- Trên đoạn [a; b]: so sánh f(a), f(b) và các giá trị f(x) tại điểm cực trị bên trong
- GTLN = max; GTNN = min trong các giá trị đó
- Ví dụ: Tìm GTLN, GTNN của y = x^3 - 3x trên [-2; 2].
- Lập bảng biến thiên
- Hoặc tìm x0 trên đoạn với tính f' = 0 hoặc không tồn tại, tính f(x0), f(a), f(b) và tìm max, min

#### Đường tiệm cận

- Tiệm cận ngang: y = L nếu lim f(x) = L khi x tiến đến +/-vô cực
- Tiệm cận đứng: x = a nếu lim f(x) = +/-vô cực khi x tiến đến a+/- (a+ đồ thị bên phải, a- đồ thị bên trái)
- Tiệm cận xiên: y = ax + b nếu lim [f(x) - (ax  + b)] = 0 khi x tiến đến +/-vô cực
- Hỏi: Hàm y = (2x + 1) / (x - 1) có tiệm cận ngang và tiệm cận đứng nào?

#### Khảo sát sự biến thiên và vẽ đồ thị hàm số

- Sơ đồ khảo sát hàm số:
  1. Tìm tập xác định
  2. Tính đạo hàm, giải f'(x) = 0 hoặc tìm những điểm đạo hàm không tồn tại
  3. Lập bảng biến thiên (xét dấu f', chiều biến thiên, cực trị, giới hạn vô cực, tiệm cận)
  4. Vẽ đồ thị
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
- Thể tích vật thể tròn xoay: V = pi x tích phân từ a đến b của f(x)^2 dx
- Ví dụ: Tính diện tích hình phẳng giới hạn bởi y = x^2 và y = x.

---

## Xác suất có điều kiện

- Cho hai biến cố A và B. Xác suất của A trong điều kiện biết B đã xảy ra: P(A | B) = P(AB) / P(B)
- Công thức nhân xác suất: P(AB) = P(B) . P(A | B)
- Xác suất toàn phần: P(B) = P(A) . P(B | A) + P(A') . P(B | A') (A' là biến cố đối của A)
- Công thức Bayes: P(A | B) = P(A) . P(B | A) / P(B)

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

#### Nhân vectơ với số thực

- Vectơ cùng phương: a = k x b: cùng hướng với a nếu k > 0, ngược hướng với a nếu k < 0, độ dài |a| = |k| x |b|

#### Tọa độ trong không gian Oxyz

- Hệ tọa độ không gian Oxyz: 3 trục Ox, Oy, Oz vuông góc nhau
- Tọa độ điểm M(x; y; z); tọa độ vectơ a = (a1; a2; a3) = a1.i + a2.j + a3.k
- vector AB = (xB - xA; yB - yA; zB - zA)
- Khoảng cách: |AB| = sqrt((xB - xA)^2 + (yB - yA)^2 + (zB - zA)^2)
- Trung điểm đoạn thẳng: M = ((xA + xB)/2; (yA + yB)/2; (zA + zB)/2)
- Tích 1 số: k.a = (k.a1, k.a2, k.a3)
- Trọng tâm tam giác: G = ((xA + xB + xC)/3; (yA + yB + yC)/3; (zA + zB + zC)/3)

#### Tích vô hướng

- a . b = |a| . |b| . cos(a, b) = a1.b1 + a2.b2 + a3.b3
- Hai vectơ vuông góc: a . b = 0
- Ứng dụng: tính góc giữa 2 vectơ, kiểm tra vuông góc

#### Tích có hướng (tích vectơ)

- a x b = (a2.b3 - a3.b2; a3.b1 - a1.b3; a1.b2 - a2.b1)
- Ứng dụng: tìm vectơ vuông góc với 2 vectơ, tìm vectơ pháp tuyến mặt phẳng
- |a x b| = diện tích hình bình hành tạo bởi a và b
- |a x b| / 2 = diện tích tam giác tạo bởi a và b

### Phương pháp tọa độ trong không gian

#### Phương trình mặt phẳng

- Vectơ pháp tuyến n = (A; B; C): vuông góc với mặt phẳng
- Phương trình tổng quát: Ax + By + Cz + D = 0
- Viết phương trình mặt phẳng khi biết:
  - 1 điểm + vectơ pháp tuyến
    - Trong không gian Oxyz, nếu mặt phẳng (α) đi qua điểm M0(x0; y0; z0) và có vectơ pháp tuyến n = (A; B; C) thì có phương trình là: A(x – x0) + B(y – y0) + C(z – z0) = 0 ⇔ Ax + By + Cz + D = 0, với D = −(Ax0 + By0 + Cz0).
  - 1 điểm + 2 vectơ chỉ phương
    - Tìm vectơ pháp tuyến, quay về dạng 1 
  - 3 điểm không thẳng hàng
    - Tìm 2 vector chỉ phương từ 3 điểm, quay về dạng 2
- 2 mặt phẳng vuông góc nếu 2 vector pháp tuyến vuông góc hay u . v = 0 => A.A' + B.B' + C.C' = 0
- 2 mặt phẳng song song nếu 2 vector pháp tuyến song song hoặc trùng nhau hay u = kv => A = kA', B = kB', C = kC'
- Khoảng cách từ điểm M(x0; y0; z0) đến mặt phẳng: d = |A.x0 + B.y0 + C.z0 + D| / sqrt(A^2 + B^2 + C^2)
- Góc giữa 2 mặt phẳng: cos(alpha) = |n1 . n2| / (|n1| x |n2|)
- Ví dụ: Viết phương trình mặt phẳng qua A(1; 0; 2) có vectơ pháp tuyến n = (2; -1; 3).

#### Phương trình đường thẳng trong không gian

- Vectơ chỉ phương u = (a; b; c), đi qua điểm A(x0; y0, z0)
- Phương trình đường phẳng (tham số): { x = x0 + at; y = y0 + bt; z = z0 + ct }
- Phương trình đường phẳng (chính tắc): (x - x0)/a = (y - y0)/b = (z - z0)/c
- Phương trình đường thẳng đi qua hai điểm
  - Tìm vector chỉ phương từ 2 điểm, rồi tìm ptđt (x - x1)/(x2 - x1) = (y - y1)/(y2 - y1) = (z - z1)/(z2 - z1)
- Vị trí tương đối giữa 2 đường thẳng: cắt, song song, chéo, trùng
  - Song song nếu vector chỉ phương cùng phương và 1 điểm ở đt 1 không nằm trên đt 2
  - Trùng nếu vector chỉ phương cùng phương và 1 điểm ở đt 1 nằm trên đt 2
  - Cắt nhau nếu tích có hướng 2 vector chỉ phương khác 0 và vuông góc với vector tạo bởi 2 điểm trên 2 đường thẳng (tích = 0)
  - Chéo nhau nếu tích có hướng 2 vector chỉ phương không vuông góc với vector tạo bởi 2 điểm trên 2 đường thẳng (tích khác 0)
- Vị trí tương đối giữa đường thẳng và mặt phẳng: cắt (1 điểm), song song, nằm trong mặt phẳng
- Giao điểm đường thẳng và mặt phẳng: thế tham số vào PT mặt phẳng
- Ví dụ: Tìm giao điểm đường thẳng { x = 1 + t; y = 2 - t; z = 3 + 2t } với mặt phẳng x + y + z - 6 = 0.
- Khoảng cách từ điểm đến đường thẳng: dùng tích có hướng
- Khoảng cách giữa 2 đường thẳng chéo nhau: dùng tích hỗn tạp
- Ví dụ: Tính khoảng cách từ A(1; 2; 3) đến mặt phẳng 2x - y + 2z - 6 = 0.

#### Công thức tính góc trong không gian

- Góc giữa 2 đường thẳng: cos(d, d') = |cos(u, v)| = |a.a' + b.b' + c.c'| / (sqrt(a^2 + b^2 + c^2) x sqrt(a'^2 + b'^2 + c'^2))
- Góc giữa đường thẳng và mặt phẳng: sin(d, P) = |cos(u, n)| = |a.A + b.B + c.C| / (sqrt(a^2 + b^2 + c^2) x sqrt(A^2 + B^2 + C^2))
- Góc giữa 2 mặt phẳng: cos(P, Q) = |cos(n, n')| = |A.A' + B.B' + C.C'| / (sqrt(A^2 + B^2 + C^2) x sqrt(A'^2 + B'^2 + C'^2))

#### Phương trình mặt cầu

- Phương trình mặt cầu: (x - a)^2 + (y - b)^2 + (z - c)^2 = R^2 (tâm I(a; b; c), bán kính R)
- Diện tích mặt cầu: S = 4 x pi x R^2
- Thể tích hình cầu: V = (4/3) x pi x R^3
- Vị trí tương đối giữa mặt phẳng và mặt cầu (d là khoảng cách từ tâm đến mặt phẳng):
+ d > R: không giao nhau
+ d = R: tiếp xúc (1 điểm)
+ d < R: cắt nhau (đường tròn giao tuyến có bán kính r = sqrt(R^2 - d^2))
- Ví dụ: Cho mặt cầu tâm I(1; 2; 3), R = 5. Viết phương trình mặt cầu. Tìm giao với mp x = 1.
