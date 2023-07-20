# 標準入力から値を受け取る
# month: int 型
month = int(input())
l = [4,6,9,11]
# 受け取った値を利用してコードを書いてください
if month == 2: print(28)
elif month in l: print(30)
else: print(31)
