n, k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    cnt = 0
    for j in range(1,i+1):
        if i%j==0:
            cnt += 1
    if cnt == k:
        ans += 1
        
print(ans)