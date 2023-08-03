def f(x, L):
    ans = 0
    for l in L:
        ans += int(l/x)
    return ans

n, k = map(int,input().split())
L = list(map(int,input().split()))

left = 0
right = 10**5+1
while (right-left>1e-6):
    mid = (left+right)/2
    if f(mid, L) >= k:
        left = mid
    else:
        right = mid

ans = left
print(ans)