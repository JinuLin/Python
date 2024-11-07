"""
abs() id() round() compile() locals()
all() input() set() dir() map()
any() int() sorted() exec() memoryview()
asci() len() str() enumerate() next()
bin() list() tuple() filter() object()
bool() max() type() format() property()
chr() min() zip() frozenset() repr()
complex() oct() getattr() setattr()
dict() open() globals() slice()
divmod() ord() bytes() hasattr() staticmethod()
eval() pow() delattr() help() sum()
float() print() bytearray() isinstance() super()
hash() range() callable() issubclass() vars()
hex() reversed() classmethod() iter() __import()__
"""
ls = [1, 2, 5, 0]
print(all(ls))
"""
all()函数：一般针对组合数据类型，如果其中每个元素都是True，则返回True
否则返回False。需要注意的是，整数0、空字符串""、空列表[]都被当中False。
"""
print(any(ls))
"""
any()函数：与all()函数相反，只要组合数据类型中任一个是True，则返回True
全部元素都是False时返回False。
"""
print(hash("中国，你好"))
"""
hash()函数：对于能够计算哈希的类型返回哈希值。
"""
print(id(ls))
print(id("中国，你好"))
"""
id()函数：对每一个数据返回唯一编编号，数据不同编号不同，
可以通过比较两个变量编号是否相同判断数据是否一致。
Python将数据存储在内存中的地址作为其唯一编号。
"""
print(list(reversed(ls)))
"""
reversed()函数：返回输入组合数据类型的逆序形式。
"""
print(sorted(ls))  # 不改变ls的值
print(ls)
print(sorted(ls, reverse=True))
"""
sorted()函数：对一个序列进行排序，默认从小到大排序。
"""
print(type(ls))
print(type(reversed(ls)))
"""
type()函数返回每个数据对应的类型。
"""
