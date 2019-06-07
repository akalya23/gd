y1=input()
st=0
for i in y1:
  st+=int(i)
if str(st)==str(st)[::-1]:
  print("YES")
else:
  print("NO")
