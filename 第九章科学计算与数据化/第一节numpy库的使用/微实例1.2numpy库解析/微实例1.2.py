# 微实例9.1.2
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
