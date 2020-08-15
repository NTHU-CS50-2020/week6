# from cs50 import get_int
import re

while True:
    # h = get_int("Height: ")
    h = input("Height: ")
    if re.search(r"^[+-]?\d+$", h):
        try:
            h = int(h)
            if 1 <= h <= 8:
                break
        except ValueError:
            pass

for i in range(h):
    for j in range(h-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("#", end="")
    print()