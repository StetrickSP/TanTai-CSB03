###Bài 8. In ra các số chia hết cho 3 từ 0 đến 20, mỗi số một dòng

numbers = range(0, 21, 1)
for i in numbers:
    if i % 3 == 0: print(i)