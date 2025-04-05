# 微实例3.3.1math库的使用
import math

# math库里包括4个数学常数:
# math.pi 圆周率，值为3.141592653589793
# math.e  自然对数，值为2.718281828459045
# math.inf 正无穷大，负无穷大为-math.inf
# math.nan 非浮点数标记，NaN（Not a Number）
print(math.e)
a = math.pi * 2  # 可以直接所用运算
print("{}".format(a))

# math库里包含16个数值表示函数
# math.fabs(x) 返回x的绝对值
# math.fmod(x, y) x % y 返回x与y的模
# math.fsum([x,y,…]) x+y+… 浮点数精确求和
# math.ceil(x) 向上取整，返回不小于x的最小整数
# math.floor(x) 向下取证，返回不大于x的最大整数
# math.factorial(x) x! 返回x的阶乘，如果x是小数或负数，返回ValueError
# math.gcd(a, b) 返回a与b的最大公约数
# math.frepx(x) x = m * 2e 返回(m, e)，当x=0，返回(0.0, 0)
# math.ldexp(x, i) x * 2i 返回x * 2
# i运算值，math.frepx(x)函数的反运算
# math.modf(x) 返回x的小数和整数部分
# math.trunc(x) 返回x的整数部分
# math.copysign(x, y) 用数值y的正负号替换数值x的正负号
# math.isclose(a,b) 比较a和b的相似性，返回True或False
# math.isfinite(x) 当x为无穷大，返回True；否则，返回False
# math.isinf(x) 当x为正数或负数无穷大，返回True；否则，返回False
# math.isnan(x) 当x是NaN，返回True；否则，返回False
b = 0.1 + 0.2 + 0.3
print("{}".format(b))
c = math.fsum([0.1, 0.2, 0.3])
print("{}".format(c))  # 在数学求和运算当中十分有用

# math库包含8个幂对数函数
# math.pow(x,y) 返回x的y次幂
# math.exp(x)  返回e的x次幂，e是自然对数
# math.expml(x) 返回e的x次幂减1
# math.sqrt(x) 返回x的平方根
# math.log(x[,base]) 返回x的对数值，只输入x时，返回自然对数，即lnx
# math.log1p(x) 返回1+x的自然对数值
# math.log2(x) 返回x的2对数值
# math.log10(x) 返回x的10对数值
d = math.pow(10, 1 / 3)  # math库里面没有提供x的y次方根，可以转化为x^(1/y)
print("{}".format(d))

# math库包含16个三角运算函数
# math.degrees(x) 角度x的弧度值转角度值
# math.radians(x) 角度x的角度值转弧度值
# math.hypot(x,y) 返回(x,y)坐标到原点(0,0)的距离
# math.sin(x)  返回x的正弦函数值，x是弧度值
# math.cos(x)  返回x的余弦函数值，x是弧度值
# math.tan(x)  返回x的正切函数值，x是弧度值
# math.asin(x)  返回x的反正弦函数值，x是弧度值
# math.acos(x)  返回x的反余弦函数值，x是弧度值
# math.atan(x)  返回x的反正切函数值，x是弧度值
# math.atan2(y,x)  返回y/x的反正切函数值，x是弧度值
# math.sinh(x)  返回x的双曲正弦函数值
# math.cosh(x)  返回x的双曲余弦函数值
# math.tanh(x)  返回x的双曲正切函数值
# math.asinh(x)  返回x的反双曲正弦函数值
# math.acosh(x)  返回x的反双曲余弦函数值
# math.atanh(x) 返回x的反双曲正切函数值
print(math.atan(1) * 4)  # arctan1的值是π/4，可以用math中的atan获得π的值

# math库包含4个高等特殊函数
# math.erf(x) 高斯误差函数，应用于概率论、统计学等领域
# math.erfc(x) 余补高斯误差函数，math.erfc(x)=1 - math.erf(x)
# math.gamma(x) 伽玛（Gamma）函数，也叫欧拉第二积分函数
# math.lgamma(x) 伽玛函数的自然对数
print(math.factorial(10))  # 这个函数只能计算非负整数的阶乘
print(math.gamma(11))
print(math.gamma(0.5))
print(math.gamma(-10.2))
# 伽玛函数能计算浮点数的阶乘
