from cs50 import get_string

def main():
    text = get_string('Text: ')
    print(GradeCal(text))


def GradeCal(text):
    letters = 0
    words = 1 if text else 0
    sentences = 0

    for letter in text:
        letters += 1 if letter.isalpha() else 0
        words += 1 if letter.isspace() else 0
        sentences += 1 if letter == '.' or letter == '!' or letter == '?' else 0

    index = round(0.0588 * (letters/words*100) - 0.296 * (sentences/words*100) - 15.8, 0)

    if index < 1:
        return 'Before Grade 1'
    elif index > 16:
        return 'Grade 16+'
    else:
        return 'Grade ' + str(int(index))


main()
