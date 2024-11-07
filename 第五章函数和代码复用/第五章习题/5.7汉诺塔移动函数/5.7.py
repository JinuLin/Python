def hanoi(n, A, B, C):
    if n == 1:
        print(f"{A} -> {C}")
    else:
        hanoi(n - 1, A, C, B)  # 将前 n - 1 个盘子从 a 借助 b 移动到 c
        print(f"{A} -> {C}")  # 将第 n 个盘子从 a 直接到 c
        hanoi(n - 1, B, A, C)  # 将前 n - 1 个盘子从 b 借助 a 移动到 c


while True:
    try:
        s = int(input("请输入汉诺塔的层数："))
        if s < 1:
            print("请输入有效的正整数层数。")
        else:
            hanoi(s, "A", "B", "C")
    except ValueError:
        print("输入格式错误，请输入正整数。")
    if input("是否继续？(y/n)") == "n":
        break
