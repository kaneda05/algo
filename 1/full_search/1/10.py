n = int(input())
a = list(map(int,input().split()))
cnt = [0]*9
for i in a:
    cnt[i-1] += 1

count = -10*9
for i in range(9):
    if count<cnt[i]:
        count = cnt[i]
        ans = i+1
print(ans)
