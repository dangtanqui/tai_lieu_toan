# Khảo sát Toán 10

---

## Đại số

### Mệnh đề và tập hợp

#### Mệnh đề

- Mệnh đề là câu khẳng định đúng hoặc sai (không vừa đúng vừa sai).
- Ví dụ: "3 là số nguyên tố" → đúng. "5 > 7" → sai.
- Hỏi: "x + 2 = 5" có phải mệnh đề không? (Không, vì còn phụ thuộc x → mệnh đề chứa biến)
- Phủ định của mệnh đề P: ký hiệu "không P"; nếu P đúng thì phủ P sai và ngược lại.
- Mệnh đề kéo theo: "Nếu P thì Q" (P => Q). Chỉ sai khi P đúng mà Q sai.
- Mệnh đề tương đương: P <=> Q nghĩa là P => Q và Q => P đều đúng.
- Điều kiện cần, điều kiện đủ:
+ P => Q: P là điều kiện đủ để Q, Q là điều kiện cần để P.
- Hỏi: "Tam giác đều => tam giác cân" đúng không? Điều ngược lại thì sao?

#### Tập hợp và các phép toán

- Tập con: A là tập con của B nếu mọi phần tử của A đều thuộc B.
- Phép hợp: A hợp B = tập gồm các phần tử thuộc A hoặc thuộc B (hoặc cả hai).
- Phép giao: A giao B = tập gồm các phần tử thuộc cả A và B.
- Phép hiệu: A \ B = tập gồm các phần tử thuộc A mà không thuộc B.
- Phần bù: nếu A là tập con của E thì phần bù của A trong E = E \ A.
- Ví dụ: A = {1; 2; 3; 4}, B = {3; 4; 5; 6}. Tìm A giao B, A hợp B, A \ B.
- Các tập số: N, Z, Q, R và mối quan hệ bao hàm.
- Khoảng, đoạn, nửa khoảng trên trục số:
+ (a; b) là khoảng (không chứa 2 đầu mút)
+ [a; b] là đoạn (chứa cả 2 đầu mút)
+ [a; b) hoặc (a; b] là nửa khoảng

### Bất phương trình và hệ bất phương trình bậc nhất hai ẩn

- Bất phương trình bậc nhất hai ẩn: ax + by < c (hoặc <=, >, >=)
- Miền nghiệm: là nửa mặt phẳng (bao gồm hoặc không bao gồm đường biên tùy dấu)
- Cách xác định miền nghiệm: vẽ đường thẳng ax + by = c, chọn 1 điểm thử, xác định nửa mặt phẳng thỏa mãn.
- Hệ bất phương trình: miền nghiệm là phần giao các miền nghiệm.
- Ví dụ: Xác định miền nghiệm của hệ: { x + y <= 6; x >= 0; y >= 0 }
- Bài toán tối ưu (quy hoạch tuyến tính đơn giản): tìm giá trị lớn nhất/nhỏ nhất của biểu thức trên miền nghiệm.

### Hàm số bậc hai

#### Ôn tập hàm số

- Tập xác định (TXĐ) của hàm số
- Hàm chẵn: f(-x) = f(x), đồ thị đối xứng qua trục Oy
- Hàm lẻ: f(-x) = -f(x), đồ thị đối xứng qua gốc tọa độ O
- Hỏi: y = x^2 là hàm chẵn hay lẻ? y = x^3 thì sao?

#### Hàm số bậc hai y = ax^2 + bx + c (a ≠ 0)

- Đồ thị là parabol, đỉnh I(-b/(2a); -Delta/(4a)) với Delta = b^2 - 4ac
- Trục đối xứng: x = -b/(2a)
- a > 0: parabol quay bề lõm lên trên (có giá trị nhỏ nhất)
- a < 0: parabol quay bề lõm xuống dưới (có giá trị lớn nhất)
- Bảng biến thiên: xét khi a > 0 và a < 0
- Ví dụ: Vẽ đồ thị y = x^2 - 4x + 3. Tìm đỉnh, trục đối xứng, điểm cắt trục Ox.
- Hỏi: Parabol y = -x^2 + 2x + 3 quay lên hay xuống? Đỉnh ở đâu?

#### Phương trình bậc hai (ôn tập nâng cao)

- Dấu của tam thức bậc hai: f(x) = ax^2 + bx + c
+ Delta < 0: f(x) cùng dấu với a, mọi x
+ Delta = 0: f(x) cùng dấu với a, mọi x ≠ -b/(2a)
+ Delta > 0: f(x) trái dấu với a khi x nằm giữa hai nghiệm; cùng dấu với a khi x nằm ngoài hai nghiệm
- Ứng dụng: giải bất phương trình bậc hai

