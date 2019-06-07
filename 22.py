r1=int(input())
l=list(map(int,input().split()))

f=1
i=1
while(i<len(l)+1):
  f=1
  j=1
  for x in l:
  
       if(i!=j):
            
            f=f*x
            j=j+1
       else:
            j=j+1
            continue
  
  print(f,end=" ")
  i=i+1
