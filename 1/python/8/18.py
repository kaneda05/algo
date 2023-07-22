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
    def __lt__(self, other): # 小なり
        return self.num * other.den - self.den * other.num < 0
    def __le__(self, other): # 以下
        return self.num * other.den - self.den * other.num <= 0
    def __eq__(self, other): # 等しい
        return self.num * other.den - self.den * other.num == 0
    def __ne__(self, other): # 異なる
        return self.num * other.den - self.den * other.num != 0
    def __gt__(self, other): # 大なり
        return self.num * other.den - self.den * other.num > 0
    def __ge__(self, other): # 以上
        return self.num * other.den - self.den * other.num >= 0

a = MyFraction(-3, 5)
b = MyFraction(2, 3)
c = MyFraction(3, 5)
d = MyFraction(6, 10)

print(f"c == d -> {c == d}")
print(f"c != d -> {c != d}")
print(f"a < b -> {a < b}")
print(f"b <= c -> {b <= c}")
print(f"a > d -> {a > d}")
print(f"c >= d -> {c >= d}")