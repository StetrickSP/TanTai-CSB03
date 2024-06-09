###Phần 1. Thời gian: 10 phút
# ##1. Init color list
# colors = ["blue", "teal", "green", "red"]
# ##2. Print color list 
# print("Color list: ", *colors)
# ##3. Update color list
# new = input("Input new color: ")
# colors.append(new)
# print("New color list: ", *colors)


###Phần 2. Thời gian: 15 phút
##1. Read color list
# colors = ["blue", "teal", "green", "red"]
# print("Color list: ", *colors)
# check = int(input("Input position: "))
# print("Color at position",check,":", colors[check-1])

##2. Remove color
# colors = ["blue", "teal", "green", "red"]
# print("Color list: ", *colors)
# delete = input("Item to delete: ")
# try: 
#     del_int = int(delete)
#     colors.pop(del_int-1)
# except ValueError:
#     colors.remove(delete)
# print("New color list: ", *colors)


###Phần 3. Thời gian: 15 phút
##1. Search number in list
# nums = [5, 1, 8, 92, -1, 30]
# print("Numbers: ",nums)
# check = int(input("Input a number: "))
# try:
#     print("Number found at position",nums.index(check))
# except ValueError: print("Number not found.")

##2. Sum number in list
# nums = [5, 1, 8, 92, -1, 30]
# print("Numbers: ",nums)
# print("Sum of all numbers: ", sum(nums))

##3. Sum number in list (2)
# print("Input the list of numbers.")
# print("Enter 0 to finish.")
# nums = []
# num = int(input(""))
# nums.append(num)
# while num != 0:
#     num = int(input(""))
#     nums.append(num)
# print("Sum of numbers in list: ",sum(nums))


###Phần 4. Thời gian: 10 phút
##1. Even filter
# nums = [5, 1, 8, 92, 7, 30]
# even_nums = []
# for i in nums:
#     if i % 2 == 0:
#         even_nums.append(i)
# print("Even numbers: ", *even_nums)

##Even filter (2)
# print("Input the list of numbers.")
# print("Enter 0 to finish.")
# nums = []
# even_nums = []

# enter = int(input(""))
# nums.append(enter)

# while enter != 0:
#     enter = int(input(""))
#     nums.append(enter)
# nums.remove(0)

# for i in nums:
#     if i % 2 == 0:
#         even_nums.append(i)

# print("Even numbers: ", *even_nums)


###Phần 5. Thời gian: 15 phút
##1. Init list of district names and population
districts = {                                ##Access value of key: dict[key]
    "BĐ": 247100,                             #Get values of all keys: dict.values()
    "BTL": 333300,                            #Get all keys:values as pairs (as a tuple): dict.items()
    "CG ":266800,
    "ĐĐ": 420900,
    "HBT":318000
}
##2. Search max & min population
popu = [*districts.values()]
count = 0
most = max(popu)
least = min(popu)

print("Indices of: ")
for i in districts:
    if districts[i] == least: print("- Least populated district: ", count)
    elif districts[i] == most: print("- Most populated district: ", count)
    count += 1

##3. From district index to name
print("Names of: ")
for i in districts:
    if districts[i] == least: print("- Least populated district: ", i)
    elif districts[i] == most: print("- Most populated district: ", i)


###Phần 6. Thời gian: 15 phút
##1. Population density
# districts = {
#     "BĐ": 247100/9.224,
#     "BTL": 333300/43.35,
#     "CG ":266800/12.04,
#     "ĐĐ": 420900/9.96,
#     "HBT":318000/10.09
# }
# print("Population density of: ")
# for i in districts:
#     print("-",i,":",districts[i])

# ##2. Average population density
# avg_density = sum(districts.values()) / len(districts) 
# print(avg_density)

###Phần 7. Thời gian: 10 phút
# score  = [70,90,76]
# inpscore = int(input('input new score: '))
# score.append(inpscore)
# score.sort(reverse=True)
# print(score)
# stt  = 0
# for i in score:
#     stt+=1
#     print(stt,':',i)
#  p8.2