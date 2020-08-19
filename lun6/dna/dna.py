from sys import argv,exit
'''for a in argv:
    print(a)'''
'''for i in range(len(argv)):
    print(argv[i])'''
if len(argv)!=3:
    print("oxo")
    
text = open(argv[2]) #print(t.read())

import csv
with open(argv[1], newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames=reader.fieldnames[1: ]#第一行標題的一個後面['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
    x=[]
    xx=[]
    for row in reader:
        #print(row)
#csv.DictReader//OrderedDict([('name', 'Sirius'), ('AGATC', '31'), ('TTTTTTCT', '11'), ('AATG', '28'), ('TCTAG', '26'), ('GATA', '35'), ('TATC', '19'), ('GAAA', '33'), ('TCTG', '6')])
#csv.reader//['name', 'AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
        for atcg in fieldnames:
            xx.append(row[atcg])
            
        x.append(row['name'])
    
    
#python dna.py databases/large.csv sequences/1.txt    
'''
    xx= []
    rr=reader.fieldnames[1: ]#不用寫在for裡面就能叫出來
    for row in reader:
        #在reader的print(row[1: ])#['29', '50', '18', '23', '38', '24', '22', '9']print(row[0])
        for STR in rr:
            x.append(row[STR])
        xx.append(x)    
        #print(' '.join(row)) #一長串的，前面是'分隔的東東'


import pandas as pd#Pandas 是 python 的一個數據分析 lib
dna = text.read()
df = pd.read_csv(argv[1])
print(df)
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
'''

