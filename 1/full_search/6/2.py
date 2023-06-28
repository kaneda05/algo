import math
l,r = map(int,input().split())
li = [0]*10
for i in range(l,r+1):
    li[i%10] += 1

print(li)
ans = 0
for i in li:
    if 2<=i:
        ans += math.comb(i,2)
print(ans)