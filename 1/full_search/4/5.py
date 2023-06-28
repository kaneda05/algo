n = int(input())
ans = 0
for i in range(n):
    s = input()
    flag = True
    m = len(s)
    for j in range(m):
        if s[j] != s[(m-1)-j]:
            flag = False
    if flag:
        ans += 1

print(ans)