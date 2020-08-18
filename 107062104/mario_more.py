from cs50 import get_int

height = 0

while height <= 0 or height > 8 :

    height = get_int('height: ')

    for i in range(1, height+1) :
        s = ' ' * (height - i) + '#' * i + ' ' + '#' * i
        print(s)