### Hệ thức lượng trong tam giác

#### Giá trị lượng giác của góc từ 0° đến 180°

- Mở rộng định nghĩa sin, cos, tan, cot cho góc từ 0° đến 180° (không chỉ góc nhọn như lớp 9)
- Với góc alpha (0° < alpha < 180°):
+ sin(alpha) >= 0
+ cos(alpha) < 0 khi 90° < alpha < 180° (góc tù)
- Công thức: sin(180° - alpha) = sin(alpha); cos(180° - alpha) = -cos(alpha)
- Hỏi: sin(120°) = ?, cos(150°) = ?

#### Định lí cosin

- a^2 = b^2 + c^2 - 2bc x cos(A)
- Dùng khi biết 2 cạnh và góc xen giữa, hoặc biết 3 cạnh tìm góc.
- Ví dụ: Tam giác có b = 5, c = 7, góc A = 60°. Tìm a.
- Hỏi: Khi góc A = 90° thì công thức trở thành gì? (chính là Pythagore)

#### Định lí sin

- a/sin(A) = b/sin(B) = c/sin(C) = 2R (R là bán kính đường tròn ngoại tiếp)
- Dùng khi biết 1 cạnh + góc đối diện + thêm 1 góc hoặc 1 cạnh.
- Ví dụ: Tam giác có A = 30°, B = 45°, a = 6. Tìm b.

#### Diện tích tam giác

- S = (1/2) x a x b x sin(C)
- Ví dụ: Tam giác có a = 8, b = 5, góc C = 30°. Tính S.
- Giải tam giác: cho các yếu tố, tìm các yếu tố còn lại.

### Đại số tổ hợp

#### Quy tắc đếm

- Quy tắc cộng: nếu công việc có thể thực hiện theo cách 1 (m cách) HOẶC cách 2 (n cách) thì tổng = m + n cách.
- Quy tắc nhân: nếu công việc gồm bước 1 (m cách) VÀ bước 2 (n cách) thì tổng = m x n cách.
- Ví dụ: Đi từ A đến B có 3 đường, từ B đến C có 4 đường. Đi từ A đến C qua B có mấy cách?

#### Hoán vị, chỉnh hợp, tổ hợp

- Hoán vị n phần tử: P(n) = n! (sắp xếp tất cả)
- Chỉnh hợp chập k của n: A(n, k) = n! / (n - k)! (chọn k phần tử có thứ tự)
- Tổ hợp chập k của n: C(n, k) = n! / (k! x (n - k)!) (chọn k phần tử không thứ tự)
- Hỏi: Phân biệt khi nào dùng chỉnh hợp, khi nào dùng tổ hợp?
- Ví dụ: Từ 5 bạn, chọn 3 bạn xếp hàng → dùng gì? Chọn 3 bạn lập nhóm → dùng gì?
- Nhị thức Newton: (a + b)^n = tổng C(n, k) x a^(n-k) x b^k (k từ 0 đến n)
- Ví dụ: Khai triển (x + 1)^4.

### Xác suất

