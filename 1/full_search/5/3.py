x, y, z = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

ans = 0
for i in range(x):
    for j in range(y):
        for k in range(z):
            if a[i]+b[j] == c[k]:
                ans += 1
print(ans)