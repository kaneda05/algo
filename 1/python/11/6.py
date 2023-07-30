# ここにコードを書いてください
ans = 0
for i in range(1,10000):
    ans += i
    if 10000<ans:
        print(i)
        break
