    
r1,s=map(int,input().split())
l=list(map(int,input().split()))
c=0
for x in l:
    if(x>s):
        l.remove(x)
for i in range(0,len(l)):
    j=0
    for x in l:
        if(x+l[i]==s and i!=j):
            
            c=c+1
            break
        j=j+1   
            
if (c>0):
    print("YES")
else:
    print("NO")
