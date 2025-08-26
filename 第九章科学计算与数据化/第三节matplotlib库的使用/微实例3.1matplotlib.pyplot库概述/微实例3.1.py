# 微实例9.3.1matplotlib.pyplot 库概述
"""
matplotlib 是提供数据绘图功能的第三方库，
pyplot子库主要用于实现各种数据展示图形的绘制。
"""
"""
为了正确显示中文字体，用以下代码更改默认设置，其中'SimHei'表示黑体字。
"""
import matplotlib
matplotlib.rcParams ['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
"""
matplotlib 库由一系列有组织有隶属关系的对象构成，这对于基础绘图操作来说显得过于复杂。
因此，matplotlib 提供了一套快捷命令式的绘图接口函数，即pyplot 子模块。
pyplot 将绘图所需要的对象构建过程封装在函数中，对用户提供了更加友好的接口。
pyplot 模块提供一批预定义的绘图函数，大多数函数可以从函数名辨别它的功能。
"""
"""
字体是计算机显示字符的方式，均由人工设计，并采用字体库方式部署在计算机中。
西文和中文字体都有很多种类，下表给出最常用的10 种中文字体及其英文表示，
这些字体的英文表示在程序设计中十分常用，但需要注意，部分字体无法在matplotlib库中使用。
宋体SimSun
黑体SimHei
楷体KaiTi
微软雅黑Microsoft YaHei
隶书LiSu
仿宋FangSong
幼圆YouYuan
华文宋体STSong
华文黑体STHeiti
苹果丽中黑Apple LiGothic Medium
"""
import matplotlib.pyplot as plt
"""
plt子库提供了一批操作和绘图函数，每个函数代表对图像进行的一个操作，
比如创建绘图区域、添加标注或者修改坐标轴等。
这些函数采用plt.<b>()形式调用，其中<b>是具体函数名称。
"""
"""
plt库的绘图区域函数
plt.figure(figsize=None,facecolo1-None) 创建一个全局绘图区域
plt.axes(rect. axisbg-'w') 创建一个坐标系风格的子绘图区域
plt.subplot(rows. ncols. plot nuber) 在全局绘图区域中创建一个子绘图区域
plt.subplots adjustO 调整子图区域的布局
"""
"""
使用figure()函数创建一个全局绘图区域，并且使它成为当前的绘图对象，
figsize参数可以指定绘图区域的宽度和高度，单位为英寸。
鉴于figure()函数参数较多，采用指定参数名称的方式输入参数。
"""
plt.figure(figsize=(8,4))
"""
subplot()都用于在全局绘图区域内创建子绘图区域，
其参数表示将全局绘图区域分成nrows行和ncols列，
并根据先行后列的计数方式在plot_number位置生成一个坐标系。
"""
plt.subplot (324)
plt.show()
"""
axes()默认创建一个subplot(111)坐标系，
参数rec=[left,bottom,width,height]中四个变量的范围都为[0,1]，
表示坐标系与全局绘图区域的关系；axisbg指背景色，默认为white。
"""
plt.axes((0.1, 0.1, 0.7, 0.3), facecolor='y')
plt.show()

"""
plt子库提供了一组读取和显示相关函数，
用于在绘图区域中增加显示内容及读入数据，
这些函数需要与其他函数搭配使用。
"""
"""
plt读取和显示函数
plt.legend() 在绘图区域中方式绘图标签（也称图注）
plt.showo() 显示创建的绘图对象
plt.matshow() 在窗口显示数组矩阵
plt.imshow 在axes上显示图像 
plt.imsave() 保存数组为图像文件
plt.imread() 从图像文件中读取数组
"""
