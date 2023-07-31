def f(n, x):
    ans = n + 1
    for i in range(5):
        ans = ans * x + 1
    return ans

n,m = map(int,input().split())

left = 0
right = 100
while (right-left>1e-4):
    mid = (right+left)/2
    if f(n,mid)<m:
        left = mid
    else:
        right = mid
        
ans = left
print(ans)