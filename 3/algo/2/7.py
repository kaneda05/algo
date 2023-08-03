def f(x):
    return x*(x+1)/2

n = int(input())
X = list(map(int,input().split()))

for i in range(n):
    left = 0
    right = 2**60
    while(left!=right):
        mid = (left+right)//2
        if (f(mid)>=X[i]):
            right = mid
        else:
            left = mid + 1
    ans = left
    print(ans)
