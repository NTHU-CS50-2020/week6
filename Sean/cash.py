from cs50 import get_float


def cal(a, b, n):
    a += b // n
    b %= n
    return a, b


while True:
    c = get_float("Change owed: ")
    if c >= 0:
        break
c = round(100 * c)
tmp = 0

tmp, c = cal(tmp, c, 25)
tmp, c = cal(tmp, c, 10)
tmp, c = cal(tmp, c, 5)
tmp, c = cal(tmp, c, 1)

print(tmp)
