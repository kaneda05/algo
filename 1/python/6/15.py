person_info = [
    {"name": "aruru", "height": 1.7, "weight": 70.0},
    {"name": "iruru", "height": 1.6, "weight": 65.0},
    {"name": "ururu", "height": 1.8, "weight": 70.0},
    {"name": "eruru", "height": 1.5, "weight": 40.0}
]

# ここに person_info を加工するコードを書いてください
for d in person_info:
    BMI = d["weight"] / d["height"]**2
    d["BMI"] = round(BMI,1)
# person_info を出力
print(person_info)
