a = " ＋ "
b = "   "
c = " — "
d = " ｜ "

for h in range(1, 12):  # 田字格有11行
    for i in range(1, 12):  # 田字格有11列
        if h in [1, 6, 11] and i in [1, 6, 11]:
            print(a, end="")
        if h in [1, 6, 11] and i not in [1, 6, 11]:
            print(c, end="")
        if h not in [1, 6, 11] and i in [1, 6, 11]:
            print(d, end="")
        if h not in [1, 6, 11] and i not in [1, 6, 11]:
            print(b, end="")
        if i == 11:
            print()
"""
for i in range(11):
    if i in [0,5,10]:
        print("+ - - - - + - - - - +")
    else:
        print("|         |          |")
"""
