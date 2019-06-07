s1=input()
l=[0]
if "ab" not in s1:
    print("0")
else:
    for i in range(len(s1)):
        c=1
        for j in range(i,len(s1)-1):
            if s1[j]=="a" and s1[j+1]=="b":
                c=c+1
            elif s1[j]=="b" and s1[j+1]=="a":
                c=c+1
            else:
                l.append(c)
                c=1
                break
        if s[i]=="a":
            l.append(c)
        else:
            l.append(c-1)
    print(max(l))
