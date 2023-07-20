# カメは全員アルファベット 5 文字の名前です
names = [ "alulu", "umumu", "namae", "totot", "irisu", "aaaaa", "mamma", "dadaa", "wowow", "kanan", "usasa", "kamem", "erina", "choco", "betty", "xoooo" ]

# アルルに似た名前か判定する
def is_like_aruru(name):
    if name[1] != name[3]:
        return False
    if name[2] != name[4]:
        return False
    return True

# アララに似た名前か判定する
def is_like_arara(name):
    if name[1] != name[3]:
        return False
    if name[2] != name[4]:
        return False
    if name[0] != name[2]:
        return False
    return True

# アルルに似た名前を数える変数
answer_aruru = 0

# アララに似た名前を数える変数
answer_arara = 0

# 条件を満たす名前を数える
for name in names:
    if is_like_aruru(name):
        answer_aruru += 1
    if is_like_arara(name):
        answer_arara += 1

# 答えを出力する         
print(answer_aruru)
print(answer_arara)