# 微实例3.7.1基本的多行文本进度条
import time

scale = 10  # 变量scale表示输出进度条的精度
print("------执行开始------")
for i in range(scale + 1):
    a, b = '**' * i, '..' * (scale - i)
    c = (i / scale) * 100
    print("%{:^3.0f}[{}->{}]".format(c, a, b))
    time.sleep(0.1)  # 调用time中的sleep(t)，将当前程序挂起t s，t可以是小数。
print("------执行结束------")
