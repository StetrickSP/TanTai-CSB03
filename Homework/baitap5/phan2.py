###Bài 1. Mảng Mới
##Cho một mảng các số nguyên được lưu dưới dạng cấu trúc dữ liệu list như sau:
## arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
## Hãy dùng kiến thức đã học để tạo các list mới dựa vào mảng đã cho, với tính chất:
## Mảng cộng 2: Chứa các giá trị lớn hơn giá trị trong mảng đã cho 2 đơn vị
## Mảng nhân 2: Chứa các giá trị gấp đôi giá trị trong mảng đã cho
## Mảng dịch 2: Chứa các giá trị như mảng đã cho, nhưng dịch chuyển 2 vị trí về bên trái. 2 giá trị đầu tiên được đưa về cuối mảng.
## Kết quả mong đợi của chương trình như sau:
##   Original list : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##   Add 2         : [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
##   Multiply by 2 : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
##   Shift 2       : [2, 3, 4, 5, 6, 7, 8, 9, 0, 1]

# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# def arrAdd2(x):
#     y = x.copy()
#     for i in y:
#         y[i] += 2
#     return y

# def arrTimes2(x):
#     y = x.copy()
#     for i in y:
#         y[i] *= 2
#     return y

# def arrShift2(x):
#     y = x.copy()
#     element1 = y.pop(y[1])
#     element2 = y.pop(y[0])
#     y.append(element2)
#     y.append(element1)
#     return y

# print("Original List: ", arr)
# print("Add 2:   ", arrAdd2(arr))
# print("Multiply by 2: ", arrTimes2(arr))
# print("Shift 2: ", arrShift2(arr))




###Bài 2. Mật Mã
## Cho một mảng chứa thông tin của một chuỗi ký tự đã được mã hóa như sau:
## arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l',
##             'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']
## Hãy tìm quy luật mã hóa và xây dựng lại chuỗi ký tự ban đầu. Kết quả mong đợi của chương trình là chuỗi ký tự trước khi được mã hóa.

# arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l','o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']
# arr.reverse()
# print(*arr)




### Bài 3. Fibonacci
## Dãy Fibonacci là một dãy vô hạn các số nguyên với tính chất: Giá trị của một phần tử bằng tổng giá trị hai phần tử đứng trước nó.
## Dãy Fibonacci bắt đầu bằng hai phần tử có giá trị 1 và có các phần tử đầu tiên như sau:
## 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
## Hãy viết một chương trình in ra n phần tử đầu tiên của dãy Fibonacci, với n là một số nguyên dương do người dùng nhập.
## Kết quả mong đợi của chương trình:
## Ví dụ 1
## Input a positive number: 1
## First 1 Fibonacci number(s): 1
## Ví dụ 2
## Input a positive number: 10
## First 10 Fibonacci number(s): 1 1 2 3 5 8 13 21 34 55

# n = int(input("Input a positiver number: "))
# def fiboSequence(x):
#     a, b = 0, 1
#     y = []
#     for i in range(x):
#         a, b = b, a + b
#         y.append(a)
#     return y
# print("First",n,"Fibonacci number(s): ", *fiboSequence(n))
    



###Bài 4. Ngày Nhận Lương
## Hôm nay là ngày nhận lương của Bình. Bình tự thưởng cho mình bằng cách ăn một bữa thật ngon ở nhà hàng.
## Thực đơn của nhà hàng bao gồm n món với các giá khác nhau. Bình chỉ muốn chọn món ăn từ các món có giá trên trung bình. Hãy viết chương trình giúp Bình tìm giá trung bình và lọc ra các món có giá trên trung bình từ thực đơn.
## Kết quả mong đợi của chương trình:
##   Number of items: 6
##   Item 1: Ribeye Steak
##   Price of item 1: 30.5
##   Item 2: Potato Salad
##   Price of item 2: 5
##   Item 3: Sparkling Wine
##   Price of item 3: 7
##   Item 4: Smoked Salmon
##   Price of item 4: 12
##   Item 5: Chicken Soup
##   Price of item 5: 8.5 
##   Item 6: Tiramisu Cake
##   Price of item 6: 4.5
##   Average price: 11.25
## Item(s) above average price: ('Ribeye Steak', 30.5) ('Smoked Salmon', 12.0)
## Với phần in đậm là nội dung được nhập từ người dùng.
## Gợi ý: Sử dụng list để lưu danh sách các món ăn. Mỗi phần tử trong list là một tuple chứa thông tin của một món ăn, bao gồm tên và giá.

#! Logic: 
#! for i in range(n) => Enter dishes:prices 
#! => print Dishes = {...} 
#! => calc & print avg.prices 
#! => for i in dishes: if price > avg.price: print(...)

# dishes = {}
# count = 0
# n = int(input("Number of items: "))

# for i in range(n):                       #EX: "for in in range(n)" se lap lai qua trinh n lan
#     key = input("Item"+": ")
#     value = float(input("Price of item"+": "))
#     dishes[key] = value
# print("")
# print("------ Menu ------")
# for i in dishes:                         #EX: "i" o day se chi toi "key" cua tung phan tu trong dishes 
#     count += 1                           
#     print("Item",count,":",i)
#     print("Price of item",count,":",dishes[i]) #EX: "dishes[i]" moi chi toi "value" cua tung phan tu trong dishes

# prices = [*dishes.values()]           #EX: "dishes.values()" se lay tat ca cac "values" trong "dishes"
# avg = sum(prices) / n                 #^^: "*dishes.values()" se nhan vao tat ca cac gia tri "values" vao "prices"
# print("Average price: ", avg)

# dishes_abvavg = {}
# for i in dishes:
#     if dishes[i] > avg: 
#         dishes_abvavg.update({i:dishes[i]})  #EX: thisdict.update({key:value})
# print("Item(s) over average price: ",dishes_abvavg)




###Bài 5. Đếm Từ
## Cho một câu bao gồm nhiều từ được nhập từ người dùng. Hãy đếm số từ xuất hiện trong câu đó. Nếu một từ xuất hiện nhiều hơn 1 lần, ta chỉ đếm 1.
## Để đơn giản, người dùng chỉ nhập các chữ cái viết thường và dấu cách, không nhập chữ viết hoa và các dấu câu khác.
## Kết quả mong đợi của chương trình:
## Ví dụ 1
## Write a sentence: welcome to programming with python
## Number of unique words: 5
## Ví dụ 2
## Write a sentence: the quick brown fox jumps over the lazy dog 
## Number of unique words: 8
## Gợi ý: Để xử lý, ta chuyển string mà người dùng nhập vào thành một list các string nhỏ hơn, mỗi phần tử trong list là một từ.
## input_str = 'welcome to programming with python'
## word_list = input_str.split(' ')
## print(word_list)
## >>> ['welcome', 'to', 'programming', 'with', 'python']

#! Logic: 
#! str = input("...") => str.split(" ") 
#! => Turn str into a "set" (remove duplicates) 
#! => print len(str)

# print("*Please do not type in capitalized letters, punctuations and/or symbols")
# x = input("Write a sentence: ")
# word_list = x.split()
# unique = set(word_list)
# print("Number of unique words: ",len(unique))