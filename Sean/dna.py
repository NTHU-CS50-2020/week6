import pandas as pd
from sys import argv, exit

if len(argv) != 3:
    exit("Usage: python dna.py data.csv sequence.txt")

f = open(argv[2])
dna = f.read()
df = pd.read_csv(argv[1])
strs = list(df.columns.values)[1:]
flag = 0
count = 0
d = {}
for s in strs:
    str_l = len(s)
    count_list = []
    if s in dna:
        for i in range(dna.find(s), dna.rfind(s)+str_l):
            if dna[i:i+str_l] != s:
                count_list.append(0)
            elif dna[i:i+str_l] == s and dna[i-str_l:i] == s:
                count += 1
                count_list.append(count)
            elif dna[i:i + str_l] == s and dna[i - str_l:i] != s:
                count = 1
                count_list.append(count)
        d[s] = count_list
    else:
        d[s] = [0]
        continue
for s in strs:
    df = df[df[s] == max(d[s])].reset_index(drop=True)
if df.empty:
    print('No match')
else:
    print(df['name'][0])
