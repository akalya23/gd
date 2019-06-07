from itertools import permutations
ls1=list(input())
p1 = permutations(ls1)
b=[]
for i in list(p1):
    s=''
    for j in i:
       s+=j
    if s not in b:
       b.append(s)
       print(s)
