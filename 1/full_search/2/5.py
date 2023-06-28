n = int(input())

def func(n):
    if n%3==0 and n%5==0: return "FizzBuzz"
    elif n%3==0: return "Fizz"
    elif n%5==0: return "Buzz"
    else: return n

for i in range(1,n+1):
    print(func(i))