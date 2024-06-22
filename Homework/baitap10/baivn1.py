###Bai 1: Huyさんはゲイです。：）
# with open("user-inputs.txt","a") as f:
#     count_enter = 0
#     while count_enter < 2:
#         a = input("Enter your words: ")
#         f.write(a + "\n")
#         count_enter += 1
#     f.close()
# with open("user-inputs.txt","r") as f:
#     print(f.read())
#     f.close()


###Bai 2:　Huyen先生は悪魔です。;(
# import datetime
# date = datetime.datetime.now()

# with open("counter.txt","r") as f:
#     a = int(f.read())
#     a += 1
#     with open("input-logs.txt","a") as f:
#         count_enter = 0
#         f.write("== Inputs at " + str(date) + " ==" + "\n")
#         if a == 1: f.write("First run" + "\n")
#         elif a == 2: f.write("Second run"+ "\n")
#         elif a == 3: f.write("Third run"+ "\n")
#         else: f.write(str(a) + "th run \n")
#         while count_enter < 2:
#             st = input("Enter your words: ")
#             f.write(st + "\n")
#             count_enter += 1
#         f.close()
#     with open("counter.txt","w") as f:
#         f.write(str(a))
#         f.close()
#     f.close()

# with open("input-logs.txt","r") as f:
#     print(f.read())
#     f.close()


###Bai 3:
# with open("question-bank.txt","r") as f:

#     txtList = []
#     quess = {}
#     ans = {}
#     user_ans = {}

#     for i in f.readlines():
#         res1 = i.strip()
#         res2 = res1.split(",")
#         txtList.append(res2)
#     for i in range(len(txtList)):
#         quess[i] = txtList[i][0]
#         ans[i] = int(txtList[i][1])
#     print("Give the correct answers to get points.")
#     for k,v in quess.items():
#         answer = int(input(v))
#         user_ans[k] = answer
#     ##The Minigame part
#     points = 0
#     for k,v in user_ans.items():
#         if user_ans[k] == ans[k]:
#             points += 1
#     print("== You got ", points, "/", len(quess), "points! ==")

#     f.close()
