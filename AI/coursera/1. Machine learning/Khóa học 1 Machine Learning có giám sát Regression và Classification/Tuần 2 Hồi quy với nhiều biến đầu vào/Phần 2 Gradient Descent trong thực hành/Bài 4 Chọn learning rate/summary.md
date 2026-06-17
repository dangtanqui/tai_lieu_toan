## Chọn α

**α quá lớn:**
- J nhảy lên xuống / tăng liên tục
- Có thể bug (thiếu dấu **−** trong update)

**α quá nhỏ:**
- J giảm mỗi bước nhưng **rất chậm**

## Debug tip
- Set α **rất nhỏ** → J phải giảm **mọi** iteration
- Nếu vẫn tăng → **bug code**

## Cách chọn α thực tế
1. Thử dãy: 0.001 → 0.003 → 0.01 → 0.03 → 0.1... (~×3 mỗi lần)
2. Chạy vài iteration, plot learning curve
3. Chọn α **lớn nhất** mà J vẫn giảm ổn định
