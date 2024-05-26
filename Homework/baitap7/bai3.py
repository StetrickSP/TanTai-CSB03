### Bài 3. Liệt Kê Số Nguyên Tố
# In ra màn hình n số nguyên tố đầu tiên, với n là một số nguyên dương được nhập từ người dùng.
# Kết quả mong đợi của chương trình:
# Ví dụ 1
# Input number: 1
# First 1 prime(s): 2
# Ví dụ 2
# Input number: 9
# First 9 prime(s): 2 3 5 7 11 13 17 19 23

# Gợi ý: Sử dụng hàm is_prime() để lần lượt kiểm tra tính nguyên tố của các số nguyên dương. Chương trình kết thúc sau khi tìm thấy n số nguyên tố.

n = int(input("Input number: "))
prime_nums = []
counter = 0
count_num = 2

def is_prime(x):
    for i in range(2, x, 1):
        if x % i == 0:
            return False
    return True

while counter < n:
    if is_prime(count_num) == True:
        prime_nums.append(count_num)
        count_num += 1
        counter += 1
    else: 
        count_num += 1

print("First",n,"prime number(s):",*prime_nums)