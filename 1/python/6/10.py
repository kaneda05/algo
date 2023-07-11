# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
T = ""
for i in S:
    if i == "a": T+="b"
    elif i == "b": T+="c"
    else: T+="a"
print(T)