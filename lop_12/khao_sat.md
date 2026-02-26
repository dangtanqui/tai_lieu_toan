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
  - Hàm phân thức bật nhất / bật nhất: y = (ax + b) / (cx + d)
  - Hàm phân thức bật hai / bật nhất: y = (ax^2 + bx + c) / (px + q)
- Ví dụ: Khảo sát và vẽ đồ thị hàm số y = x^3 - 3x^2 + 2.

```
#### Ứng dụng đồ thị

- Dùng đồ thị biện luận số nghiệm phương trình f(x) = m
- Tìm m để phương trình có 1 nghiệm, 2 nghiệm, 3 nghiệm
- Ví dụ: Dựa vào đồ thị y = x^3 - 3x, tìm m để x^3 - 3x = m có 3 nghiệm phân biệt.

### Hàm số mũ và hàm số logarit

#### Lũy thừa (mở rộng)

- Lũy thừa với số mũ nguyên âm: a^(-n) = 1 / a^n (a ≠ 0)
- Lũy thừa với số mũ hữu tỉ: a^(m/n) = căn bậc n của a^m (a > 0)
- Tính chất lũy thừa (mở rộng cho số mũ thực):
+ a^x x a^y = a^(x+y)
+ a^x / a^y = a^(x-y)
+ (a^x)^y = a^(xy)
+ (a x b)^x = a^x x b^x

#### Hàm số mũ

- y = a^x (a > 0, a ≠ 1)
- a > 1: hàm đồng biến; 0 < a < 1: hàm nghịch biến
- Đồ thị luôn qua điểm (0; 1)
- TXĐ: R; tập giá trị: (0; +vô cực)

#### Logarit

- log_a(b) = c nghĩa là a^c = b (a > 0, a ≠ 1, b > 0)
- Logarit tự nhiên: ln(x) = log_e(x) (e ≈ 2,718)
- Logarit thập phân: lg(x) = log_10(x)
- Tính chất:
+ log_a(1) = 0; log_a(a) = 1
+ log_a(xy) = log_a(x) + log_a(y)
+ log_a(x/y) = log_a(x) - log_a(y)
+ log_a(x^n) = n x log_a(x)
+ Đổi cơ số: log_a(b) = log_c(b) / log_c(a)
- Ví dụ: log_2(8) = ?, log_3(1/9) = ?, lg(1000) = ?

#### Hàm số logarit

- y = log_a(x) (a > 0, a ≠ 1)
- TXĐ: (0; +vô cực); tập giá trị: R
- a > 1: đồng biến; 0 < a < 1: nghịch biến
- Đồ thị luôn qua điểm (1; 0)
- y = log_a(x) là hàm ngược của y = a^x

#### Phương trình, bất phương trình mũ và logarit

- Phương trình mũ cơ bản: a^x = b → x = log_a(b)
- Phương trình logarit cơ bản: log_a(x) = b → x = a^b
- Điều kiện: biểu thức trong logarit phải > 0
- Bất phương trình: chú ý chiều bất đẳng thức phụ thuộc cơ số a > 1 hay 0 < a < 1
- Ví dụ: Giải 2^x = 16. Giải log_2(x - 1) = 3.
- Ví dụ: Giải 3^(2x-1) > 27.
```

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

### Thống kê (ôn lại lớp 10)

- Tính xấp xỉ a ra số gần đúng a gạch ngang đầu
- Sai số tuyệt đối: Denta(a) = |a - a gạch ngang|
- Sai sô tương đối: S(a) = Denta(a)/|a|
- Làm tròn số a ra số quy tròn b
- Các số đặc trưng đo xu thế trung tâm (ôn lại lớp 7)
  - Số trung bình (tbc): X gạch ngang = (x1 + x2 + ... + xn)/n (hoặc xtb)
  - Số trung vị: Sắp xếp thứ tự từ bé đến lớn, lấy số ở giữa (nếu k có thì lấy 2 số ở giữa chia 2)
  - Tứ phân vị: gồm Q1, Q2, Q3
    - Sắp xếp thứ tự từ bé đến lớn
    - Tìm trung vị: Q2
    - Tìm trung vị nữa bên trái (k bao gồm Q2 nếu lẻ): Q1
    - Tương tự bên phải: Q3
  - Mốt: giá trị xuất hiện nhiều nhất
- Các số đặc trưng đo mức độ phân tán:
  - Khoảng biến thiên: R = số lớn nhất - số bé nhất
  - Khoảng tứ phân vị: Denta(Q) = Q3 - Q1
  - Phương sai: S^2 = [(x1 - xtb)^2 + (x2 - xtb)^2 + ... + (xn - xtb)^2]/n
  - Độ lệch chuẩn: S = sqrt(phương sai)
