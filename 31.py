n2=int(input())
l=[int(i) for i in input().split()]
a=[]
for i in range(0,n2):
    c=1
    for j in range(i,n2):
        c=c*l[j]
    a.append(c)
for i in range(0,n2):
    c=1
    for j in range(i+1):
        c=c*l[j]
    a.append(c)
print(max(a))
