n = int(input())
a = list(map(int,input().split()))

for _ in range(n):
    flag = False
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            flag = True
    
    if flag: print(*a)
    else: break
        