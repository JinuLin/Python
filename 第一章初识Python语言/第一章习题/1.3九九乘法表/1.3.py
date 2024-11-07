# 1.3九九乘法表输出
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={:2} ".format(j, i, i * j), end='')  # end指最终终止值
    print('')
