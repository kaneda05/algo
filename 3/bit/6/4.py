N = int(input())
F = list(map(int, input().split()))

# ビットシフトにより答えを求める
result = sum(1 << f for f in F)

print(result)