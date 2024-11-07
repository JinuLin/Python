def drawsq(n):
    # 计算每一行的长度
    line = 3 * n + 1
    # 循环打印每一行
    for i in range(1, line + 1):
        # 如果是奇数行
        if i % 3 == 1:
            # 打印加号和横线
            print(n * "+----", end="")
            print("+")
        else:
            # 打印空格和竖线
            print("|    " * n, end="")
            print("|")


def main():
    # 获取用户输入的阶数
    n = eval(input("请输入您要的阶数："))
    # 调用drawsq函数打印图案
    drawsq(n)


# 运行主函数
main()
