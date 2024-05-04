###Bài 3. Giai Thừa
# Giai thừa của một số nguyên dương được tính bằng tích của các số tự nhiên bé hơn hoặc bằng số đó.
# Ta ký hiệu:
# n!=1.2.3…n-1.n            (n≥1)
# Trường hợp đặc biệt:
# 0!=1                                                         
# Hãy viết một chương trình tính giai thừa của một số nguyên không âm do người dùng nhập vào. Nếu người dùng nhập vào số âm, trả về kết quả là Invalid.
# Kết quả mong đợi của chương trình:
#Ví dụ 1
# Input number: 0
# 0! = 1
#Ví dụ 2
# Input number: 4
# 4! = 24
#Ví dụ 3
# Input number: -10
# Invalid

import math 

x = int(input("Input Number: "))
try:
    fac_x = math.factorial(x)
    print(x,"!", "=",fac_x)
except ValueError: print("Invalid")
