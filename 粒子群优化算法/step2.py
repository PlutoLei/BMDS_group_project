import numpy as np
import matplotlib as mpl

# 指定默认字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 解决保存图像中‘-’显示为方块的的问题
mpl.rcParams['axes.unicode_minus'] = False

# 计算粒子的适应度值，也就是目标函数值，X的维度是size*2


def fitnessfction(X):
    A = 10
    pi = np.pi
    x = X[:, 0]
    y = X[:, 1]

    return 20 + x ** 2 - 10 * np.cos(2 * pi * x) + y ** 2 - 10 * np.cos(2 * pi * y)


"""
根据速度更新公式更新每个粒子的速度
#种群大小20
:param V:粒子当前的速度矩阵，20*2的矩阵
:param X:粒子当前的位置矩阵，20*2的矩阵
:param ibest:每个粒子历史最优位置，20*2的矩阵
:param gbest:种群历史最优位置，1*2矩阵
"""


def velupdate(V, X, ibest, gbest, c1, c2, w, max_val):
    # 种群大小
    size = X.shape[0]
    # 生成size个0-1之间的随机数
    r1 = np.random.random((size, 1))
    r2 = np.random.random((size, 1))
    # 对照公式写
    V = w * V + c1 * r1 * (ibest - X) + c2 * r2 * (gbest - X)
    # 防越界处理
    V[V < -max_val] = -max_val
    V[V > max_val] = max_val
    return V


"""
根据公式更新粒子位置
:param X:粒子当前的位置矩阵，20*2的矩阵
:param V:粒子当前的速度矩阵，20*2的矩阵
"""


def pstionupdate(X, V):
    return X + V
