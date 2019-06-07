n1=int(input())
l=list(map(int,input().split()))
a=l
c=[]
while(len(a)!=1):
	for i in range(len(a)):
		if i%2!=0:
			c.append(a[i])
	a=c
	c=[]
print(l.index(a[0]))
