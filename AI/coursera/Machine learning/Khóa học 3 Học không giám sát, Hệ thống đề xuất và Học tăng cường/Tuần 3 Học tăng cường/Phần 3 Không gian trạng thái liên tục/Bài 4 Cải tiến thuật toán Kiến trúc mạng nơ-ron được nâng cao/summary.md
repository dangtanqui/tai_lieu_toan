## Vấn đề kiến trúc cũ

- Input (S,A) → output 1 Q → cần **4 lần inference** mỗi state để so sánh actions
- Tính max_{A'} Q(S',A') trong Bellman cũng tốn 4 lần

## Kiến trúc nâng cao (dùng trong lab)

- Input: chỉ **8 số state**
- Hidden: 64 → 64
- Output: **4 units** — Q(S,nothing), Q(S,left), Q(S,main), Q(S,right) **cùng lúc**

## Lợi ích

- **1 lần inference** → đủ 4 giá trị Q → chọn action nhanh
- Tính max Q(S',·) trong Bellman cũng chỉ **1 lần forward**

## Bước tiếp theo

- **ε-greedy policy**: cân bằng khám phá (exploration) và khai thác (exploitation) khi thu thập kinh nghiệm
