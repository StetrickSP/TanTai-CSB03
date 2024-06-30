###Bai 1:
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# print(a, "+", b,"=", a + b)

###Bai 2:
# import math
# a = int(input("Input a: "))
# b = int(input("Input b: "))
# c = int(input("Input c: "))

# dis = b*b - 4*a*c
# sqrt_val = math.sqrt(abs(dis)) 

# if dis > 0: 
#     print("The equation has 2 answers: ") 
#     print((-b + sqrt_val)/(2 * a)) 
#     print((-b - sqrt_val)/(2 * a)) 
# elif dis == 0:
#     print("The equation has 2 answers with the same value") 
#     print(-b / (2 * a)) 
# else:
#     print("No real answers") 
#     print(- b / (2 * a), + "i", sqrt_val / (2 * a)) 
#     print(- b / (2 * a), - "i", sqrt_val / (2 * a)) 


###Bai 3:
# def isPalindrome(x):
#         x = str(x)
#         rvr_x = x[::-1]
#         return True if rvr_x == x else False
# st = input("Enter your string (without using capitalized letters): ")
# print("This is a palindrome. ") if isPalindrome(st) == True else print("This is not a palindrome.")

###Bai 4:
# print("== Welcome to MindX Restaurant")
# any_else = ""
# orders = []

# order = input("Please choose a dish: ")
# orders.append(order)
# any_else = int(input("Great choice! Anything else? (0: No / 1: Yes)"))

# while any_else != 0:  
#     order = input("Please choose a dish: ")
#     if order in orders:
#         print("You chose this already.")
#     else: 
#         orders.append(order)
#     any_else = int(input("Great choice! Anything else? (0/1)"))

# print(any_else)
# print("Well Done! Your order: ")
# for i in orders:
#     print("-", i)


###Bai 5:
# mydict = {
# 'Iphone12' : 28000000,
# 'Samsung N10': 16000000,
# 'Oppo 93': 7500000,
# 'Vsmart': 7400000,
# 'Vivo': 4200000
# }
# new_d = {

# }
# name = str(input('Input name of a phone: '))
# if name in mydict:
#     print("Price of Vsmart:", mydict[name])
# else :
#     print('we dont have this phone ')

# prize= int(input('Input your budget: '))
# print("Phones that fit your budget: ")
# for x,y in  mydict.items():
#     if y < prize:
#         new_d[x]=y
# print(new_d)


###Bai 6:
# num = int(input("Enter an integer greater than 0: "))
# while num <= 0:
#     num = int(input("Enter an integer greater than 0: "))
# output = list(map(int, str(num)))
# print("This number has", len(output), "digit(s).")

###Bai 7:
# l = [5,1,8,92,-1,30] 
# print("Original List:", *l)
# def sort_ascending(l1):
#     for i in range(0, len(l1)):
#         for j in range(i+1, len(l1)):
#             if l1[i] >= l1[j]:
#                 l1[i], l1[j] = l1[j],l1[i]
#     return l1
# print("Sorted List", *sort_ascending(l))

###Bai 8:
# n = int(input("Input a number: "))
# def fiboSequence(x):
#     a, b = 0, 1         
#     y = []              
#     for i in range(x):
#         a, b = b, a + b                            
#         y.append(a)      
#     return y             
# print("First",n,"Fibonacci number(s): ", *fiboSequence(n))