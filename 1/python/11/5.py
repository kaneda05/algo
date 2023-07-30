
for i in range(1,9):
    ans = ""
    for j in range(1,9):
        if (i+j)%2==0:
            ans += "."
        else:
            ans += "#"
    print(ans)
