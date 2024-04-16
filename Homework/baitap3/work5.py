###Bài 5. Đăng Nhập
##De bai
# Bạn đang viết hệ thống đăng nhập cho một công ty bảo mật nổi tiếng. Người dùng cần nhập đúng tên tài khoản và mật khẩu đã có để vào hệ thống. Trong quá trình phát triển, công ty có một tài khoản dùng chung với tên tài khoản là admin và mật khẩu là 12345.
# Hãy viết chương trình yêu cầu người dùng nhập vào tên tài khoản và mật khẩu, sau đó đối chiếu với tài khoản dùng chung để quyết định người dùng có được đăng nhập hay không.
# Kết quả mong đợi của chương trình:
# Ví dụ 1
# Welcome to The Ultimate Sercurity System
# Username: admin
# Password: 12345
# You are logged in, admin.
# Ví dụ 2
# Welcome to The Ultimate Sercurity System
# Username: admin
# Password: 123456
# Wrong username or password.

print("Welcome to The Ultimate Sercurity System")
name = input("Please enter your username: ")
pw = input("Please enter your password: ")
if name == "admin" and pw == "12345":
    print("Welcome to The Ultimate Sercurity System")
    print("Username: ", name)
    print("Password: ", pw)
    print("You are logged in, admin.")
else: 
    print("Welcome to The Ultimate Sercurity System")
    print("Username: ", name)
    print("Password: ", pw)
    print("Wrong username or password.")

