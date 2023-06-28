s = input()
t = input()

n = len(s)
m = len(t)
for i in range(n-m+1):
    if s[i:i+m] == t:
        print("Yes")
        exit()
        
print("No")