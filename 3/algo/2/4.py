import bisect
n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
for b in B:
    print(bisect.bisect_right(A,b))