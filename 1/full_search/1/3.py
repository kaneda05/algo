n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in a:
    if 0<i: ans += 1
print(ans)