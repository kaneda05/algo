s = input()
alphabet = [chr(i) for i in range(ord("a"),ord("z")+1)]
m = len(alphabet)
ans = 0
for i in range(m):
    if alphabet[i] in s:
        ans += 1
print(ans)