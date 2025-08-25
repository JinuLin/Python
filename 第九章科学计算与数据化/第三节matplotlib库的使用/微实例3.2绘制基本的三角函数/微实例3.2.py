# 微实例9.3.2绘制基本的三角函数
"""
plot()函数是用于绘制直线的最基础函数，调用方式很灵活，
x和y可以是numpy计算出的数组，并用关键字参数指定各种属性。
其中，label 表示设置标签并在图例(legend)中显示，
color 表示曲线的颜色，linewidth 表示曲线的宽度。
在字符串前后添加"$"符号，matplotlib会使用其内置的latex引擎绘制的数学公式。
"""
"""
plt库的基础图表函数
plt.polt(x,y,label,color,width) 根据x,y数组绘制直/曲线
plt.boxplot(data,notch,position) 绘制一个箱型图(Box-plot)
plt.bar(left,height,width,bottom) 绘制一个条形图
plt.barh(bottom,width,height,left) 绘制一个横向条形图
plt.polar(theta,r) 绘制极坐标图
plt.pie(data,explode) 绘制饼图
plt.psd(x,NFFT=256,pad_to,Fs) 绘制功率谱密度图
plt.specgram(x,NFFT=256,pad_to,F) 绘制谱图
plt.cohere(x,y,NFFT=256,Fs) 绘制X-Y的相关性函数
plt.scatter() 绘制散点图(x,y是长度相同的序列)
plt.step(x,y,where) 绘制步阶图
plt.hist(x,bins,normed) 绘制直方图
plt.contour(X,Y,Z,N) 绘制等值线
plt.vlines() 绘制垂直线
plt.stem(x,y,linefmt,markerfmt,basefmt) 绘制曲线每个点到水平轴线的垂线
plt.plot_date() 绘制数据日期
plt.plotfile() 绘制数据后写入文件
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 6, 100)
y = np.cos(2*np.pi*x) * np.exp(-x) +0.8
plt.plot(x, y, "k", color="r", linewidth=3,linestyle="-")
plt.show()
