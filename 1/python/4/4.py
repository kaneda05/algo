# 標準入力から値を受け取る
# dist: int 型
dist = int(input())

# 受け取った値を利用してコードを書いてください
ans = 300 * dist + 650
if 100<=dist: ans -= 5000
print(ans)