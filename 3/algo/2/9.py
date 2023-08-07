n, k = map(int,input().split())
cnt = 0
for i in range(n):
    cnt += min(n, k//(i+1))
print(cnt)