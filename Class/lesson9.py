###Nested Dictionary
# myClass = {
#     "student1" : 
#     {
#         "name" : "huy",
#         "age" : 18
#     },
#     "student2" :
#     {
#         "name" : "tai",
#         "age" : 19
#     },

#     "student3" : 
#     {
#         "name" : "Ngoc",
#         "age" : 18
#     }
# }
# print(myClass["student3"]["name"])  ##Access into a nested dictionary
# for i, obj in myClass.items(): ##Loop through
#     print(i) 
#     for y in obj:
#         print(y + ':', obj[y])

##################################  Bai tap Thuc Hanh ####################################################

###Bài I) 
# Init dictionary - Dưới đây là thông tin về số lượng máy tính theo hãng trong 1 kho của một shop:
# HP: 20
# DELL: 50
# MACBOOK: 12
# ASUS: 30
# - Khai báo 1 dictionary để biểu diễn thông tin trên
# - Read - Hiện ra số lương MACBOOK có trong kho
# - Read - with key from input - Lặp lại câu 2 với hãng máy tính nhập bởi người dùng

##Bai lam
# myDict = {
#     "HP" : 20,
#     "DELL" : 50,
#     "MACBOOK" : 12,
#     "ASUS" : 30
# }
# print(myDict["MACBOOK"])
# k = input("Enter exactly the name of the brand: ")
# if k in myDict:
#     print(k + " has", myDict[k], "laptops")
# else: print("Brand doesn't exist")
# # for k, v in myDict.items():
# #     print(k + " has", v,"laptops")


###Bài II) 
# Init character dictionary - Dưới đây là mô tả một nhân vật trong 1 text adventure:
# Name: Light
# Age: 17
# Strength: 8
# Defense: 10
# HP: 100
# Backpack: Shield, Bread Loaf
# Gold: 100
# Level: 2
# Sử dụng 1 dictionary để mô tả nhân vật này
# - Update character dictionary - Không chỉnh sửa khai báo, thêm 50 Gold cho nhân vật này
# - Update character dictionary (2) - Không chỉnh sửa khai báo, thêm FlintStone vào Backpack của nhân vật này
# - Update character dictionary (3) - Không chỉnh sửa khai báo, thêm mô tả Pocket cho nhân vật, trong Pocket chứa 1 danh sách các vật dụng bao gồm MonsterDex và Flashlight

##Bai lam
# myChar = {
#     "Name": "Light",
#     "Age": 17,
#     "Strength": 8,
#     "Defense": 10,
#     "HP": 100,
#     "Backpack": [
#         "Shield", 
#         "Bread Loaf"
#         ],
#     "Gold": 100,
#     "Level": 2
# }
# ## - Update character dictionary -
# myChar["Gold"] += 50
# ## - Update character dictionary (2) -
# myChar["Backpack"].append("Flintstone")
# ## - Update character dictionary (3) -
# myChar["Pocket"] = ["MonsterDex", "Flashlight"]
# for k, v in myChar.items():
#     print(k + ":", v)


###Tạo một dictionary lưu trữ thông tin chi tiết về học sinh, bao gồm tên, tuổi và điểm số. Ví dụ:
# students_details = {
#     "Alice": {"age": 20, "score": 85},
#     "Bob": {"age": 22, "score": 92},
#     "Charlie": {"age": 21, "score": 78}
# }
# 1. Kiểm tra xem "David" có tồn tại trong dictionary students_details hay không. Nếu có, in ra thông tin của David. Nếu không, in ra thông báo "David không có trong danh sách".
# 2. Sắp xếp các học sinh theo điểm số giảm dần và in ra màn hình

##Bai lam
students_details = {
    "Alice": {"age": 20, "score": 85},
    "Bob": {"age": 22, "score": 92},
    "Charlie": {"age": 21, "score": 78}
}

if "David" in students_details:
    print(students_details["David"])
else: print("David is not on the list")

# counter = students_details["Alice"]["score"]
# for i in students_details:
#     if students_details[i]["score"] >= 
