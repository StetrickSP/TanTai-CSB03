###Phần 1

##Bai 1
# num = int(input("Input number: "))
# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else: return False
# if is_even(num):
#     print("This number is even.")
# else: print("This number is not even.")

##Bai 2
# import math
# r = float(input("Input radius: "))
# def cal_area(x):
#     area = pow(r, 2) * math.pi
#     return area
# print("Circle's area:",cal_area(r))

##Bai 3
# a = input("Input a text: ")
# def reverse_str(x):
#     txt = x[::-1]
#     return txt
# print("Reversed text: ",reverse_str(a))

##Bai 4
# a = input("Input a text: ")
# def is_palidrome(x):
#     txt = x[::-1]
#     if txt == x:
#         return True
#     else: return False
# print(is_palidrome(a))

#######################################################################################################

###Phần 2

##Bai 1 
# n = int(input("Input a number: "))
# def factorial(x):
#     fact = 1
#     for i in range(1, x+1, 1):
#         fact *= i
#     return fact
# print(n,"! =",factorial(n))

##Bai 2
# l = [5, 1, 8, 92, -1, 30] 
# print("Original List:", *l)
# def sort_ascending(l1):
#     for i in range(0, len(l1)):
#         for j in range(i+1, len(l1)):
#             if l1[i] >= l1[j]:
#                 l1[i], l1[j] = l1[j],l1[i]
#     return l1
# print("Sorted List", *sort_ascending(l))

##Bai 3
# n = int(input("Input a number: "))
# def fiboSequence(x):
#     a, b = 0, 1         
#     y = []              
#     for i in range(x):
#         a, b = b, a + b                            
#         y.append(a)      
#     return y             
# print("First",n,"Fibonacci number(s): ", *fiboSequence(n))

#######################################################################################################

###Phần 3.  

##Bai 1:
# num = int(input("Input a number: "))
# def myFunc(x):
#     n = x - 17
#     ans = 0
#     if n >= 0:  
#         ans = n * 2
#     else: 
#         ans = abs(n)
#     return ans
# print(myFunc(num))


##Bai 2: 
# x = (2024, 7, 2) 
# a = (2024, 7, 9) 
# def ngay(x, a):
#     if x[2] > a[2]:
#         return x[2]-a[2]
#     else:
#         return a[2]-x[2]
# print(ngay(x, a))

##Bai 3:
# arr = input("Input list:")
# x = arr.split()
# def count4(l):
#     counter = 0
#     for i in arr:
#         if i == "4":
#             counter += 1
#     return counter
# print("There are",count4(x),"numbers 4 in the list")

##Bai 4:
# arr = input("Input list:")
# x = arr.split()
# y = []
# for i in x:
#     z = int(i)
#     y.append(z)
# def output(l):
#     for i in l:
#         if i % 2 == 0:
#             print(i)
#         elif i == 237:
#             break
# output(y)

##Bai 5:
# char = input("Character to print: ")
# arr = input("Numbers: ")
# x = arr.split()
# y = []
# for i in x:
#     z = int(i)
#     y.append(z)
# def drawHistro(a, l):
#     for i in l:
#         print(a * i)
# drawHistro(char, y)
