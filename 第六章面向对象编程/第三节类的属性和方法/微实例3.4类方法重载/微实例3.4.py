# 微实例6.3.4类方法重载
"""
Python类方法重载主要是运算符重载。
运算符重载：主要有算术运算符重载、比较算术运算符重载、 位操作运算符重载、索引和切片运算符重载等。
"""
"""
__add__ 	加法运算 	对象加法:x+y,x+=y
__sub__ 	减法运算 	对象减法:x-y,x-=y
__mul__ 	乘法运算 	对象乘法:x*y,x*=y
__div__ 	除法运算 	对象除法:x/y,x/=y
__mod__ 	求余运算 	对象运算:x%y,x%=y
__bool__ 	真值测试 	测试对象是否为真值:bool(x)
__repr__、__str__ 	打印、转换 	print(x) 、repr(x) 、str(x)
__contains__ 	成员测试 	iteminx
__getitem__ 	索引、分片 	x[i]、x[i:j]、没有__iter__的for循环等
__setitem__ 	索引赋值 	x[i]=值、x[i:j]=序列对象
__delitem__ 	索引和分片删除 	delx[i]、delx[i:j]
__len__ 	求长度 	len(x)
__iter__、__next__ 	迭代 	iter(x) 、next(x) 、for循环等
__eq__、__next__ 	相等测试、不等于测试 	x==y、x! =y
__ge__、__gt__ 	大于等于测试、大于测试 	x>=y、x>y
__le__、__lt__ 	小于等于测试、小于测试 	x<=y、x<y
"""
"""
1.算术运算符重载
算术运算符重载可以让自定义的类对象进行算术运算操作。
"""
#加法运算符重载
class Addition:
	def __init__(self,obj):
		self.data = obj[:]
	#实现加法运算的重载，将两个列表对应元素进行相加
	def __add__(self,obj):
		x = len(self.data)
		y = len(obj.data)
		m =x if x > y else y
		ls = []
		for i in range(m):
			ls.append(self.data[i] + obj.data[i])
		#返回包含新列表的实例对象
		return Addition(ls[:])
#创建实例对象并初始化
ls1 = Addition([1,2,3])
ls2 = Addition([11,22,33])
#执行加法运算
ls_sum = ls1 + ls2
print(ls_sum.data)

"""
2.索引和分片重载
索引和分片重载可以让自定义的类对象进行索引和分片操作。 
"""
class Index:
	data = [1,2,3,4,5]
	def __getitem__(self,item):
		return self.data[item]
index = Index()
print(index[0])     	#索引返回单个值
print(index[:])     	#分片返回全部的值
print(index[:2])    	#分片返回部分值
for i in index:    	#for循环迭代
	print(i)
