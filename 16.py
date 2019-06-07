n1,k=map(int,input().split())
l=list(map(int,input().split()))
dics={}

for i in range(len(l)):
    f=[abs(l[i]-k) for i in range(len(l))]
for i in range(len(l)):
    dics[l[i]]=f[i]
del dics[k]
q=sorted(dics.items(),key = lambda x : x[1])
i=0
for a,b in q:
     i=i+1
     print (a,end=" ")
     if (i==3):
         break
