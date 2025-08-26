# 微实例9.5.2霍兰德人格分析雷达图
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
radar_labels = np.array(['研究型(I)', '艺术型(A)', '社会型(S)', '企业型(E)', '常规型(C)', '现实型(R)'])
nAttr = 6
data = np.array([[0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
                 [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
                 [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
                 [0.30, 0.25, 0.48, 0.85, 0.45, 0.40],
                 [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
                 [0.34, 0.31, 0.38, 0.40, 0.92, 0.28]])  # 数据值
data_labels = ('工程师', '实验员', '艺术家', '推销员', '社会工作者', '记事员')
angles = np.linspace(0, 2 * np.pi, nAttr, endpoint=False)
# 为角度和标签添加闭合点
angles = np.concatenate((angles, [angles[0]]))
radar_labels = np.concatenate((radar_labels, [radar_labels[0]]))

# 为每个数据系列单独添加闭合点
closed_data = []
for i in range(len(data)):
    closed_data.append(np.concatenate((data[i], [data[i][0]])))
data = np.array(closed_data)

fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
# plt.plot(angles,data,'bo-',color ='gray',linewidth=1,alpha=0.2)
plt.plot(angles, data.T, 'o-', linewidth=1.5, alpha=0.2)
for i in range(len(data)):
    plt.fill(angles, data[i], alpha=0.25)

# 设置角度网格标签
plt.thetagrids(angles[:-1] * 180 / np.pi, radar_labels[:-1])

plt.ylim(0, 1)  # 设置径向范围从0到1
plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0])  # 显示指定的径向刻度，保持0.2间隔的风格

plt.figtext(0.52, 0.95, '霍兰德人格分析', ha='center', size=20)
legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize='small')
plt.grid(True)
plt.savefig('holland_radar.JPG')
plt.show()
