n, s = map(int,input().split())
q = int(input())
for i in range(q):
    num, x = map(int, input().split())
    if num == 0:
        # Switch(x)
        s ^= (1 << i)
    else:
        # Check(x)
        if s & (1 << x):
            print("on")
        else:
            print("off")