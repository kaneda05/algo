# ここに答えとなるコードを書いてください
import datetime

# 2023 年 1 月 1 日を表す変数
d = datetime.date(2023, 1, 1)

# 100 日進める
d += datetime.timedelta(days=100)

# YYYY-MM-DD 形式で出力する
print(d)