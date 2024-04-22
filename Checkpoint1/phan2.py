###Bai 1: 3 to 12 sequence
# nums = range(3, 12 +1, 1)
# print(*nums)

###Bai 2: 0 to n sequence
# x = int(input("Input a number: "))
# while x < 0: 
#     print("Please enter a number greater than or equal to 0.")
#     x = int(input("Input a number: "))
# print(*range(0, x +1, 1))

###Bai 3: 0 to n odd sequence
# x = int(input("Input a number: "))
# while x < 0: 
#     print("Please enter a number greater than or equal to 0.")
#     x = int(input("Input a number: "))
# nums = range(0, x +1, 1)
# arr_nums = [*nums]
# for i in arr_nums:
#     if i % 2 == 0: arr_nums.remove(i)
# print(*arr_nums)

###Bai 4: Polygon with custom edge number
# from turtle import *
# pen
# n = int(input("Input number of sides: "))
# for i in range(n):
#     forward(50)
#     left(360 / n)
# mainloop()