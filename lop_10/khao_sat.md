# Khảo sát Toán 10

---

## Đại số

### Mệnh đề và tập hợp

#### Mệnh đề

- Mệnh đề là câu khẳng định đúng hoặc sai (không vừa đúng vừa sai).
- Ví dụ: "3 là số nguyên tố" → đúng. "5 > 7" → sai.
- Hỏi: "x + 2 = 5" có phải mệnh đề không? (Không, vì còn phụ thuộc x → mệnh đề chứa biến)
- Phủ định của mệnh đề P: ký hiệu "Dấu - ở trên P"; nếu P đúng thì phủ P sai và ngược lại.
- Mệnh đề kéo theo: "Nếu P thì Q" (P => Q).
- Mệnh đề đảo: Mệnh đề P => Q là mệnh đề đảo của Q => P
- Điều kiện cần, điều kiện đủ:
  - P => Q: P là điều kiện đủ để Q; Q là điều kiện cần để P.
- Mệnh đề tương đương: P <=> Q nghĩa là P => Q và Q => P đều đúng.
- Điều kiện cần và đủ, khi và chỉ khi
  - P => Q: P là điều kiện cần và đủ để Q; Q khi và chỉ khi P
- Hỏi: "Tam giác đều => tam giác cân" đúng không? Điều ngược lại thì sao?
- Mệnh đề chứa ký hiệu "với mọi", "tồn tại"
- Ví dụ: với mọi x, x^2 >= 0; tồn tại x, x^=4

#### Tập hợp và các phép toán

- Nhắc lại tập hợp (lớp 6)
  - Liêt kê
  - Chỉ ra tính chất đặc trưng
  - Tập rỗng
- Tập con: A là tập con của B nếu mọi phần tử của A đều thuộc B.
- Hai tập hợp bằng nhau: Mỗi phần tử thuộc A cũng thuộc B và ngược lại (tức A con B và B con A => A = B).
- Phép hợp: A hợp B = tập gồm các phần tử thuộc A hoặc thuộc B (hoặc cả hai).
- Phép giao: A giao B = tập gồm các phần tử thuộc cả A và B.
- Phép hiệu: A \ B = tập gồm các phần tử thuộc A mà không thuộc B.
- Phần bù: nếu A là tập con của E thì phần bù của A trong E = E \ A.
- Ví dụ: A = {1; 2; 3; 4}, B = {3; 4; 5; 6}. Tìm A giao B, A hợp B, A \ B.
- Công thức: A hợp B = A + B - A giao B
- Các tập số: N, Z, Q, R và mối quan hệ bao hàm.
- Khoảng, đoạn, nửa khoảng trên trục số:
  - (a; b) là khoảng (không chứa 2 đầu mút)
  - [a; b] là đoạn (chứa cả 2 đầu mút)
  - [a; b) hoặc (a; b] là nửa khoảng

### Bất phương trình và hệ bất phương trình bậc nhất hai ẩn

- Bất phương trình bậc nhất hai ẩn: ax + by < c (hoặc <=, >, >=)
- Cặp (x0, y0) là 1 nghiệm nếu thế vào biểu thức đúng.
- Miền nghiệm: là nửa mặt phẳng, bao gồm (nét liền) hoặc không bao gồm (nét đứt) đường biên tùy dấu
- Cách xác định miền nghiệm: vẽ đường thẳng ax + by = c, chọn 1 điểm thử, xác định nửa mặt phẳng thỏa mãn.
- Hệ bất phương trình: miền nghiệm là phần giao các miền nghiệm.
- Cặp (x0, y0) là 1 nghiệm nếu thế vào 2 biểu thức đúng.
- Ví dụ: Xác định miền nghiệm của hệ: { x + y <= 6; x >= 0; y >= 0 }
- Bài toán tối ưu (quy hoạch tuyến tính đơn giản): tìm giá trị lớn nhất/nhỏ nhất của biểu thức trên miền nghiệm.

### Hàm số bậc hai

#### Ôn tập hàm số (lớp 8)

