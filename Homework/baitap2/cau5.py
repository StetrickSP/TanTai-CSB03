###Bài 5. Lãi Suất

A = float(input("Enter the amount you want to deposit: "))

one_year = (A * 105) / 100
two_year = (A * pow(105, 2)) / pow(100, 2)
ten_year = (A * pow(105, 10)) / pow(100, 10)

print("Your money after 1 year: ", one_year)
print("Your money after 2 years: ", two_year)
print("Your money after 10 years: ", ten_year)