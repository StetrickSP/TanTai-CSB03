### Bài 5. Số May Mắn
# Các nước phương Đông thường quan niệm số 9 là một số may mắn. Hãy tìm 10 số tự nhiên đầu tiên có 4 chữ số và có tổng các chữ số bằng 9.
# Kết quả mong đợi của chương trình:
# Numbers with sum of digits = 9:
# 1008 1017 1026 1035 1044 1053 1062 1071 1080 1107
import random

nums = range(1000,9999+1,1)
count = 0
arr9 = []

def splitInteger(x):
    digits = []
    sum = 0
    while x > 0:
        digits.append(x % 10)
        x //= 10
    for i in digits: sum += i
    return sum

for i in nums: 
    if splitInteger(i) == 9 and count <= 9:
        arr9.append(i)
        count += 1

print("Numbers with sum of digits = 9:")
print(*arr9)
