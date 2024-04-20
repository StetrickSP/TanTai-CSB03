### Input kiem tra so nguyen
# try: 
#     a = float(input("Type in a number: "))
#     if a > 0: print("That number is positive.")
#     elif a < 0: print("Number's negativer.") 
#     else: print("A is 0")
# except ValueError: 
#     print("Not a number.")

### Input kiem tra Odd/Even
# try:
#     b = float(input("Type in a number: "))
#     if b % 2 == 0:
#         print("even")
#     elif b % 2 != 0:
#         print("odd")
# except ValueError:
#     print("Not a number")

### While Loop
# i = 1
# while i <= 5:
#   print(i)
#   i += 1

### While Sum of Natural numbers of 1 to 100
# i = 1
# total = 0
# while i <= 100:
#     total += i
#     i += 1
# print("Tong so la: ", total,)

### For Loops
# start = 5   # starts at 5 
# stop = 500  # stops at 499 (condition: <500)
# step = 10   # increment every addition
# number = range(start, stop, step)
# for i in number: 
#     i += 1
#     print(i)

### Bai Tap Luyen tap #### 
# 1. Viết chương trình tìm số lớn hơn trong 3 số nhập từ người dùng
# 2. Viết chương trình xác định một năm có phải năm nhuận không (Năm nhuận là năm chia hết cho 4. Trong trường hợp năm chia hết cho 100 thì phải chia hết cho 400).
# 3. Dùng vòng lặp in ra các dãy số sau (mỗi dãy số là 1 vòng lặp):
#      - 0 1 2 3 4 5 6
#      - 100 101 102 103 104 105
#      - 9 8 7 6 5 4 3 2
# 4. In ra các  số chia hết cho 3 từ 0 đến 20, mỗi số một dòng
# 5. Tính số chữ số của một số nguyên do người dùng nhập vào

##Bai 1
# try:
#     a = float(input("Nhap so thu nhat: "))
#     b = float(input("Nhap so thu hai: "))
#     c = float(input("Nhap so thu ba: "))
# except ValueError: 
#     print("Please enter all 3 numbers")
# count = a                         #count = 0 will make the code unable to analyze negative numbers
# numbers = [a, b, c]
# for i in numbers:
#     if i > count: count = i
# print("So lon nhat: ", count)

##Bai 2
# year = int(input("Nhap nam: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("la Nam nhuan.")
# else: print("Ko phai nam nhuan")

##Bai 3
i = 0
while i < 6:
    print(i)
    i += 1
        

