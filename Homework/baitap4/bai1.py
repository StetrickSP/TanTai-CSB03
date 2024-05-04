### Bài 1. Cầu Thang
# Yêu cầu người dùng nhập vào một số nguyên dương là số bậc của một cầu thang. In ra màn hình cầu thang có số bậc tương ứng theo định dạng bên dưới.
# Kết quả mong đợi của chương trình như sau:
# Ví dụ 1
# Ví dụ 2
# Input number: 1
# #
# Input number: 5
# #
# ##
# ###
# ####
# #####
# Với phần in đậm là nội dung được nhập từ người dùng.
# arr = [1, 4, 5]
# print(*arr)

num = int(input("Input number: "))
r_num = range(1, num+1, 1)
for i in r_num:
    print("#" * i)
