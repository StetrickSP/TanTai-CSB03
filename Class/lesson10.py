###Bai 1:
# f = open("names.txt","w")
# n = ["Nikki Roysden","Mervin Friedland","Aron Wilkins"]
# for i in n: 
#     f.write("-" + i + "\n")
# f = open("names.txt","r")
# print("List of names: ")
# print(f.read())

###Bai 2:
# import os
# name = input("Enter the exact name of the file: ")
# if os.path.exists(name):
#     with open(name,"r") as f:
#         print(f.read())
# else: print("File doesn't exist")

###Bai 3:
# f = open("tai.txt", "w")
# studentTai = {
#     "Name" : "Ngo Tan Tai",
#     "Class" : "PVT-CSB03",
#     "School" : "MindX Technology School"
# }
# for k,v in studentTai.items():
#     f.write(k + ": " + v + "\n")
# f = open("tai.txt", "r")
# print(f.read())

