import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'FangSong', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

def square_wave_fourier(x1, n1_terms):
    """
    计算方波的傅里叶级数近似

    参数:
    x: 自变量数组
    n_terms: 级数项数

    返回:
    方波的傅里叶级数近似值
    """
    # 方波的傅里叶级数: f(x) = (4/π) * Σ [sin((2n-1)x) / (2n-1)]
    result = np.zeros_like(x1)
    for n1 in range(1, n1_terms + 1):
        # 只包含奇数项
        harmonic = 2 * n1 - 1
        result += np.sin(harmonic * x1) / harmonic
    return (4 / np.pi) * result

# 创建x轴数据
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 创建图形
plt.figure(figsize=(12, 8))

# 绘制不同项数的傅里叶级数近似
terms_list = [1, 3, 5, 10, 50]
colors = ['red', 'orange', 'green', 'blue', 'purple']

# 绘制各项近似
for i, (n_terms, color) in enumerate(zip(terms_list, colors)):
    y_approx = square_wave_fourier(x, n_terms)
    plt.plot(x, y_approx, label=f'{n_terms} 项', color=color, linewidth=1.5)

# 绘制理想方波作为参考
y_exact = np.sign(np.sin(x))
plt.plot(x, y_exact, '--', color='black', linewidth=1, label='理想方波')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('方波的傅里叶级数表示')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim(-2 * np.pi, 2 * np.pi)
plt.ylim(-1.5, 1.5)

# 添加x轴标记
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
           [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$'])

plt.tight_layout()
# 保存第一张图片
plt.savefig('square_wave_fourier_series.jpg', dpi=300, bbox_inches='tight')
plt.show()

# 绘制收敛过程的动画效果（可选）
plt.figure(figsize=(10, 6))
# 选择一个特定点来观察收敛过程
x_point = np.pi/2  # 在这个点上，方波值为1

n_range = range(1, 101)
convergence_values = []

for n in n_range:
    approx_value = square_wave_fourier(np.array([x_point]), n)[0]
    convergence_values.append(approx_value)

plt.plot(n_range, convergence_values, 'b-', linewidth=1.5)
plt.axhline(y=1, color='r', linestyle='--', label='真实值 = 1')
plt.xlabel('级数项数')
plt.ylabel('近似值')
plt.title(f'傅里叶级数在 x = π/2 处的收敛过程')
plt.grid(True, alpha=0.3)
plt.legend()
# 保存第二张图片
plt.savefig('fourier_convergence.jpg', dpi=300, bbox_inches='tight')
plt.show()
