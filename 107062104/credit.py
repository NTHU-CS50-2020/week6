from cs50 import get_string

def main():

    number = get_string('Number: ')

    if len(number) == 15 and number[0:1] == '34' or number[0:1] == '37' :
        print('AMEX')
    elif len(number) == 16 and number[0] == '5' and number[1] >= '1' and number[1] <= '5':
        print('MASTERCARD')
    elif isVisa(number) :
        print('VISA')
    else :
        print('INVALID')


def isVisa(number):
    if len(number) == 13 or len(number) == 16:
        sum = 0
        for i in range(len(number)):
            if i % 2 == 0:
                sum += (int(number[i]) * 2) // 10 + (int(number[i]) * 2) % 10
            else:
                sum += int(number[i])
        if sum % 10 == 0:
            return True
    return False


main()