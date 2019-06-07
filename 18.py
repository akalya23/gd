n=int(input())
M1=[]
c=0
for i in range(n):
  M1.append(list(map(int,input().split())))
f=0
for i in range(len(M1)):
  for j in range(len(M1[0])):
    f=0
    if M1[i][j]==1:
      try:
        if M1[abs(i-1)][j]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M1[i+1][j]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M1[i][abs(j-1)]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M1[i][j+1]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M1[abs(i-1)][abs(j-1)]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M1[abs(i-1)][j+1]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M1[i+1][abs(j-1)]==0:
          f+=1
      except IndexError:
        f+=1
      try:
        if M1[i+1][j+1]==0:
          f+=1
      except IndexError:
        f+=1
    if f==8:
      c+=1

print(c)
