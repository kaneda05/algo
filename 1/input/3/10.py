s = list(input())
n, m = map(int,input().split())
s[n-1],s[m-1] = s[m-1],s[n-1]
print("".join(s))