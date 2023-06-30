n = int(input())
ans = 0
while True:
    if n == 0:
        break
    else:
        if n % 2 == 0:
            n //= 2
            ans += 1
        else:
            n-= 1
            ans += 1
print(ans)
