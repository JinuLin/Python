# 微实例9.3.4带标签的坐标系
"""
plt 库的标签设置函数：
plt.figlegend(handles,label,loc) 为全局绘图区域放置图注
plt.legendo 为当前坐标图放置图注
plt.xlabel(s) 设置当前x轴的标签
plt.ylabel(s) 设置当前y轴的标签
plt.xticks(array,'a','b','c') 设置当前x轴刻度位置的标签和值
plt.yticks(array,'a','b','c') 设置当前y轴刻度位置的标签和值
plt.clabel(cs,v) 为等值线图设置标签
plt.get_figlabels() 返回当前绘图区域的标签列表
plt.figtext(x,y,s,fontdic) 为全局绘图区域添加文字
plt.title() 设置标题
plt.suptitle() 为当前绘图区域添加中心标题
plt.text(x,y,s,fontdic,withdash) 为坐标图轴添加注释
plt.annotate(note,xy,xytext,xycoords,textcoords,arrowprops) 用箭头在指定数据点创建一个注释或一段文本
"""
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.plot([1, 2, 4], [1, 2, 3])
plt.title("坐标系标题")
plt.xlabel('时间 (s)')
plt.ylabel('范围 (m)')
plt.xticks([1, 2, 3, 4, 5], [r'$\pi/3$', r'$2\pi/3$', r'$\pi$',
                             r'$4\pi/3$', r'$5\pi/3$'])
plt.show()
