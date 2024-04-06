### Bai 2: Dang ky tai khoan

f_name = input("Please write your First Name: ")
l_name = input("Please write your Last Name: ")
p_number = input("Please write your phone number: ")

print("First name: " + "\033[1m" + f_name + "\033[0m")
print("Last name:  " + "\033[1m" + l_name + "\033[0m")
print("Phone number: " + "\033[1m" + p_number + "\033[0m")

print("Your registered name is " + f_name + " " + l_name + ".")
print("Your phone number is " + p_number + ".")