n = int(input())
S = set()
for i in range(n):
    s = input()
    S.add(s)

if len(S)<n: print("Yes")
else: print("No")