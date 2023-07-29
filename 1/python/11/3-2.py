s = input()

ans = ""
char_set = set()
for c in s:
    if c in char_set:
        ans += "*"
    else:
        ans += c
        char_set.add(c)
print(ans)