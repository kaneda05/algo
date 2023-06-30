x = int(input())
a = list(map(int,input().split()))

coins = [50, 10, 5, 1]

res = 0
for i in range(4):
    add = x//coins[i]
    add = min(add, a[i])
    res += add

    x -= coins[i] * add

print(res)