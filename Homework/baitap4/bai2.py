### Bài 2. Số Dương
# Yêu cầu người dùng nhập vào một số thực. Nếu số thực này không phải số dương, yêu cầu người dùng nhập lại cho đến khi chương trình nhận được một số dương.
# Kết quả mong đợi của chương trình:
# Ví dụ 1:
# Input a positive number: 3.14
# Thank you.
# Ví dụ 2:
# Input a positive number: -3.14
# Input a positive number: 0
# Input a positive number: 100
# Thank you.

num = float(input("Input a positive number: "))
while num < 0:
    num = float(input("Input a positive number: "))
print("Thank you.")
