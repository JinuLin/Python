# a = eval(input("请输入一个五位数："))
# b = a // 10000 + a // 1000 % 10 * 10 + a // 100 % 10 * 100 + a // 10 % 10 * 1000 + a % 10 * 10000
# if a == b:
#     print("这个数是回文数")
# else:
#     print("这个数不是回文数")
a = 0
c = 0
for a in range(10000, 100000):
    b = a // 10000 + a // 1000 % 10 * 10 + a // 100 % 10 * 100 + a // 10 % 10 * 1000 + a % 10 * 10000
    if b == a:
        print("{}".format(b), end="、")
        c += 1  # 用c循环计数
        if c % 10 == 0:  # 计数到10，每十个换行一次
            print("\n")
