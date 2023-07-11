# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
def trans(c):
    if c == "a":
        return "z"
    else:
        return chr(ord(c)-1)

T = ""
for c in S:
    T += trans(trans(trans(c)))
print(T)

