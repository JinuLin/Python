import time
scale = 3  # 进度条精度
print("--------执行开始---------")
for i in range(scale + 1):
    a, b = '.' * i, ' ' * (scale - i)
    print("\rStarting {}{} Done!".format(a, b), end='')
    time.sleep(0.1)
print()
print("--------执行结束----------")
