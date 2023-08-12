a = list(map(int,input().split()))
dp = [[0 for _ in range(4)] for i in range(4)]
dp[0] = a

for i in range(1,4):
    for j in range(4):
        if i-1>=0 and j-1>=0:
            dp[i][j] += dp[i-1][j-1]
        if i-1>=0:
            dp[i][j] += dp[i-1][j]
        if i-1>=0 and j+1<4:
            dp[i][j] += dp[i-1][j+1]

print(dp[-1][-1])