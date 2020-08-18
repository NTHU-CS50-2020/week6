import string

s = input("Text: ")
n = len(s)

letter = 0
word = 0
sentence = 0

for i in range(n):
    if(('a' <= s[i] and s[i] <= 'z') or ('A' <= s[i] and s[i] <= 'Z')):
        letter += 1
    elif(s[i] == ' '):
        word += 1
    elif(s[i] == '.' or s[i] == '!'):
        sentence += 1

word_real = int(word + 1)
print(f"letter={letter}, word_real={word_real}, sentence={sentence} ")

multiple = 0
letter_per = 0
sentence_per = 0
degree = 0

multiple = float(100 / word_real)
letter_per = float(letter * multiple)
sentence_per = float(sentence * multiple)
degree = float((0.0588 * letter_per) - (0.296 * sentence_per) - 15.8)

print(f"letter_per={letter_per}, sentence_per={sentence_per}, degree={degree} ")

degree_precise = 0
if(((int(degree) * 10) % 10) >= 5):
    degree_precise = int(degree) + 1
else:
    degree_precise = int(degree)

if (degree_precise <= 1):
    print("degree: 1")
elif(degree_precise > 16):
    print("degree: 16+")
else:
    print(f"degree: {degree_precise}")