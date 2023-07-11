# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
def trans(L):
    T = ""
    for i in L:
        if i == "a": T+="b"
        elif i == "b": T+="c"
        else: T+="a"
    return T

T = trans(S)
U = trans(T)
V = trans(U)
print(T)
print(U)
print(V)