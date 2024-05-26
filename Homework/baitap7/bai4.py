### Bài 4. Biểu Thức Đặc Biệt
# Viết chương trình tính giá trị của biểu thức sau, với n là một số nguyên dương được nhập từ người dùng.
# 1!/1 + 2!/2 + ... + n!/n
# Kết quả mong đợi của chương trình:
# Ví dụ 1
# Input number: 1
# Result: 1

# Ví dụ 2
# Input number: 2
# Result: 2

# Ví dụ 3
# Input number: 5
# Result: 34

# Gợi ý: Viết hàm tính giai thừa để đưa vào vòng lặp tính tổng lớn.

n = int(input("Input number: "))
total = 0

def factorial(x):
    fact = 1
    for i in range(1, x+1, 1):
        fact *= i
    return fact

for i in range(1, n+1, 1):
    total += factorial(i) / i

print("Result:",int(total))