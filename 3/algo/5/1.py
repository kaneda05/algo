n, x, y = map(int,input().split())

dp = [0] * n
dp[0], dp[1] = x, y

for i in range(2,n):
    dp[i] = (dp[i-2]+dp[i-1]) % 100

print(dp[-1])