### Bài 4. Tổng Chữ Số
# Yêu cầu người dùng nhập vào một số nguyên dương. Hãy tính tổng các chữ số của số đó.
# Ví dụ: Số 314 có tổng các chữ số là 3 + 1  + 4 = 8.
# Kết quả mong đợi của chương trình:
# Ví dụ 1
# Input number: 111
# Sum of digits of 111 = 3
# Ví dụ 2
# Input number: 123456789
# Sum of digits of 123456789 = 45

def splitInteger(x):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    return digits[::-1]

num = int(input("Input Number: "))
sum = 0
split_num = splitInteger(num)
for i in split_num:
    sum += i
print(sum)
    

