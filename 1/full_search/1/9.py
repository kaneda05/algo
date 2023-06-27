n = int(input())
a = list(map(int,input().split()))
cnt = [0]*9
for i in range(n):
    cnt[a[i]-1] += 1

for i in cnt:
    print(i)