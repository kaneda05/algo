n = int(input())
a = list(map(int,input().split()))

for k in range(1, n):
    while k!=0 and a[k-1]>a[k]:
        a[k-1], a[k] = a[k], a[k-1]
        k -= 1

    print(*a)