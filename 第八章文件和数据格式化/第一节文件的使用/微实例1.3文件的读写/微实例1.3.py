# 微实例6.1.3文件的读写
"""
根据打开方式不同可以对文件进行相应的读写操作，Python提供4个常用的文件内容读取方法
<file>.readall() 读入整个文件内容，返回一个字符串或字节流*
<file>.read(size=-1) 从文件中读入整个文件内容，如果给出参数，读入前size长度的字符串或
字节流
<file>.readline(size = -1) 从文件中读入一行内容，如果给出参数，读入该行前size长度的字符串或
字节流
<file>.readlines(hint=-1) 从文件中读入所有行，以每行为元素形成一个列表，如果给出参数，读
入hint行
"""
name = input("请输入要打开的文件: ")
fo = open(name, "r")
for line in fo.readlines():
    print(line)
fo.close()

"""
遍历文件的所有行可以直接这样完成
如果程序需要逐行处理文件内容，建议采用这种代码格式：
fo = open(name, "r")
for line in fo:
    # 处理一行数据
fo.close()
"""
f_name = input("请输入要打开的文件: ")
fo = open(f_name, "r")
for line in fo:
    print(line)
fo.close()
"""
Python提供3个与文件内容写入有关的方法
<file>.write(s) 向文件写入一个字符串或字节流
<file>.writelines(lines) 将一个元素为字符串的列表写入文件
<file>.seek(offset) 改变当前文件操作指针的位置，offset的值：0：文件开头； 1: 当前位置； 2: 文件结尾
"""
name = input("请输入要写入的文件: ")  # 输入文件名1.3test.txt
fo = open(name, "w+")
ls = ["唐诗", "宋词", "元曲"]
fo.writelines(ls)
for line in fo:
    print(line)
fo.close()
