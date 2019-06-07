r1=input()
r1=list(r1)
if r1==r1[::-1]:
	while r1==r1[::-1]:
		r1[-1]=""
h=""
for i in r1:
	h=h+i
print(h)
