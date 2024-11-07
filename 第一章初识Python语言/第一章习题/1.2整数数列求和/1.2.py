# 1.2整数序列求和
n = input("请输入整数N: ")
sum = 0
for i in range(int(n)):  # range用于计数整数。for表示循环
    sum += i + 1
print("1 到N 求和结果: ", sum)
