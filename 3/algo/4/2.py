n = int(input())
a = list(map(int,input().split()))

for i in range(n-1):
    tmp = a[i]
    index = i
    for j in range(i+1, n):
        if tmp > a[j]:
            tmp = a[j]
            index = j
    a[i], a[index] = a[index], a[i]
    print(*a)