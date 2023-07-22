import math

class MyFraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.normalize()
    def normalize(self): # 約分して分母を正にするメソッド
        if self.den < 0:
            self.num *= -1
            self.den *= -1
        g = math.gcd(self.num, self.den)
        self.num //= g
        self.den //= g
    def __str__(self): # print 関数の出力内容を定義するメソッド
        return f"{self.num}/{self.den}"
    def __add__(self, other): # 足し算を定義するメソッド
        num_result = self.num * other.den + self.den * other.num
        den_result = self.den * other.den
        return MyFraction(num_result, den_result)
    def __sub__(self, other): # 引き算を定義するメソッド
        num_result = self.num * other.den - self.den * other.num
        den_result = self.den * other.den
        return MyFraction(num_result, den_result)
    def __mul__(self, other): # 掛け算を定義するメソッド
        num_result = self.num * other.num
        den_result = self.den * other.den
        return MyFraction(num_result, den_result)
    def __truediv__(self, other): # 割り算を定義するメソッド
        num_result = self.num * other.den
        den_result = self.den * other.num
        return MyFraction(num_result, den_result)

a = MyFraction(2, 3)
b = MyFraction(1, 6)
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} × {b} = {a * b}")
print(f"{a} ÷ {b} = {a / b}")