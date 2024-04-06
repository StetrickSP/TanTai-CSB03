### Bai 4: Chúc Mừng Năm Mới
# Phao hoa khong biet lam

try:
    year = int(input("What year is it?"))
    if year >= 1000 and year <= 9999:
        print("\033[1m", year, "\033[0m")
        print("HAPPY NEW YEAR" + "\n!!!", year, "!!!")
    else:
        print("Enter a Year with 4 digits.")
except ValueError:
    print("ValueError, please enter a number.")