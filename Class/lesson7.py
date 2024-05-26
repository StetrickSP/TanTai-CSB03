# nums = []
# num = int(input("Enter your number, enter 0 to end: "))
# nums.append(num)
# while num != 0:
#     num = int(input("Enter your number: "))
#     nums.append(num)
# def calculateTotal(*argv):
#     for arg in argv:
#         print(arg)
# calculateTotal(*nums)

####BAI TAP
###5. Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
# sent = input("Enter your string: ")
# def splitComma(x):
#     splitX = x.split(",")
#     splitX.sort()
#     return splitX
# print(*splitComma(sent), sep=", ")

###4. Viết function tính tổng một array nhập từ bàn phím. Nếu trong array tồn tại phần tử không phải là số, thì bỏ qua phần tử đó 
nums = []
int_nums = []

num = input("Enter your number: ")
nums.append(num)

while num != '':
    num = input("Enter your number: ")
    nums.append(num)
nums.remove('')

o = 0
for i in nums:
    try: 
        number = float(i)
        int_nums.append(number)
    except ValueError:
        print()


# def tinh_tong(nums):
#     for i in range(len(nums)):
#         tong = 0
#     if type(i) == str:
#         nums.pop(i)
#     else:
#         tong +=i
#     return tong

#! Logic:
# 
#