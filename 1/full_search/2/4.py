a,b = map(int,input().split())
n = max(a,b)
for i in range(1, n+1):
    if a%i==0 and b%i==0:
        ans = i
        
print(ans)