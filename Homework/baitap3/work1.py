###Bài 1. Chẵn Lẻ
##De bai
# Yêu cầu người dùng nhập vào một số nguyên. Hãy kiểm tra tính chẵn lẻ của số nguyên đó.
# Kết quả mong đợi của chương trình như sau:
# Ví dụ 1
# Input number: 4
# 4 is even
# Ví dụ 2
# Input number: 5
# 5 is odd
# Với phần in đậm là nội dung được nhập từ người dùng.
# Gợi ý: Ta có thể kiểm tra số chẵn bằng tính chất số chẵn chia hết cho 2.

a = int(input("Enter your number: "))

print("Input: "+"\033[1m", a, "\033[0m")
if a % 2 == 0:
    print("Number is even")
else: 
    print("Number is odd")