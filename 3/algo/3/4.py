# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10**6)

from functools import lru_cache

@lru_cache(maxsize=1000)
def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

n = int(input())
print(fib(n))

