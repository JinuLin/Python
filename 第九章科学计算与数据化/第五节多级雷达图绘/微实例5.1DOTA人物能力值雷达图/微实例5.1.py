# 微实例9.5.1DOTA人物能力值雷达图
"""
雷达图是通过多个离散属性比较对象的最直观工具。
游戏角色中经常出现表示人物能力值的雷达图。
DOTAMAX测试版曾经推出过显示玩家能力值分布的雷达图，
只要点击自己或是好友头像，
就可以看到能力值在综合、KDA、发育、推进、生存、输出等方面的能力分布
"""
"""
在一组同心圆上填充不规则六边形，其每个顶点到圆心的距离代表人物某个属性的数据。
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
labels = np.array(['综合', 'KDA', '发育', '推进', '生存', '输出'])
nAttr = 6
data = np.array([7, 5, 6, 9, 8, 7])  # 数据值
angles = np.linspace(0, 2 * np.pi, nAttr, endpoint=False)
"""
np.linspaces()函数设定起点为0、末值为2π、返回一个两端点间数值平均分布的长为nAttr的数组angles，
它表示从一个属性点到下一个属性点笔画需要旋转的角度，
它取决于属性nAttr的大小，也是雷达图的多边形边数。
"""
# 为了形成闭合图形，需要在数据末尾添加第一个数据点
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
"""
np.concatenate()函数用于将数据和角度的数组首尾闭合起来，便于调用plot()函数绘制。
"""
# 但是标签只需要6个，所以需要调整thetagrids的使用方式
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
"""
建立基本绘图对象后，使用subplot()函数建立极坐标系的子分区。
Polar参数指定了绘制类型为极坐标，这是subplot()除默认正方形坐标系外唯一支持的内置坐标图。
"""
plt.plot(angles, data, 'o-', color='g', linewidth=2)
plt.fill(angles, data, facecolor='g', alpha=0.25)
"""
建立极坐标后，使用plot()函数依照data提供的数据画出不规则六边形，
然后使用fill()函数填充半透明颜色。
"""
# 使用前6个角度值来设置标签位置
label_angles = np.linspace(0, 2 * np.pi, nAttr, endpoint=False)
plt.thetagrids(label_angles * 180 / np.pi, labels)
"""
thetagrids()函数为极坐标设置标签，这里把标签安放在六角形的顶点上，需要将角度数据和文字一起作为参数传给thetagrids函数。
"""
# 设置径向轴刻度为1-9级，并限制显示范围
plt.yticks(range(1, 10))  # 显示1~9刻度
plt.ylim(0, 9)  # 设置径向轴显示范围从0到9
plt.figtext(0.52, 0.95, 'DOTA能力值雷达图', ha='center')
plt.grid(True)
plt.savefig('dota_radar.JPG')
plt.show()
