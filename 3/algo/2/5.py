N,K = map(int, input().split())
A = list(map(int, input().split()))

# 配列 A を昇順にソートする
A.sort()

count = 0
for i in range(N):
    # 二分探索
    left = 0
    right = N
    while (left!=right): # 解が求まるまで
        # left と right の 中点 mid をとる
        mid = (left+right)//2;
        if (A[mid]>=K-A[i]): # もし A[mid] >= B[i] ならば答えは left 以上 mid 以下
            right = mid; # 範囲を狭める
        else: # そうでなければ答えは mid+1 以上 right 以下
          left = mid+1; # 範囲を狭める
    count += N - left;

print(count)