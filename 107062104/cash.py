from cs50 import get_float

def main():

    change = -1

    while change < 0 :
        change = get_float('Change owned: ')
        
    print(Change(change * 100))

def Change(change):
    if change >= 25  :
        return Change(change - 25) + 1
    elif change >= 10:
        return Change(change - 10) + 1
    elif change >= 5 :
        return Change(change - 5)  + 1
    elif change >= 1 :
        return Change(change - 1)  + 1
    else :
        return 0

main()

