# 微实例3.7.2单行动态刷新

import time

for i in range(101):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.05)
