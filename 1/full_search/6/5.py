n = int(input())
s = input()
ans = 0
for x in range(n):
    for y in range(x+1,n):
        if s[x]==s[y]:
            ans += 1
print(ans)