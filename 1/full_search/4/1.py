def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

n = int(input())
A = list(map(int,input().split()))

ans = 0
for a in A:
    if is_prime(a):
        ans += 1
print(ans)