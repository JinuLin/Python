# 微实例6.1.2集合类型
"""
集合类型与数学中集合的概念一致，即包含0个或多个数
据项的无序组合。集合中元素不可重复，元素类型只能是
固定数据类型，例如：整数、浮点数、字符串、元组等，
列表、字典和集合类型本身都是可变数据类型，不能作为
集合的元素出现。
"""
"""
哈希运算：
哈希运算可以将任意长度的二进制值映射为较短的固定的二制值，
这个小的值称为哈希值。
哈希值是对数据的一种有损且紧凑的表达表示形式。
Python中，使用hash()函数可以计算任意对象的哈希值。
"""
print(hash("PYTHON"))
print(hash("IS"))
print(hash("GOOD"))
print(hash("PYTHON IS GOOD"))
"""
哈希值与哈希前的内容无关，也和这些内容的组合无关。
"""
"""
由于集合是无序组合，它没有索引和位置的概念，不能分
片，集合中元素可以动态增加或删除。集合用大括号（{}）
表示，可以用赋值语句生成一个集合
"""
S = {425, "BIT", (10, "CS"), 424}
print(S)
T = {425, "BIT", (10, "CS"), 424, 425, "BIT"}
print(T)
"""
由于集合元素是无序的，集合的打印效果与定义顺序可以
不一致。由于集合元素独一无二，使用集合类型能够过滤掉
重复元素。set(x)函数可以用于生成集合。
"""
W = set('apple')
print(W)
V = ("cat", "dog", "tiger", "human")
print(set(V))
"""
集合类型有10个操作符：
S – T 或 S.difference(T)：返回一个新集合，包括在集合S中但不在集合T中的元素
S-=T或S.difference_update(T)：更新集合S，包括在集合S中但不在集合T中的元素
S & T或S.intersection(T)：返回一个新集合，包括同时在集合S和T中的元素
S&=T或S.intersection_update(T)：更新集合S，包括同时在集合S和T中的元素。
S^T或s.symmetric_difference(T)：返回一个新集合，包括集合S和T中元素，但不包括同时在其中的元素
S=^T或s.symmetric_difference_update(T)：更新集合S，包括集合S和T中元素，但不包括同时在其中的元素
S|T或S.union(T)：返回一个新集合，包括集合S和T中所有元素
S=|T或S.update(T)：更新集合S，包括集合S和T中所有元素
S<=T或S.issubset(T)：如果S与T相同或S是T的子集，返回True，否则返回False，可以用S<T判断S是否是T的真子集
S>=T或S.issuperset(T)：如果S与T相同或S是T的超集，返回True，否则返回False，可以用S>T判断S是否是T的真超集

上述操作符表达了集合类型的4种基本操作，交集（&）、并集（|）、差集（-）、补集（^），操作逻辑与数学定义相同
"""
"""
集合类型有10个操作函数或方法:
S.add(x) 如果数据项x不在集合S中，将x增加到s
S.clear() 移除S中所有数据项
S.copy() 返回集合S的一个拷贝
S.pop() 随机返回集合S中的一个元素，如果S为空，产生KeyError异常
S.discard(x) 如果x在集合S中，移除该元素；如果x不在，不报错
S.remove(x) 如果x在集合S中，移除该元素；不在产生KeyError异常
S.isdisjoint(T) 如果集合S与T没有相同元素，返回True
len(S) 返回集合S元素个数
x in S 如果x是S的元素，返回True，否则返回False
x not in S 如果x不是S的元素，返回True，否则返回False
"""
"""
集合类型主要用于三个场景：成员关系测试、元素去重和删除数据项
"""
print("BIT" in {"PYTHON", "BIT", 123, "GOOD"})  # 成员关系测试
tup = ("PYTHON", "BIT", 123, "GOOD", 123)  # 元素去重
print(set(tup))
new_tup = tuple(set(tup) - {'PYTHON'})  # 去重同时删除数据项
print(new_tup)
"""
集合类型与其他类型最大的不同在于它不包含重复元素，
因此，当需要对一维数据进行去重或进行数据重复处理时，一般通过集合来完成。
"""
