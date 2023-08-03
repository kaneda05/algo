import bisect

n = int(input())
W = list(map(int,input().split()))

W1 = W
W1 = sorted(W)

for w in W:
    print(bisect.bisect_left(W1, w))
