n, m = map(int,input().split())
d = list(map(int,input().split()))

dp = [False]*(n+1)
dp[0] = True

for i in range(1,n+1):
    for j in range(m):
        if (i - d[j] >= 0 and dp[i-d[j]]):
            dp[i] = True

if dp[n]:
    print("Yes")
else:
    print("No")
