n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if max(a[i],a[j],a[k])==a[j]:
                ans += 1

print(ans)