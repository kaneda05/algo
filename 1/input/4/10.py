n = int(input())
left = 0
right = 0
for i in range(n):
    s = input()
    if s == "left": left += 1
    else: right += 1

if left<right: print("right")
elif right<left: print("left")
else: print("same")