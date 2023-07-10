def func(x):
    return x*(x*(x+1)+2)+3

n = int(input())
left = 0
right = 100
while (right-left>1e-4):
    mid = (left+right)/2
    if func(mid)<n:
        left = mid
    else:
        right = mid
        
ans = left
print(ans)