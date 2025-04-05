# 微实例4.4.1遍历循环：for语句
for s in "BIT":
    print("循环进行中：" + s)
else:
    s = "循环正常结束"
print(s)
# 遍历结构可以是字符串、文件、组合数据类型或range()函数等
"""
循环N次
for i in range(N):
<语句块>
"""
"""
遍历文件fi的每一行
for line in fi:
<语句块>
"""
"""
遍历字符串s
for c in s:
<语句块>
"""
"""
遍历列表ls
for item in ls:
<语句块>
"""
# else扩展
"""
for <遍历变量> in <遍历结构>:
    <语句块1>
else:
    <语句块2>
"""
# for循环执行结束后，执行else的内容。可以用else在语句块2放置来判断执行循环的情况
