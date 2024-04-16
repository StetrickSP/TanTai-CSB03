###Bài 3. Ký Tự
##De Bai
# Yêu cầu người dùng nhập vào một ký tự. Hãy kiểm tra ký tự đó có phải là một chữ số hay không.
# Kết quả mong đợi của chương trình:
# Ví dụ 1
# Input character: 3
# '3' is a digit
# Ví dụ 2
# Input character: m
# 'm' is not a digit

a = input("Enter your type of data: ") ##Logic: Cho nguoi dung nhap so...
try:
    int(a)                             #+Truong hop la so: int(a) se khong loi ValueError va print ra a is a digit 
    print("'",a,"'", "is a digit")
except ValueError:                     #+Truong hop khong phai la so: int(a) se bi ValueError va print a is not a digit
    print("'",a,"'", "is not a digit")
