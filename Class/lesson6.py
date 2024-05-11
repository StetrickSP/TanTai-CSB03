###Lists and list-related functions
# students = ["ngoc", "huybede", "taichodien", "hieuthuhai"]
# print(students[1])

# students[0] = "ngocdeptrai"  #Change a specific value of an item in a list
# print(students[0])

# students.append("khoiMap")  #Add an item at the end of the list
# print(students) 

# students.insert(3, "khoiGay")  #Insert an item at a specific position of the list
# print(students)

# nums = [1, 2, 3]
# students.extend(nums)      #Add another list into the original list
# print(*students)
# newList = students + nums  #Add 2 lists toghether
# print(newList)

# students.remove("huybede")  #Remove a specific item
# print(students)

# students.pop(1)   #Remove an item at a specific position
# print(*students)
# del students[3]   #Remove an item at a specific position
# print(students)

######################################
###Bai tap thuc dung
##Bai 1:
# menu = ["pho bo tai", "pho gau", "pho nam", "pho huy"]
# print(*menu)
# order = []
# x = input("Ban muon an gi?")
# order.append(x)
# end = False
# while end != True:
#     y = input("Ban goi them mon khong? (Khong/Co)")
#     if y == "Khong": end = True
#     else: 
#         end = False
#         x = input("Ban muon an gi?")
#         order.append(x)
# for i in order:
#     print(i)

##Bai 2: Tính tổng các số trong một list (List nhập từ bàn phím)
# input_str = input("Nhap vao cac so cua list: ")
# user_list = input_str.split()

# for i in range(len(user_list)):
#     user_list[i] = int(user_list[i])

# def totalNums(x):
#     sum = 0
#     for i in x:
#         sum += i
#     return sum

# print(totalNums(user_list))

##Bai 3: Tìm số lớn nhất trong một list (List nhập từ bàn phím)
# nums = [30, 290, 12, 8, 300]
# def findLargest(x):
#     max = x[0]
#     for i in x:
#         if max < i: max = i
#     return max
# print(findLargest(nums))

##Bai 4: Sắp xếp các số trong list theo thứ tự tăng dần (không dùng hàm sort, sorted, List nhập từ bàn phím))
# nums = [30, 290, 12, 8, 300]
# def sortAscending(x):
#     count = x[0]
#     for i in x:
