# 標準入力から値を受け取る
# S: str 型
S = input()
S1,S2 = S.split(" ")
ans = S2[0].lower() + "_" + S1.lower()

# 受け取った値を利用してコードを書いてください
print(ans)