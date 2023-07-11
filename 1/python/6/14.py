poll_info = [90, 60, 240, 30, 180]

# ここに poll_info を加工するコードを書いてください
total = 0
for i in poll_info:
    total += i
    
for i in range(len(poll_info)):
    poll_info[i] = poll_info[i] * 100 // total

# poll_info を出力
print(poll_info)
