# 微实例3.7.3带刷新的文本进度条
import time

scale = 50
print("执行开始".center(scale // 2, '-'))
t = time.perf_counter()
# 原来采用time.clock，但是Python3.8以上把这个函数去掉了，但是库里还包含着。
# 可以调用time.perf_counter() 或process_time()替换
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    t -= time.perf_counter()
    s = t / 100000  # 如果调用的是time.clock就不用做除法转化
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, -s), end='')
    time.sleep(0.05)
print("\n" + "执行结束".center(scale // 2, '-'))
