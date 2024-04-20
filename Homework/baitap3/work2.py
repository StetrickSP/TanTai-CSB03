###Bài 2. Số Nguyên
##De bai
# Yêu cầu người dùng nhập vào một số thực. Hãy kiểm tra số thực đó có phải là số nguyên hay không.
# Kết quả mong đợi của chương trình:
# Ví dụ 1
# Input number: 3
# 3 is an integer
# Ví dụ 2
# Input number: 3.14
# 3.14 is not an integer
# Gợi ý: Ta có thể lấy phần nguyên của một số thực bằng hàm int() hoặc phép chia lấy nguyên // cho 1.

try:
    a = float(input("Enter your type of data: "))
    b = int(a)
    if b / a == 1:                                 ##Logic: Lay so nguyen int duoc lam tron cua input chia
        print(a, "is an integer")                  ##cho chinh so ban dau cua no: 
    else: print(a, "is not an integer")            #+Truong hop la so nguyen: int(a) / float(a) == 1
except ValueError:                                 #+Truong hop khong phai la so nguyen: int(a) / float(a) < 1
    print(a, "is not an integer")