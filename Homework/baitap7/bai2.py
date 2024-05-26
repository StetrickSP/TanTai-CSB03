### Bài 2. Số Nguyên Tố
# Số nguyên tố là số nguyên dương lớn hơn 1, chỉ chia hết cho 1 và chính nó.
# Các số nguyên tố đầu tiên là 2, 3, 5, 7, 11, 13, 17, 19, 23, …
# Số 4 không phải số nguyên tố vì chia hết cho 2. Số 9 không phải số nguyên tố vì chia hết cho 3,…
# Yêu cầu người dùng nhập vào một số nguyên. Kiểm tra số đã nhập có phải là số nguyên tố hay không.
# Yêu cầu: Viết hàm is_prime() nhận vào một số nguyên, trả về True nếu số nhận vào là số nguyên tố, ngược lại trả về False.
# Kết quả mong đợi của chương trình:
# Ví dụ 1
# Input number: 17
# 17 is a prime
# Ví dụ 2
# Input character: 9
# 9 is not a prime
# Gợi ý: Để kiểm tra số nguyên tố, ta kiểm tra số đó có chia hết cho bất kì số nguyên > 1 nào bé hơn nó hay không. Nếu có thì số đó không phải số nguyên tố.

try:
    num = int(input("Input number: "))
    while num < 0:
        num = int(input("Input number: "))
except ValueError:
    print("Is not a number.")

def is_prime(x):
    prime = True
    non_nums = []
    for i in range(2, x, 1):
        if x % i == 0:
            non_nums.append(i)
            prime = False
    if prime == True:
        return True
    else: 
        print(x,"can be exactly divided by:", *non_nums)
        return False

if is_prime(num):
    print(num, "is a prime number.")
else: print(num, "is not a prime number")