- Nếu mỗi giá trị của x thuộc D, tìm được 1 giá trị của y gọi là hàm số
- x là biến số, y là hàm số của x, ký hiệu: y = f(x)
- D: Tập xác định (TXĐ) của hàm số
- Hàm chẵn: f(-x) = f(x), đồ thị đối xứng qua trục Oy
- Hàm lẻ: f(-x) = -f(x), đồ thị đối xứng qua gốc tọa độ O
- Hỏi: y = x^2 là hàm chẵn hay lẻ? y = x^3 thì sao?
- Đồ thị của hàm số: tập hợp các điểm M(x, f(x)) trên trục tọa độ
- Đồng biến: x1 < x2 => f(x1) < f(x2)
- Nghịch biến: x1 < x2 => f(x1) > f(x2)

#### Hàm số bậc hai y = ax^2 + bx + c (a ≠ 0)

- Ôn lại lớp 9 có học đồ thị y = ax^2
- Đồ thị là parabol, đỉnh I(-b/(2a); -Delta/(4a)) với Delta = b^2 - 4ac
- Trục đối xứng: x = -b/(2a)
- a > 0: parabol cong xuống (có giá trị nhỏ nhất)
- a < 0: parabol cong lên (có giá trị lớn nhất)
- Bảng biến thiên: xét khi a > 0 và a < 0
- Ví dụ: Vẽ đồ thị y = x^2 - 4x + 3. Tìm đỉnh, trục đối xứng, điểm cắt trục Ox.
- Hỏi: Parabol y = -x^2 + 2x + 3 quay lên hay xuống? Đỉnh ở đâu?

#### Tam thức bậc hai

- ôn lại lớp 9 phương trình bật 2
- Dấu của tam thức bậc hai: f(x) = ax^2 + bx + c
  - Delta < 0: f(x) cùng dấu với a, mọi x
  - Delta = 0: f(x) cùng dấu với a, mọi x ≠ -b/(2a)
  - Delta > 0: f(x) trái dấu với a khi x nằm giữa hai nghiệm; cùng dấu với a khi x nằm ngoài hai nghiệm
- Ứng dụng: giải bất phương trình bậc hai

#### Phương trình quy về phương trình bậc hai

- Dạng sqrt(ax^2 + bx + c) = sqrt(dx^2 + ex + f)
- Dạng sqrt(ax^2 + bx + c) = dx + e

### Hệ thức lượng trong tam giác

#### Giá trị lượng giác của góc từ 0° đến 180°

- Mở rộng định nghĩa sin, cos, tan, cot cho góc từ 0° đến 180° (không chỉ góc nhọn như lớp 9)
- Với góc alpha (0° < alpha < 180°):
  - sin(alpha) >= 0
  - cos(alpha) > 0 khi 0° < alpha < 90° (góc tù)
  - cos(alpha) < 0 khi 90° < alpha < 180° (góc tù)
- tan = sin / cos, cot = cos / sin, tan = 1 / cot
- Bù nhau: sin(180° - alpha) = sin(alpha); cos(180° - alpha) = -cos(alpha), tan(180° - alpha) = -tan(alpha), cot(180° - alpha) = -cot(alpha)
- Hỏi: sin(120°) = ?, cos(150°) = ?

#### Định lí cosin

- a^2 = b^2 + c^2 - 2bc x cos(A)
- Dùng khi biết 2 cạnh và góc xen giữa, hoặc biết 3 cạnh tìm góc.
- Ví dụ: Tam giác có b = 5, c = 7, góc A = 60°. Tìm a.
- Hỏi: Khi góc A = 90° thì công thức trở thành Pythagore

#### Định lí sin

- a/sin(A) = b/sin(B) = c/sin(C) = 2R (R là bán kính đường tròn ngoại tiếp)
- Dùng khi biết 1 cạnh + góc đối diện + thêm 1 góc hoặc 1 cạnh.
- Ví dụ: Tam giác có A = 30°, B = 45°, a = 6. Tìm b.

#### Diện tích tam giác

- S = (1/2) x a x b x sin(C) = ... = pr = (a + b + c).r/2 = abc/(4R)
- Công thức Heron: S = sqrt(p(p - a)(p - b)(p - c))
- Ví dụ: Tam giác có a = 8, b = 5, góc C = 30°. Tính S.
- Giải tam giác: cho các yếu tố, tìm các yếu tố còn lại.

---

### Đại số tổ hợp

#### Quy tắc đếm

