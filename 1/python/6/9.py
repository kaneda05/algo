# 標準入力から値を受け取る
# S: str 型
S = input()
S = S.replace("o","z")
S = S.replace("x","o")
S = S.replace("z","x")
# 受け取った値を利用してコードを書いてください
print(S)