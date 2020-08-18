from sys import exit,argv
import csv


if (len(argv) != 3):
    print("Usage: python dna.py data.csv sequence.txt")
    exit()

file_sequence = open(argv[2], "r")

sequence = file_sequence.read()

print(f"sequence={sequence}")

file_database = open(argv[1], "r")

database = csv.DictReader(file_database)

for row in database:
    print(row)