- Quy tắc cộng: nếu công việc có thể thực hiện theo cách 1 (m cách) HOẶC cách 2 (n cách) thì tổng = m + n cách.
- Quy tắc nhân: nếu công việc gồm bước 1 (m cách) VÀ bước 2 (n cách) thì tổng = m x n cách.
- Ví dụ: Đi từ A đến B có 3 đường, từ B đến C có 4 đường. Đi từ A đến C qua B có mấy cách?
- Kết hợp 2 quy tắc

#### Hoán vị, chỉnh hợp, tổ hợp

- Hoán vị n phần tử: P(n) = n! (sắp xếp tất cả)
- Chỉnh hợp chập k của n: A(n, k) = n! / (n - k)! (chọn k phần tử có thứ tự, chọn lần lượt để làm công việc khác nhau)
- Tổ hợp chập k của n: C(n, k) = n! / (k! x (n - k)!) (chọn k phần tử không thứ tự, chọn 1 lần để làm công việc giống nhau)
- Hỏi: Phân biệt khi nào dùng chỉnh hợp, khi nào dùng tổ hợp?
- Ví dụ: Từ 5 bạn, chọn 3 bạn xếp hàng → dùng gì? Chọn 3 bạn lập nhóm → dùng gì?
- Nhị thức Newton: (a + b)^n = tổng C(n, k) x a^(n-k) x b^k (k từ 0 đến n)
- Ví dụ: Khai triển (a + b)^4,  (a + b)^5.

### Xác suất

- Phép thử ngẫu nhiên: 1 hành động mà kết quả không biết trước
- Không gian mẫu (ký hiệu Omega): tập hợp các kết quả có thể xảy ra
- Kết quả thuận lợi: 1 biến cố E liên quan đến phép thử T là kết quả của phép thử T làm cho biến cố E xảy ra
- Biến cố: tập con của không gian mẫu. tập con này là các kết quả thuận lợi
- Biến đố đối: biến bố đối của biến cố E là biến cố E không xảy ra, ký hiệu E gạch ngang đầu
- Xác suất cổ điển: P(A) = số kết quả thuận lợi / tổng số kết quả. = n(A) / n(Omega)
- Quy tắc cộng xác suất (biến cố xung khắc): P(A hợp B) = P(A) + P(B)
- Quy tắc nhân xác suất (biến cố độc lập): P(A giao B) = P(A) x P(B)
- Biến cố đối: P(A gạch ngang) = 1 - P(A)
- Ví dụ: Gieo 2 xúc xắc. Tính xác suất tổng bằng 7. Kq: 6/36=1/6
- Ví dụ: Rút 2 lá bài từ bộ 52 lá. Tính xác suất cả 2 là át. Kq: C(2, 4)/C(2, 52) = 6/1326
- Ví dụ: Rút lần lượt 2 lá bài từ bộ 52 lá. Tính xác suất cả 2 là át. Kq: A(2, 4)/A(2, 52) = 1/221

### Thống kê

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

---

## Hình học

### Vectơ

#### Khái niệm vectơ

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
- Phép trừ: AB - AC = CB
- Ví dụ: Cho tam giác ABC. Rút gọn: AB + BC + CA = ?
- Tính chất giao hoán: a + b = b + a
- Tính chất kết hợp: (a + b) + c = a + (b + c)

#### Nhân vectơ với số thực

- Vectơ cùng phương: a = k x b: cùng hướng với a nếu k > 0, ngược hướng với a nếu k < 0, độ dài |a| = |k| x |b|
- Trung điểm M của AB: OM = (OA + OB) / 2 (với O bất kỳ)
- Trọng tâm G của tam giác ABC: OG = (OA + OB + OC) / 3

#### Tọa độ vectơ và tọa độ điểm

- Vectơ a = (a1; a2) trong hệ tọa độ Oxy
- AB = (xB - xA; yB - yA)
- Độ dài: |AB| = sqrt((xB - xA)^2 + (yB - yA)^2)
- Trung điểm M của AB: M = ((xA + xB)/2; (yA + yB)/2)
- Trọng tâm G: G = ((xA + xB + xC)/3; (yA + yB + yC)/3)
- Tích vô hướng theo tọa độ: a . b = a1 x b1 + a2 x b2
- Hai vectơ vuông góc: a . b = 0
- Ví dụ: A(1; 2), B(4; 6). Tìm |AB| và trung điểm M.

