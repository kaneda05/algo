n, s = map(int,input().split())
q = int(input())
for i in range(q):
    num, x = map(int,input().split())

    if num == 0:
        # on
        s |= (1 << x)

    elif num == 1:
        # off
        s &= ~(1 << x)

    else:
        # check
        if s & (1 << x):
            print("Yes")
        else:
            print("No")
    
