import math
import sys

def check(number):
    counteven = 0
    countodd = 0
    for i in range(8):
        oddnumber = int((number/(math.pow(10,(2*i))))%10)
        countodd = int(countodd + oddnumber)
        
        evennumber = int((number/(math.pow(10,(2*i+1))))%10)
        doubleeven = int(evennumber*2)
        doubleeven1 = int(doubleeven%10)
        doubleeven2 = int((doubleeven/10)%10)
        counteven = int(counteven + doubleeven1 + doubleeven2)
        
    check_num = int(counteven + countodd)
    if(check_num%10 == 0):
        return 1
    else:
        return 0 

def main():
    number = int(input("number:\n"))
    if(number < math.pow(10,12) or number > math.pow(10,16)):
        print("invalid")
        return 1
    

    if(check(number) == 1):
        print("check")
        if((int(number/math.pow(10,14))%10) == 3):
            print("AMEX")
        elif(int((number/math.pow(10,15))%10) == 5):
            print("MASTERCARD")
        elif(int((number/math.pow(10,15))%10) == 4 or int((number/math.pow(10,12))%10) == 4):
            print("VISA")
        else:
            print("invalid")
    else:
        print("invalid")



            
main()