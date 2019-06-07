
s1=0
q=0
r=int(input())
while(r!=0):
    t=r%10
    s1=s1+t
    r=r//10
a=s1

if(s1<9):
    print("YES")
else:
    while(s1!=0):
        f=s1%10
        q=f+(q*10)
        
        s1=s1//10
    if(a==q):
        print("YES")
    else:
        print("NO")
