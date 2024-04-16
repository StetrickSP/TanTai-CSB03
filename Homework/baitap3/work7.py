###Bài 7. Tam Giác Đặc Biệt
##De bai
# Yêu cầu người dùng nhập vào 3 số thực dương là độ dài 3 đoạn thẳng. Ta kiểm tra:
# 3 đoạn thẳng đó có thể là 3 cạnh của một tam giác hay không.
# Nếu có thể tạo thành tam giác, ta tiếp tục kiểm tra các trường hợp:
# Tam giác vuông
# Tam giác đều
# Các trường hợp khác, ta coi như một tam giác bình thường.
# Nếu tam giác được tạo thành là tam giác đều, ta dùng thư viện turtle để vẽ tam giác với các kích thước được nhập.
from turtle import *

try:
    a = float(input("Enter triangle side 1: "))
    b = float(input("Enter triangle side 2: "))
    c = float(input("Enter triangle side 3: "))
    max_num = a
    sides = [a, b, c]
    if a + b > c: print("The 3 sides can form a triangle")   
    else:                                                    
        print("The 3 sides cannot form a triangle.")         
        exit()                                               
    for i in sides:                                       ##Logic: Tim canh huyen (max_num)
        if i > max_num: max_num = i                       
    if pow(a, 2) + pow(b, 2) + pow(c, 2) - pow(max_num, 2) == pow(max_num, 2):#Tinh: 
        print("This is a Right Triangle!")                                 #a^2 + b^2 + c^2 - max_num^2 == max_num^2
    elif a == b == c:
        print("This is an Equilateral Triangle!")
        pen()
        forward(a)
        left(120)
        forward(b)
        left(120)
        forward(c)
        left(120)
        mainloop()
    else: print("This is just a normal triangle.")
except ValueError: 
    print("Please enter all numbers.")
