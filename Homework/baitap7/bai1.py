### Bài 1. Số Nguyên
# Yêu cầu người dùng nhập vào một số thực. Hãy kiểm tra số thực đó có phải là số nguyên hay không.
# Yêu cầu: Viết hàm is_int() nhận vào một số thực. Hàm trả về True nếu số nhận vào là số nguyên, ngược lại trả về False. Khi đó ta có thể sử dụng hàm như sau:
#   if is_int(num):
#     print(f'{int(num)} is an integer')
#   else:
#     print(f'{num} is not an integer')
# Kết quả mong đợi của chương trình:
# Ví dụ 1
# Input number: 3
# 3 is an integer
# Ví dụ 2
# Input number: 3.14
# 3.14 is not an integer
# Với phần in đậm là nội dung được nhập từ người dùng.

try: 
    num = float(input("Input number: "))
except ValueError:
    print("Not a number.")

def is_int(x):
    y = int(num)
    if y / x == 1:
        return True
    else:
        return False

if is_int(num):
    print(f'{int(num)} is an integer')
else:
    print(f'{num} is not an integer')
