#  python credit.py

from cs50 import get_int
h=get_int("Number:")
while h<=0 :
    print("INVALID")
    h=get_int("Number:")
 
d=1
while h//(10**(d-1))>10:
    d+=1
    
#print(d)
f=h//(10**(d-2))
#print(f)
    
if d==15 and (f==34 or f==37):
    print("AMEX")
    
elif d==16 and (f==51 or f==52 or f==53 or f==54 or f==55):
    print("MASTERCARD")

elif (d==13 or d==16)and h//(10**(d-1))==4:
    print("VISA")

else:
    print("INVALID")