n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()
cnt = 0
index = 0
for i in range(n):
    flag = False
    for j in range(index,m):
        if a[i]<=b[j] and flag==False:
            cnt += 1
            index = j+1
            flag = True

print(cnt)
        