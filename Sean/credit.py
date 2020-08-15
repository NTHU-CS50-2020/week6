from cs50 import get_string


def luhn(num):
    l = list(num)
    l.reverse()
    l = list(map(int, l))
    tmp = 0
    for i in range(1, len(l), 2):
        if l[i] * 2 < 10:
            tmp += l[i] * 2
        else:
            tmp += (l[i] * 2) // 10
            tmp += (l[i] * 2) % 10
    for i in range(0, len(l), 2):
        tmp += l[i]
    return 0 if tmp % 10 else 1


n = get_string("Number: ")
if luhn(n):
    len_n = list(n)
    n = int(n)
    if len(len_n) == 15 and (n // (10**13) == 37 or n // (10**13) == 34):
        print("AMEX")
    elif len(len_n) == 13 and (n // (10**12) == 4):
        print("VISA")
    elif len(len_n) == 16:
        if n // (10**15) == 4:
            print("VISA")
        elif 51 <= n // (10**14) <= 55:
            print("MASTERCARD")
        else:
            print("INVALID")
    else:
        print("INVALID")
else:
    print("INVALID")