- Phép thử ngẫu nhiên, không gian mẫu (ký hiệu Omega)
- Biến cố: tập con của không gian mẫu.
- Xác suất cổ điển: P(A) = số kết quả thuận lợi / tổng số kết quả.
- Quy tắc cộng xác suất (biến cố xung khắc): P(A hợp B) = P(A) + P(B)
- Quy tắc nhân xác suất (biến cố độc lập): P(A giao B) = P(A) x P(B)
- Biến cố đối: P(A') = 1 - P(A)
- Ví dụ: Gieo 2 xúc xắc. Tính xác suất tổng bằng 7.
- Ví dụ: Rút 2 lá bài từ bộ 52 lá. Tính xác suất cả 2 là át.

### Thống kê

- Số gần đúng, sai số, sai số tuyệt đối, sai số tương đối
- Các số đặc trưng đo xu thế trung tâm: trung bình, trung vị, mốt (ôn lại từ lớp 7)
- Các số đặc trưng đo mức độ phân tán:
+ Khoảng biến thiên (range): R = giá trị lớn nhất - giá trị nhỏ nhất
+ Phương sai: S^2 = tổng (xi - trung bình)^2 / n
+ Độ lệch chuẩn: S = sqrt(phương sai)
- Hỏi: Phương sai và độ lệch chuẩn cho biết điều gì? (mức độ phân tán quanh trung bình)
- Ví dụ: Cho dãy điểm: 5, 6, 7, 8, 9. Tính trung bình, phương sai, độ lệch chuẩn.

---

## Hình học

### Vectơ

#### Khái niệm vectơ

- Vectơ: đoạn thẳng có hướng, ký hiệu AB (mũi tên từ A đến B)
- Giá của vectơ: đường thẳng chứa vectơ
- Độ dài (mô-đun) của vectơ: |AB|
- Hai vectơ cùng phương: giá song song hoặc trùng nhau
- Hai vectơ bằng nhau: cùng hướng và cùng độ dài
- Vectơ-không: có điểm đầu trùng điểm cuối, ký hiệu 0 (mũi tên)
- Hỏi: Hai vectơ cùng phương có nhất thiết bằng nhau không?
- Vectơ đối: cùng độ dài, ngược hướng

#### Phép cộng, trừ vectơ

- Quy tắc ba điểm: AB + BC = AC
- Quy tắc hình bình hành: AB + AD = AC (ABCD là hình bình hành)
- Phép trừ: AB - AC = CB
- Ví dụ: Cho tam giác ABC. Rút gọn: AB + BC + CA = ?

#### Nhân vectơ với số thực

- k x a (mũi tên): cùng hướng nếu k > 0, ngược hướng nếu k < 0, độ dài = |k| x |a|
- Vectơ cùng phương: a = k x b (với k là số thực, b khác vectơ-không)
- Trung điểm M của AB: OM = (OA + OB) / 2 (với O bất kỳ)
- Trọng tâm G của tam giác ABC: OG = (OA + OB + OC) / 3

#### Tích vô hướng của hai vectơ

- a . b = |a| x |b| x cos(góc giữa a và b)
- Tính chất: a . b = b . a; a . a = |a|^2
- Hai vectơ vuông góc khi a . b = 0
- Ví dụ: |a| = 3, |b| = 4, góc giữa a và b = 60°. Tính a . b.

### Phương pháp tọa độ trong mặt phẳng

#### Tọa độ vectơ và tọa độ điểm

- Vectơ a = (a1; a2) trong hệ tọa độ Oxy
- AB = (xB - xA; yB - yA)
- Độ dài: |AB| = sqrt((xB - xA)^2 + (yB - yA)^2)
- Trung điểm M của AB: M = ((xA + xB)/2; (yA + yB)/2)
- Trọng tâm G: G = ((xA + xB + xC)/3; (yA + yB + yC)/3)
- Tích vô hướng theo tọa độ: a . b = a1 x b1 + a2 x b2
- Hai vectơ vuông góc: a1 x b1 + a2 x b2 = 0
- Ví dụ: A(1; 2), B(4; 6). Tìm |AB| và trung điểm M.

#### Phương trình đường thẳng

- Vectơ chỉ phương u = (a; b): song song với đường thẳng
- Vectơ pháp tuyến n = (A; B): vuông góc với đường thẳng
- Phương trình tổng quát: Ax + By + C = 0
- Phương trình tham số: { x = x0 + at; y = y0 + bt } (t là tham số)
- Hệ số góc: y = kx + m (k = -A/B)
- Khoảng cách từ điểm M(x0; y0) đến đường thẳng Ax + By + C = 0:
+ d = |A.x0 + B.y0 + C| / sqrt(A^2 + B^2)
- Góc giữa hai đường thẳng: cos(alpha) = |A1.A2 + B1.B2| / (sqrt(A1^2 + B1^2) x sqrt(A2^2 + B2^2))
- Hai đường thẳng song song: A1/A2 = B1/B2 ≠ C1/C2
- Hai đường thẳng vuông góc: A1.A2 + B1.B2 = 0
- Ví dụ: Viết phương trình đường thẳng qua A(1; 2) và vuông góc với d: 3x + 4y - 5 = 0.

#### Phương trình đường tròn

- Phương trình chính tắc: (x - a)^2 + (y - b)^2 = R^2 (tâm I(a; b), bán kính R)
- Phương trình khai triển: x^2 + y^2 - 2ax - 2by + c = 0 (tâm I(a; b), R = sqrt(a^2 + b^2 - c))
- Điều kiện để là đường tròn: a^2 + b^2 - c > 0
- Vị trí tương đối giữa đường thẳng và đường tròn (tính khoảng cách d từ tâm đến đường thẳng, so sánh với R)
- Tiếp tuyến của đường tròn: d = R
- Phương trình tiếp tuyến tại điểm M(x0; y0) trên đường tròn
- Ví dụ: Tìm tâm và bán kính: x^2 + y^2 - 4x + 6y - 3 = 0.
