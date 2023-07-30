# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
dict_a = {
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
}

for key, value in dict_a.items():
    S = S.replace(key, value)
print(S)