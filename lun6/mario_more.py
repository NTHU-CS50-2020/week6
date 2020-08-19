#h=int(input("Height:"))
from cs50 import get_int
h=get_int("Height:")
while not(h>0) or h>8:
    print("invalid")
    h=get_int("Height:")
for i in range(h):
    print(f" "*(h-i-1),"#"*(i+1)," ","#"*(i+1)," "*(h-i-1))
