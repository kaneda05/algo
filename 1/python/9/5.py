# 各有権者が投票した立候補者の名前
votes = ["aruru", "iruru", "ururu", "aruru", "eruru", "oruru", "aruru", "iruru", "aruru", "eruru", "iruru", "ururu", "eruru"]
from collections import defaultdict
d = defaultdict(int) # 空の辞書型変数
for vote in votes: # 投票された立候補者に 1 を足す
    d[vote] += 1

# 投票結果を出力
for name, value in d.items():
    print(f"{name} {value}")
