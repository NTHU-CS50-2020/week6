# quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢)
# 0.01 0.05 0.1 0.25
from cs50 import get_float
d=get_float("Change owed:")
while not(d>0):
    print("invalid")
    d=get_float("Change owed:")

c= round(d* 100)
print(c//25+c%25//10+c%25%10//5+c%25%10%5//1)