import sys
sys.setrecursionlimit(10**6)

def func(x):
    if x == 0:
        return 0

    return x + func(x-1)

a, b = map(int,input().split())
print(func(b)-func(a-1))
