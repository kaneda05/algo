# 標準入力から値を受け取る
# S: str 型
S = input()

# 答えを格納するための空文字列を用意
ans = ""

# S の各文字について調べる
for c in S:
    if c.islower() and not c in ["a", "i", "u", "e", "o"]:
        ans += "_" # 小文字の子音は置換する
    else:
        ans += c

# 答えを出力
print(ans)