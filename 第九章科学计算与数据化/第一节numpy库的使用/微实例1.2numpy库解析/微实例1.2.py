# 微实例9.1.2numpy库解析
"""
numpy 库常用的创建数组函数
np.array([x,y,z], dtype=int) 从Python列表和元组创造数组
np.arange(x,y,i) 创建一个由x到y，以i为步长的数组
np.linspace(x,y,n) 创建一个由x到y，等分成n个元素的数组
np.indices((m,n)) 创建一个m行n列的矩阵
np.random.rand(m,n) 创建一个m行n列的随机数组
np.ones((m,n),dtype) 创建一个m行n列全1的数组，dtype是数据类型
np.empty((m,n),dtype) 创建一个m行n列全0的数组，dtype是数据类型
"""
"""
创建一个简单的数组后，可以查看ndarray类型有一些基本属性
ndarray类的常用属性：
ndarray.ndim 数组轴的个数，也被称作秩
ndarray.shape 数组在每个维度上大小的整数元组
ndarray.size 数组元素的总个数
ndarray.dtype 数组元素的数据类型，dtype类型可以用于创建数组中
ndarray.itemsize 数组中每个元素的字节大小
ndarray.data 包含实际数组元素的缓冲区地址
ndarray.flat 数组元素的迭代器
"""
import numpy as np

a = np.ones((4, 5))
print(a)

print(a.ndim)
print(a.shape)
print(a.dtype)

"""
数组在numpy中被当作对象，可以采用<a>.<b>()方式调用一些方法。
这里给出了改变数组基础形态的操作方法，例如改变和调换数组维度等。
其中，np.flatten()函数用于数组降维，相当于平铺数组中数据，该功能在矩阵运算及图像处理中用处很大。

ndarray类的形态操作方法：
ndarray.reshape(n,m) 不改变数组ndarray，返回一个维度为(n,m)的数组
ndarray.resize(new_shape) 与reshape()作用相同，直接修改数组ndarray
ndarray.swapaxes(ax1,ax2) 将数组n个维度中任意两个维度进行调换
ndarray. flatten() 对数组进行降维，返回一个折叠后的一维数组
ndarray.ravel() 作用同 np.flatten()，但是返回数组的一个视图
"""

"""
数组切片得到的是原始数组的视图，所有修改都会直接反映到源数组。
如果需要得到的ndarray切片的一份副本，需要进行复制操作，比如arange[5:8].copy()

ndarray类的索引和切片方法:
x[i] 索引第i个元素
x[-i] 从后向前索引第i个元素
x[n:m] 默认步长为 1，从前往后索引，不包含m
x[-m:-n] 默认步长为 1，从后往前索引，结束位置为n
x[n,m,i] 指定i步长的由 n到m 的索引
"""
a = np.random.rand(5, 3)  # 创建一个5行3列的随机数组
print(a[2])  # 获得2行的数据
print(a[1:3])
print(a[-5:-2:2])

"""
numpy库中提供了一批运算函数。
这些函数中，输出参数y可选，
如果没有指定，将创建并返回一个新的数组保存计算结果，
如果指定参数，则将结果保存到参数中。
例如，两个数组相加可以简单地写为a+b，而np.add(a,b,a)则表示a+=b。

numpy库的算术运算函数
np.add(x1,x2 [,y])：y=x1+ x2
np.subtract(x1,x2 [,y])：y=x1-x2
np.multiply(x1,x2 [y])：y=x1*x2
np.divide(x1,x2 [,y])：y=x1/x2
np floor_divide(x1,x2[,y])：y=x1//x2，返回值取整
np.negative(x[,y])：y=-x
np.power(x1,x2[,y])：y=x1**x2
np.remainder(x1,x2[,y])：y=x1%x2
"""
"""
numpy库的比较运算函数
np.equal(x1,x2 [,y])：y=x1==x2
np.not_equal(x1,x2 [y])：y=x1!=x2
np.less(x1,x2,[,y])：y=x1<x2
np.less equal(x1,x2,[,y])：y=x1<=x2
np.greater(x1,x2,[y])：y=x1>x2
np.greater_equal(x1,x2,[,y])：y=x1>=x2
np.where(condition[x,y])：根据给出的条件判断输出x还是y
"""
print(np.less([1, 2], [2, 2]))
# 其将返回一个布尔数组，它包含两个数组中对应元素值的比较结果

"""
numpy库的其他函数
np.abs(x) 计算基于元素的整形，浮点或复数的绝对值
np.sqrt(x) 计算每个元素的平方根
np.squre(x) 计算每个元素的平方
np.sign(x) 计算每个元素的符号：1(+)、0、-1(-)
np.ceil(x) 计算大于或等于每个元素的最小值
np.floor(x) 计算小于或等于每个元素的最大值
np.rint (x[,out]) 圆整，取每个元素为最近的整数,保留数据类型
np.exp(x[,out]) 计算每个元素指数值
np.log(x),np.log10(x),np.log2(x) 计算自然对数(e),基于 10,2 的对数,log(1+x)
"""
