from random import randint
i = randint(0, 9)
tim = 0
while True:
    n = eval(input("0~9请输入您猜测的一个数："))
    tim += 1
    if n != i:
        if n > i:
            print("遗憾，太大了")
        else:
            print("遗憾太小了")
    else:
        print("预测{}次，您猜中了！".format(tim))
        break
