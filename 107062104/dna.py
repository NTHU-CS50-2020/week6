import sys, csv, re

if len(sys.argv) != 3:
    print('Usage: python dna.py data.csv sequence.txt')

def main():

    database = []

    with open(sys.argv[1] , newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        STRs = reader.fieldnames[1:]
        for row in reader:
            individual = []
            individual.append(row['name'])
            for STR in STRs:
                individual.append(row[STR])
            database.append(individual)

    f = open(sys.argv[2], 'r')
    DNA = f.read()

    STR_count = ['DNA']
    for STR in STRs:
        #https://www.geeksforgeeks.org/python-maximum-consecutive-substring-occurrence/
        longest_STR = max(re.findall('((?:' + re.escape(STR) + ')*)', DNA), key = len)
        STR_count.append(len(longest_STR) // len(STR))

    for individual in database:
        for i in range(1, len(individual)):
            if int(individual[i]) == STR_count[i]:
                if i == len(individual) - 1:
                    print(individual[0])
                    return
            else:
                break
    print('No match')

main()