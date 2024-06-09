##Phần 1. Thời gian: 10 phút
# myDict = {
#     "HP" : 20,
#     "DELL" : 50,
#     "MACBOOK" : 12,
#     "ASUS" : 30
# }
# print(myDict["MACBOOK"])
# k = input("Enter exactly the name of the brand: ")
# if k in myDict:
#     print("Available",k,"laptops:",myDict[k])
# else: print("Brand doesn't exist")



##Phần 2. Thời gian: 20 phút
# #Bai 1:
# myDict = {
#     "HP" : 20,
#     "DELL" : 50,
#     "MACBOOK" : 12,
#     "ASUS" : 30,
# }
# myDict["TOSHIBA"] = 10
# print("Available products: ")
# for k,v in myDict.items():
#     print("-",k,":",v)
# #Bai 2:
# myDict = {
#     "HP" : 20,
#     "DELL" : 50,
#     "MACBOOK" : 12,
#     "ASUS" : 30,
# }
# brand = input("Input a brand: ")
# amount = int(input("Input an amount: "))
# myDict[brand] = amount
# print("Available products: ")
# for k,v in myDict.items():
#     print("-",k,":",v)
# #Bai 3:
# myDict = {
#     "HP" : 20,
#     "DELL" : 50,
#     "MACBOOK" : 12,
#     "ASUS" : 30,
# }
# myDict["DELL"] = 60
# myDict["MACBOOK"] = 2
# print("Available products: ")
# for k,v in myDict.items():
#     print("-",k,":",v)
# #Bai 4
# myDict = {
#     "HP" : 20,
#     "DELL" : 50,
#     "MACBOOK" : 12,
#     "ASUS" : 30,
# }
# total = 0
# for v in myDict.values():
#     total += v
# print("Total products:",total)



##Phần 3. Thời gian: 10 phút
# myDict = {
#     "HP" : 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400
# }
# print("Price of ASUS laptops:",myDict["ASUS"])
# brand = input("Input a brand: ")
# if brand in myDict:
#     print("Price of",brand,"laptops:",myDict[brand])
# else: print("Brand doesn't exist.")



##Phần 4. Thời gian: 15 phút
# myDict = {
#     "HP" : 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400
# }
# myLaps = {
#     "HP" : 20,
#     "DELL" : 50,
#     "MACBOOK" : 12,
#     "ASUS" : 30,
# }
# #Bai 1:
# print("Total price of 5 ASUS laptops:",myDict["ASUS"]*5)
# #Bai 2:
# brand = input("Input a brand: ")
# amount = int(input("Amount to buy: "))
# if brand in myDict:
#     print("Total price:",myDict[brand]*amount)
# else: print("Brand doesn't exist")
# #Bai 3:
# if brand in myLaps:
#     myLaps[brand] -= amount
# print("Available products: ")
# for k,v in myLaps.items():
#     print("-",k,":",v)



##Phần 5. Thời gian: 10 phút
# myPrices = {
#     "HP" : 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400
# }
# myLaps = {
#     "HP" : 20,
#     "DELL" : 50,
#     "MACBOOK" : 12,
#     "ASUS" : 30,
# }
# #Bai 1:
# print("Total value of each available brands: ")
# for k in myLaps.keys():
#     print("-",k,":",myPrices[k]*myLaps[k])
# #Bai 2:
# total = 0
# for k in myLaps.keys():
#     total += myPrices[k]*myLaps[k]
# print("Total value of all available items:",total)



##Phần 6. Thời gian: 15 phút
# #Bai 1:
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
# #Bai 2:
# myChar["Gold"] += 50
# #Bai 3:
# myChar["Backpack"].append("Flintstone")
# for k, v in myChar.items():
#     print(k + ":", v)



###Phần 7. Thời gian: 10 phút
# mySkills = {
#     "Skill 1": {
#         "Name": "Tackle", 
#         "Minimum level": 1,
#         "Damage": 5,
#         "Hit rate": 0.3
#         },
#     "Skill 2": {
#         "Name": "Quick Attack",
#         "Minimum level": 2,
#         "Damage": 3,
#         "Hit rate": 0.5
#         },
#     "Skill 3": {
#         "Name": "Strong Kick",
#         "Minimum level": 4,
#         "Damage": 9,
#         "Hit rate": 0.2
#         }
# }
# for k,v in mySkills.items():
#     print("-",k,":",v["Name"])



###Phần 8. Thời gian: 20 phút
# import random
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
# mySkills = {
#     "Skill 1": {
#         "Index" : 1,
#         "Name": "Tackle", 
#         "Minimum level": 1,
#         "Damage": 5,
#         "Hit rate": 0.3
#         },
#     "Skill 2": {
#         "Index" : 2,
#         "Name": "Quick Attack",
#         "Minimum level": 2,
#         "Damage": 3,
#         "Hit rate": 0.5
#         },
#     "Skill 3": {
#         "Index" : 3,
#         "Name": "Strong Kick",
#         "Minimum level": 4,
#         "Damage": 9,
#         "Hit rate": 0.2
#         }
# }
# #Bai 1:
# for k,v in mySkills.items():
#     print("-",k,":",v["Name"])
# skill_num = int(input("Choose skill by number (1->3): "))
# for k,v in mySkills.items():
#     if v["Index"] == skill_num:
#         print("You chose",v["Name"])
#         if myChar["Level"] >= v["Minimum level"]:  ##Bai 2:
#             ran = random.random()         
#             # print(ran)
#             if ran < v["Hit rate"]:
#                 print("Damage:",v["Damage"])
#             else: print("Attack missed.")
#         else: print("Cannot deployed. Required level",v["Minimum level"])
