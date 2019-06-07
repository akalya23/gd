a2,b = map(int,input().split())
b = b%a2
l1 = list(map(int,input().split()))
l2 = l1[-b:] + l1[:-b]
print(*l2)
