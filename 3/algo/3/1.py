# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10**6)

# 再帰関数
def func(x):
    if x == 0:
        return 0
    
    return x + func(x-1)

n = int(input())
print(func(n))