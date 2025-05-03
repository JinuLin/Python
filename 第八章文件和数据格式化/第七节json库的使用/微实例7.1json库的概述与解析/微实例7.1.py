# 微实例7.1json库的概述与解析
import json

"""
json库主要包括两类函数：操作类函数和解析类函数。
操作类函数主要完成外部JSON格式和程序内部数据类型之间的转换功能，
解析类函数主要用于解析键值对内容。
dumps()和loads()分别对应编码和解码功能。
"""
"""
4个操作函数：
json.dumps(obj, sort_keys=False, indent=None)：将Python的数据类型转换为JSON格式，编码过程
json.loads(string)：将JSON格式字符串转换为Python的数据类型，解码过程
json.dump(obj, fp, sort_keys=False, indent=None)：与dumps()功能一致，输出到文件fp
json.load(fp)：与loads()功能一致，从文件fp读入
"""
"""
json.dumps()中的obj可以是Python的列表或字典类型，当obj为字典时，
dumps()函数将其转换为JSON格式的字符串类型。
默认生成的字符串是顺序存放，sort_keys可以对字典元素按照key进行排序，输出控制结果
indent参数用于增加缩进空格数。
"""
dt = {'b': 2, 'c': 4, 'a': 6}
s1 = json.dumps(dt)  # dumps返回JSON格式的字符串类型
s2 = json.dumps(dt, sort_keys=True, indent=4)
print(s1)
print(s2)
print(s1 == s2)
dt2 = json.loads(s2)
print(dt2, type(dt2))
