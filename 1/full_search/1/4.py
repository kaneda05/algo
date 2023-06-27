n, v = map(int,input().split())
a = list(map(int,input().split()))
if a.count(v) == 0:
    print(-1)
    exit()
else:
    for i in range(n):
        if a[i] == v:
            ans = i
print(ans)