#### Tích vô hướng của hai vectơ

- a . b = |a| x |b| x cos(a, b)
- Tính chất: a . b = b . a; a . (b + c) = a . b + a . c; a . a = |a|^2
- Hai vectơ vuông góc khi a . b = 0
- Ví dụ: |a| = 3, |b| = 4, góc giữa a và b = 60°. Tính a . b.

### Phương pháp tọa độ trong mặt phẳng

#### Phương trình đường thẳng

- Vectơ chỉ phương u = (A; B): nếu giá của nó song song với đường thẳng
- Vectơ pháp tuyến n = (a; b): nếu giá của nó vuông góc với đường thẳng
- Phương trình tổng quát: ax + by + c = 0 với n = (a, b) là vector pháp tuyến, u = (a, -b) hoặc u = (-a, b)
- Phương trình tham số: { x = x0 + at; y = y0 + bt } (t là tham số)
- Hệ số góc: y = kx + m (k = -a/b)
- Khoảng cách từ điểm M(x0; y0) đến đường thẳng ax + by + c = 0: d = |a.x0 + b.y0 + c| / sqrt(a^2 + b^2)
- Góc giữa hai đường thẳng: cos(alpha) = |a1.a2 + b1.b2| / (sqrt(a1^2 + b1^2) x sqrt(a2^2 + b2^2))
- Hai đường thẳng song song: a1/a2 = b1/b2 ≠ c1/c2
- Hai đường thẳng vuông góc: a1.a2 + b1.b2 = 0
- Ví dụ: Viết phương trình đường thẳng qua A(1; 2) và vuông góc với d: 3x + 4y - 5 = 0.

#### Phương trình đường tròn

- Phương trình chính tắc: (x - a)^2 + (y - b)^2 = R^2 (tâm I(a; b), bán kính R)
- Phương trình khai triển: x^2 + y^2 - 2ax - 2by + c = 0 (tâm I(a; b), R = sqrt(a^2 + b^2 - c))
- Điều kiện để là đường tròn: a^2 + b^2 - c > 0
- Vị trí tương đối giữa đường thẳng và đường tròn (tính khoảng cách d từ tâm đến đường thẳng, so sánh với R)
- Tiếp tuyến của đường tròn: d = R
- Phương trình tiếp tuyến tại điểm M(x0; y0) trên đường tròn: (a - x0)(x - x0) + (b - y0)(y - y0) = 0, có vector pháp tuyến n = (a - x0, b - y0)
- Ví dụ: Tìm tâm và bán kính: x^2 + y^2 - 4x + 6y - 3 = 0.

#### Ba đường cong

- Elip: 2 điểm cố định F1, F2, F1F2 = 2c > 0, với a > c, tập hợp các điểm M với MF1 + MF2 = 2a tạo ra đường elip. F1, F2 là tiêu điểm, F1F2 = 2c là tiêu cự
- Phương trình chính tắt của elip: x^2/a^2 + y^2/b^2 = 1 thì F1(-sqrt(a^2 - b^2); 0), F2(sqrt(a^2 - b^2); 0), c = sqrt(a^2 - b^2), MF1 + MF2 = 2a
- Hypebol: 2 điểm cố định F1, F2, F1F2 = 2c > 0, với 0 < a < c, tập hợp các điểm M với |MF1 - MF2| = 2a tạo ra đường hypebol. F1, F2 là tiêu điểm, F1F2 = 2c là tiêu cự
- Phương trình chính tắt của hypebol: x^2/a^2 - y^2/b^2 = 1 thì F1(-sqrt(a^2 + b^2); 0), F2(sqrt(a^2 + b^2); 0), c = sqrt(a^2 - b^2), MF1 + MF2 = 2a
- Parabol: điểm cố định F và đường thẳng d không đi qua F, tập hợp các điểm cách điều F và d tạo ra đường parabol. F là tiêu điểm, d là đường chuẩn, khoảng cách F tới d là tham số tiêu
- Phương trình chính tắt của parabol: y^2 = 2px, tiêu điểm F(p/2; 0), đường chuẩn d: x = -p/2
