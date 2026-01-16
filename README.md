# Python 全方位学习教程 🐍

一个完整的 Python 学习体系,从零基础入门到高级应用,包含10个章节共185个代码实例。

## 📚 项目简介

本项目系统性地涵盖了 Python 编程的各个方面,通过大量微实例和练习题帮助学习者循序渐进地掌握 Python 技能。每个章节都配有详细的代码注释和配套习题,适合初学者系统学习,也可作为教学参考资料。

## ✨ 项目特色

- 📖 **系统性强**: 10个章节从入门到进阶,知识体系完整
- 💻 **实例丰富**: 185个Python代码文件,每个知识点都有对应示例
- 📝 **注释详尽**: 代码注释包含知识点说明和原理解释
- 🎯 **练习充分**: 每章都有配套习题,理论实践相结合
- 🛠️ **实用导向**: 涵盖爬虫、数据可视化、图像处理等实际应用
- 🌐 **中文友好**: 大量中文文本处理示例(jieba分词、中文词频统计等)
- 📚 **库覆盖广泛**: 涉及10+个标准库和6个常用第三方库

## 📋 目录结构

### 第一章 初识Python语言 (13个文件)
Python基础入门,包括变量、运算、格式化输出等基础概念
- 圆面积的计算
- 简单的人机对话
- 斐波那契数列
- 同切圆绘制
- 九九乘法表等

### 第二章 Python程序实例解析 (15个文件)
通过经典实例理解Python编程思维
- 温度转换实例(华氏度/摄氏度)
- 蟒蛇绘制(turtle图形)
- 汇率转换程序
- 多种几何图形绘制

### 第三章 基本数据类型 (约20个文件)
Python核心数据类型详解
- 数字类型(整数、浮点数、复数)
- math库的使用
- 字符串操作
- 文本进度条实现
- 格式化输出

### 第四章 程序的控制结构 (约30个文件)
程序流程控制
- 分支结构(PM2.5空气质量提醒)
- 循环结构
- random库的使用
- π的计算(蒙特卡罗方法)
- 异常处理

### 第五章 函数和代码复用 (约25个文件)
函数定义与模块化编程
- 函数的基本使用
- 参数传递(可选参数、可变参数)
- datetime库
- 七段数码管绘制
- 函数递归(阶乘、科赫曲线)

### 第六章 面向对象编程 (约15个文件)
OOP基础与应用
- 类和对象的创建
- 封装、继承、多态
- 实例属性/类属性
- 私有属性和方法
- 类方法重载

### 第七章 组合数据类型 (约25个文件)
列表、字典、集合等复合数据类型
- 列表操作
- 基本统计值计算
- 字典操作
- jieba中文分词
- 文本词频统计(Hamlet、三国演义)
- Python之禅

### 第八章 文件和数据格式化 (约20个文件)
文件操作与数据格式
- 文件读写
- PIL图像处理
- 图像字符画绘制
- CSV格式处理
- JSON数据编码/解码
- HTML数据展示

### 第九章 科学计算与数据可视化 (14个文件)
numpy和matplotlib的应用
- numpy多维数组
- 图像手绘效果(基于梯度)
- matplotlib绘图
- 科学坐标图(阻尼衰减曲线)
- 多级雷达图(DOTA人物能力值、霍兰德人格分析)

### 第十章 网络爬虫和自动化 (10个文件)
网络数据获取与处理
- requests库使用
- beautifulsoup4 HTML解析
- 中国大学排名爬虫
- 百度搜索关键词自动提交
- Robots协议

## 🛠️ 技术栈

### 标准库
- **turtle** - 图形绘制
- **math** - 数学运算
- **random** - 随机数生成
- **datetime** - 日期时间处理
- **json** - JSON数据格式
- **time** - 时间处理

### 第三方库
- **jieba** - 中文分词
- **PIL (Pillow)** - 图像处理
- **numpy** - 科学计算
- **matplotlib** - 数据可视化
- **requests** - HTTP请求
- **beautifulsoup4** - HTML/XML解析

## 📦 安装依赖

```bash
pip install jieba pillow numpy matplotlib requests beautifulsoup4
```

## 🚀 快速开始

1. 克隆项目到本地
```bash
git clone https://github.com/yourusername/Python-main.git
```

2. 进入任意章节目录
```bash
cd "第一章初识Python语言/微实例1.1圆面积的计算/"
```

3. 运行Python代码
```bash
python 微实例1.1.py
```

## 📖 学习路径建议

### 初学者路径
1. 第一章 → 第二章 → 第三章 → 第四章 → 第五章
2. 重点掌握基础语法、数据类型、控制结构、函数

### 进阶路径
3. 第六章 → 第七章 → 第八章
4. 学习面向对象、组合数据类型、文件操作

### 实战应用路径
5. 第九章 → 第十章
6. 科学计算、数据可视化、网络爬虫

## 💡 代表性案例

### 1. 温度转换 (第二章)
展示条件分支、eval()函数、字符串操作
```python
TempStr = input("请输入带有符号的温度值: ")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print("转换后的温度是{:.2f}C".format(C))
```

### 2. 蟒蛇绘制 (第二章)
turtle图形库经典应用
```python
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()
```

### 3. 文本词频统计 (第七章)
字典、jieba库、排序综合应用
```python
import jieba
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
```

### 4. 数据可视化 (第九章)
matplotlib雷达图绘制
```python
import matplotlib.pyplot as plt
import numpy as np

labels = np.array(['综合', 'KDA', '发育', '推进', '生存', '输出'])
data = np.array([7, 5, 6, 9, 8, 7])
angles = np.linspace(0, 2 * np.pi, 6, endpoint=False)
plt.subplot(111, polar=True)
plt.plot(angles, data, 'o-', color='g', linewidth=2)
plt.fill(angles, data, facecolor='g', alpha=0.25)
plt.show()
```

### 5. 网络爬虫 (第十章)
requests和beautifulsoup4组合使用
```python
import requests
from bs4 import BeautifulSoup

def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except requests.RequestException:
        return ""
```

## 📊 项目统计

- 总章节数: 10章
- Python文件数: 185个
- 文本数据文件: 13个
- 参考图片: 9张
- 涉及的第三方库: 6个
- 标准库: 10+个

## 📝 使用说明

1. 每个章节按知识点分节,便于针对性学习
2. 微实例: 简短代码,展示特定知识点
3. 习题: 巩固练习,检验学习成果
4. 图片资料: 章节知识点快速参考
5. 文本数据: 配合文本处理案例使用

## 🤝 贡献指南

欢迎提交Issue和Pull Request!

## 📄 许可证

MIT License

## 📧 联系方式

如有问题或建议,欢迎通过Issue联系。

---

**Happy Coding!** 🎉
