# コラッツ予想
# ここにコードを書いてください
def func(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3*num+1

x = 27
cnt = 0
while x!=1:
    x = func(x)
    cnt += 1
print(cnt)