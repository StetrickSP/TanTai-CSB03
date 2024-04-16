###Bài 6. Tam Giác
##De bai
# Yêu cầu người dùng nhập vào 3 số thực dương là độ dài 3 đoạn thẳng. Hãy kiểm tra 3 đoạn thẳng đó có thể là 3 cạnh của một tam giác hay không.
# Kết quả mong đợi của chương trình:
# Ví dụ 1
# Input length 1: 1
# Input length 2: 2
# Input length 3: 3
# The 3 line segments cannot form a triangle.
# Ví dụ 2
# Input length 1: 2
# Input length 2: 3
# Input length 3: 4
# The 3 line segments can form a triangle.
# Gợi ý: Ta có thể kiểm tra bằng Định lý Bất đẳng thức tam giác: Trong một tam giác, tổng độ dài hai cạnh bất kỳ bao giờ cũng lớn hơn độ dài cạnh còn lại.

try:
    a = float(input("Enter triangle side 1: "))
    b = float(input("Enter triangle side 2: "))
    c = float(input("Enter triangle side 3: "))
    if a + b > c: 
        print("The 3 sides can form a triangle")
    else: print("The 3 sides cannot form a triangle")
except ValueError: print("Fuk you, enter all 3 sides with numbers, dipsht.")