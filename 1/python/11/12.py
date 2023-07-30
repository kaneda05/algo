# ここに答えとなるコードを書いてください
from itertools import permutations
ans = permutations('ABCD', 4)
for i in ans:
    print("".join(i))