- Ví dụ: Cho dãy điểm: 5, 6, 7, 8, 9. Tính trung bình, phương sai, độ lệch chuẩn.

## Xác xuất có điều kiện

- Cho hai biến cố A và B. Xác suất của biến cố A, tính trong điều kiện biết rằng biến cố B đã xảy ra, được gọi là xác suất của A với điều kiện B và kí hiệu là P(A | B): P(A | B) = P(AB) / P(B)
- Công thức nhân xác xuất: P(AB) = P(B).P(A | B)
- Xác xuất toàn phần: P(B) = P(A).P(B | A) + P(phũ A).P(B | phũ A)
- Công thức Bayes: P(A | B) = (P(A).P(B | A)) / (P(A).P(B | A) + P(phũ A).P(B | phũ A))

---

## Hình học

### Vectơ trong không gian – Phương trình mặt phẳng, đường thẳng

#### Tọa độ trong không gian Oxyz

- Hệ tọa độ không gian Oxyz: 3 trục Ox, Oy, Oz vuông góc nhau
- Tọa độ điểm M(x; y; z); tọa độ vectơ a = (a1; a2; a3)
- vector AB = (xB - xA; yB - yA; zB - zA)
- Khoảng cách: |AB| = sqrt((xB - xA)^2 + (yB - yA)^2 + (zB - zA)^2)
- Trung điểm đoạn thẳng: M = ((xA + xB)/2; (yA + yB)/2; (zA + zB)/2)
- Trọng tâm tam giác: G = ((xA + xB + xC)/3; (yA + yB + yC)/3; (zA + zB + zC)/3)

#### Tích có hướng (tích vectơ)

- Tích vô hướng: a . b = a1.b1 + a2.b2 + a3.b3 = |a|.|b|.cos 0
  - Ứng dụng tính góc của 2 vector, kiểm tra sự vuông góc
- Hai vectơ vuông góc: a . b = 0
- Tích có hướng a x b = (a2.b3 - a3.b2; a3.b1 - a1.b3; a1.b2 - a2.b1)
  - Ứng dụng tìm 1 vector vuông góc với 2 vector đã cho, tính diện tích hình bình hành, hình tam giác, tìm vectơ pháp tuyến mặt phẳng để viết phương trình mặt phẳng
- Độ lớn tích có hướng |a x b| = diện tích hình bình hành tạo bởi a và b
- Độ lớn tích có hướng |a x b| / 2 = diện tích hình tam giác tạo bởi a và b

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

#### Khoảng cách trong không gian (tọa độ)

- Khoảng cách từ điểm đến đường thẳng: dùng tích có hướng
- Khoảng cách giữa 2 đường thẳng chéo nhau: dùng tích hỗn tạp
- Khoảng cách từ điểm đến mặt phẳng: dùng công thức
- Ví dụ: Tính khoảng cách từ A(1; 2; 3) đến mặt phẳng 2x - y + 2z - 6 = 0.

### Mặt nón, mặt trụ, mặt cầu

#### Mặt nón tròn xoay

- Hình nón tròn xoay: quay tam giác vuông quanh 1 cạnh góc vuông
- Đường sinh l: l^2 = r^2 + h^2
- Diện tích xung quanh: Sxq = pi x r x l
- Diện tích toàn phần: Stp = pi x r x (r + l)
- Thể tích: V = pi x r^2 x h / 3
- Thiết diện qua trục: tam giác cân
- Hỏi: Khi cắt hình nón bằng mặt phẳng song song đáy thì thiết diện là gì? (đường tròn)

#### Mặt trụ tròn xoay

- Hình trụ tròn xoay: quay hình chữ nhật quanh 1 cạnh
- Diện tích xung quanh: Sxq = 2 x pi x r x h (= 2 x pi x r x l vì l = h)
- Diện tích toàn phần: Stp = 2 x pi x r x (r + h)
- Thể tích: V = pi x r^2 x h
- Thiết diện qua trục: hình chữ nhật
- Ví dụ: Hình trụ r = 5, h = 10. Tính V, Sxq, Stp.

#### Mặt cầu

- Phương trình mặt cầu: (x - a)^2 + (y - b)^2 + (z - c)^2 = R^2 (tâm I(a; b; c), bán kính R)
- Diện tích mặt cầu: S = 4 x pi x R^2
- Thể tích hình cầu: V = (4/3) x pi x R^3
- Vị trí tương đối giữa mặt phẳng và mặt cầu (d là khoảng cách từ tâm đến mặt phẳng):
+ d > R: không giao nhau
+ d = R: tiếp xúc (1 điểm)
+ d < R: cắt nhau (đường tròn giao tuyến có bán kính r = sqrt(R^2 - d^2))
- Ví dụ: Cho mặt cầu tâm I(1; 2; 3), R = 5. Viết phương trình mặt cầu. Tìm giao với mp x = 1.
