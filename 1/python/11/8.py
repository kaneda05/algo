# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
name_set = set()
n = len(S)
for i in range(n-2):
    name_set.add(S[i]+S[i+1]+S[i+2])


ans = len(name_set)
#print(name_set)
print(ans)