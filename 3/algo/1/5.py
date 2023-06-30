n = int(input())
res = 1
while n!=1:
    if n % 3 == 0:
        n //= 3
        res += 1
    else:
        n -= 1
        res += 1

print(res)