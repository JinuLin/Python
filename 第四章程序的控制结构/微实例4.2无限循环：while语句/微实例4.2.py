# 微实例4.4.2无限循环：while语句
s, idx = "BIT", 0
while idx < len(s):
    print("循环进行中：" + s[idx])
    idx += 1
else:
    s = "循环正常结束"
print(s)
"""
while <条件>:
    <语句块>
条件为True和False，当条件判断为True时，则执行语句块，如果条件判断为False时，则跳出循环。
如果条件为True时，则无限循环执行语句块：
while True:
    <语句块>
"""
# 扩展while-else：
"""
while <条件>:
    <语句块1>
else:
    <语句块2>
当while正常执行后，才会执行else。
"""
