# 標準入力から値を受け取る
# S: str 型
S = input()
# T: str 型
T = input()

# 受け取った値を利用してコードを書いてください
cnt = 0
for i in range(len(S)):
    if S[i] == T[i]:
        cnt += 1

if 4<=cnt:
    print("Bad")
else:
    print("Good")