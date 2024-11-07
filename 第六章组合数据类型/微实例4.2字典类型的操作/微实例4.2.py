# 微实例6.4.2字典类型的操作
Dcountry = {"中国": "北京", "美国": "华盛顿", "法国": "巴黎"}
print(Dcountry)
Dcountry["英国"] = "伦敦"  # 通过中括号可以增加新的元素
print(Dcountry)

# 直接使用大括号（{}）可以创建一个空的字典，并通过中括号（[]）向其增加元素。
Dp = {}
print(Dp)
Dp['2^10'] = 1024
print(Dp)
# 应注意，集合类型也是用大括号（{}）表示，直接用大括号生成的空的字典，而不是集合。
"""
字典类型的函数和方法：
<d>.keys() 返回所有的键信息
<d>.values() 返回所有的值信息
<d>.items() 返回所有的键值对
<d>.get(<key>,<default>) 键存在则返回相应值，否则返回默认值
<d>.pop(<key>,<default>) 键存在则返回相应值，同时删除键值对，否则返回默认值
<d>.popitem() 随机从字典中取出一个键值对，以元组(key, value)形式返回
<d>.clear() 删除所有的键值对
del <d>[<key>] 删除字典中某一个键值对
<key> in <d> 如果键在字典中返回True，否则返回False
"""
# 使用keys()、values()、items()等方法可以遍历字典中的键、值、键值对。
# 可以用list()将返回的迭代对象转化为列表。
Dcountry = {"中国": "北京", "美国": "华盛顿", "法国": "巴黎"}
print(Dcountry.keys())
print(list(Dcountry.values()))
print(Dcountry.items())
print('中国' in Dcountry)  # 只对键进行判断
print(Dcountry.get('美国', '悉尼'))  # '美国'在字典中存在
print(Dcountry.get('澳大利亚', '悉尼'))  # '澳大利亚'在字典中不存在

"""
与其他组合类型一样，字典可以通过for…in语句对其元
素进行遍历，基本语法结构如下：
for <变量名> in <字典名>:
    语句块
"""
for key in Dcountry:
    print(key)

"""
字典是实现键值对映射的数据结构，请理解如下基本原则：
字典是一个键值对的集合，该集合以键为索引，一个键信息
只对应一个值信息；
字典中元素以键信息为索引访问；
字典长度是可变的，可以通过对键信息赋值实现增加或修改键值对。
"""
