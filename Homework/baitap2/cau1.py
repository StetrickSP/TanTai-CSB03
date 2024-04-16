###Cau 1: Hình Tròn
import math

r = float(input("Enter the Radius of the circle: "))
circum = math.pi * r * 2
area = math.pi * r * r
print("Radius: " + "\033[1m", r, "\033[0m")
print("Circumference: ", circum)
print("Area: ", area)