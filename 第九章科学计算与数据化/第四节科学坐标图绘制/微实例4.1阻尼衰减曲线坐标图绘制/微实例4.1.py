# 微实例9.4.1阻尼衰减曲线坐标图绘制
"""
科学坐标图绘制有4个要素：坐标轴、数据曲线、标题和图注。
这个实例以阻尼衰减曲线绘制来具体阐述科学坐标系的绘制方法。
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']


def draw(pcolor, nt_point, nt_text, nt_size):
    plt.plot(x, y, 'k', label="$exp_decay$", color=pcolor, linewidth=3, linestyle="-")
    plt.plot(x, z, "b--", label="$cos(x^2)$", linewidth=1)
    plt.xlabel('时间(s)')
    plt.ylabel('幅度(mV)')
    plt.title("阻尼衰减曲线绘制")
    plt.annotate('$\cos(2 \pi t) \exp(-t)$', xy=nt_point, xytext=nt_text, fontsize=nt_size,
                 arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.1"))


def shadow(a, b):
    ix = (x > a) & (x < b)
    plt.fill_between(x, y, 0, where=ix, facecolor='grey', alpha=0.25)
    plt.text(0.5 * (a + b), 0.2, "$\int_a^b f(x)\mathrm{d}x$",
             horizontalalignment='center')


def xy_axis(x_start, x_end, y_start, y_end):
    plt.xlim(x_start, x_end)
    plt.ylim(y_start, y_end)
    plt.xticks([np.pi / 3, 2 * np.pi / 3, 1 * np.pi, 4 * np.pi / 3, 5 * np.pi / 3],
               ['$\pi/3$', '$2\pi/3$', '$\pi$', '$4\pi/3$', '$5\pi/3$'])


x = np.linspace(0.0, 6.0, 100)
y = np.cos(2 * np.pi * x) * np.exp(-x) + 0.8
z = 0.5 * np.cos(x ** 2) + 0.8
note_point, note_text, note_size = (1, np.cos(2 * np.pi) * np.exp(-1) + 0.8), (1, 1.4), 14
fig = plt.figure(figsize=(8, 6), facecolor="white")
plt.subplot(111)
draw("red", note_point, note_text, note_size)
xy_axis(0, 5, 0, 1.8)
shadow(0.8, 3)
plt.legend()
plt.savefig('sample.JPG')
plt.show()
