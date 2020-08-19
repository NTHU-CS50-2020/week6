from sys import exit,argv
import csv


if (len(argv) != 3):
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

file_sequence = open(argv[2], "r")

sequence = file_sequence.read()

#print(f"sequence={sequence}")

file_database = open(argv[1], "r")

strands = []
compare = {}

for ind, row in enumerate(file_database):
    if ind == 0:
        strands = row.strip().split(',')
        strands = strands[1:]
        #print(strands)
    else:
        name = row.strip().split(',')[0]
        data = row.strip().split(',')
        compare[name] = [int(x) for x in data[1:]]
        
#print(compare)
#print(len(strands))

final_strands = []

for strands in strands:
#    print(strands)
    i = 0
    max_repeat = -1
    repeat = 0
    while i < len(sequence):
#        print(sequence[i:i + len(strands)])
        if (strands != sequence[i:i + len(strands)]):
            i += 1
            repeat = 0
        elif(strands == sequence[i:i + len(strands)]):
            i += len(strands)
            repeat += 1
            max_repeat = max(max_repeat, repeat)

    final_strands.append(max_repeat)

#print(final_strands)

for name in compare:
#    print(compare[name])
    if(compare[name] == final_strands):
        print(name)
        exit()
print("no match")