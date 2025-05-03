# 微实例3.5.4内置字符串处理函数
# len(x) 返回字符串长度，也可返回其他组合数据类型元素个数
# str(x) 返回任意类型的字符串形式
# chr(x) 返回Unicode编码x对应
# ord(x) 返回单字符表示Unicode编码
# hex(x) 返回整数x对应十六进制数的小写形式字符串
# oct(x) 返回整数x对应八进制数的小写形式字符串
print(len("Python语言程序设计"))
print(str(3.1415926))
print("1+1=2" + chr(10004))
print("金牛座的字符♉Unicode的值是：" + str(ord("♉")))

print(hex(255))
print(oct(-255))
"""
字符串操作含义：
+：连接
*：重复
<string>[ ]：索引
<string>[ : ]：剪切
len(<string>)：长度
<string>.upper()：字符串中字母大写
<string>.lower()：字符串中字母小写
<string>.strip()：去两边空格及去指定字符
<string>.split()：按指定字符分割字符串为数组
<string>.join()：连接两个字符串序列
<string>.find()：搜索指定字符串
<string>.replace()：字符串替换
for <var> in <string>：字符串迭代
"""
