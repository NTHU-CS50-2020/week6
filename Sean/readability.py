from cs50 import get_string

t = get_string("Text: ")
l_count = w_count = s_count = 0
flag = 1
n = len(t)
for i in range(n):
    if t[i].isalpha():
        l_count += 1
    if t[i] == '.' or t[i] == '!' or t[i] == '?':
        s_count += 1
    if flag and not t[i].isspace():
        w_count += 1
        flag = 0
    elif t[i].isspace():
        flag=1
# print(f'l_count: {l_count}, s_count: {s_count}, w_count: {w_count}')
L = l_count / w_count * 100
S = s_count / w_count * 100
index = 0.0588 * L - 0.296 * S - 15.8
g = round(index)
if g > 16:
    print("Grade 16+")
elif g < 1:
    print("Before Grade 1")
else:
    print(f"Grade {g}")
