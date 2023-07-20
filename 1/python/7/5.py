# 円周率を表す変数
PI = 3.14

# ここに答えとなるコードを書いてください
def cal1(r):
    s = r**2 * PI
    return s

def cal2(r,h):
    s = r**2 * PI * h
    return s

print(f"半径 3 cm の円の面積は {cal1(3)} cm^2")
print(f"半径 5 cm の円の面積は {cal1(5)} cm^2")
print(f"半径 10 cm の円の面積は {cal1(10)} cm^2")
print(f"底面の半径が 2 cm、高さが 4 cm の円柱の体積は {cal2(2,4)} cm^3")
print(f"底面の半径が 6 cm、高さが 10 cm の円柱の体積は {cal2(6,10)} cm^3")
print(f"底面の半径が 10 cm、高さが 3 cm の円柱の体積は {cal2(10,3)} cm^3")