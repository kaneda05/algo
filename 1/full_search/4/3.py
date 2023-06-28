l, r = map(int,input().split())
ans = 0

for i in range(l, r+1):
    s = str(i)
    n = len(s)
    flag = True
    for j in range(n):
        if s[j] != s[(n-1)-j]:
            flag = False
    if flag:
        ans += 1
print(ans)