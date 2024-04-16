###Bài 4. Chia Hết
##De bai
# Cho người dùng nhập vào một số nguyên n. Ta kiểm tra 4 trường hợp:
# n chia hết cho 3 và n chia hết cho 5
# n chia hết cho 3 nhưng không chia hết cho 5
# n chia hết cho 5 nhưng không chia hết cho 3
# n không chia hết cho 3 và không chia hết cho 5

# Kết quả mong đợi của chương trình:
# Ví dụ 1
# Input number: 15
# 15 is divisible by 3 and 5
# Ví dụ 2
# Input number: 9
# 9 is divisible by 3
# Ví dụ 3
# Input number: 10
# 10 is divisible by 5
# Ví dụ 4
# Input number: 7
# 7 is not divisible by 3 or 5

try:
    a = int(input("Enter an integer: "))
    if a % 3 == 0 and a % 5 == 0:
        print(a, "is divisible by 3 and 5")
    elif a % 3 == 0 and a % 5 != 0: 
        print(a, "is divisible by 3")
    elif a % 3 != 0 and a % 5 == 0: 
        print(a, "is divisible by 5")
    else: print(a, "is not divisible by 3 or 5")
except ValueError: print("Enter an integer, please.")

