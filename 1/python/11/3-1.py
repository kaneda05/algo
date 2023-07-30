# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください

alphabet = {chr(c):0 for c in range(ord("a"), ord("z")+1)}

ans = ""
for s in S:
    if alphabet[s] == 1:
        ans += "*"
    else:
        alphabet[s] += 1
        ans += s
#print(alphabet)
print(ans)
    