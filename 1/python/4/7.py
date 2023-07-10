# 標準入力から値を受け取る
# diff: int 型
diff = int(input())
special = (10,20,30)
# 受け取った値を利用してコードを書いてください
if diff in special: print("special")
else:
    if 1<=diff<=9: print("easy")
    elif 11<=diff<=19: print("normal")
    elif 21<=diff<=29: print("hard")
