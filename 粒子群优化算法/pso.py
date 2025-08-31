import matplotlib.pyplot as plt
import numpy as np
from step2 import fitnessfction, velupdate, pstionupdate


def pso():
    # PSO的参数
    # 惯性因子，一般取1
    w = 1
    # 学习因子，一般取2
    c1 = 2
    c2 = 2
    # 为两个（0，1）之间的随机数
    r1 = None
    r2 = None
    # 维度
    dim = 2
    # 种群大小
    size = 20
    # 算法最大迭代次数
    iter_num = 1000
    # 限制粒子最大速度为0.5
    max_val = 0.5
    # 初始的适应度，在迭代过程中不断减小这个值
    best_fitness = float(9e10)
    # 记录每次迭代过程中的种群适应度值变化
    fitness_value_list = []
    # 初始化种群的各个粒子位置
    # 用一个20*2的矩阵表示种群，每行表示一个粒子
    # 2维，表示x，y
    X = np.random.uniform(-5.12, 5.12, size=(size, dim))
    # 初始化种群的各个粒子的速度
    # 2维，表示x，y速度
    V = np.random.uniform(-0.5, 0.5, size=(size, dim))
    # 计算种群各个粒子的初始适应度
    ifitness = fitnessfction(X)
    # 计算种群的初始最优适应度值
    grpfitness = ifitness.min()
    # 添加到记录中
    fitness_value_list.append(grpfitness)
    # 初始的个体最优位置和种群最优位置
    ibest = X
    gbest = X[ifitness.argmin()]
    # 下来进行迭代
    for i in range(1, iter_num):
        # 更新速度
        V = velupdate(V, X, ibest, gbest, c1, c2, w, max_val)
        # 更新位置
        X = pstionupdate(X, V)
        # 计算各个粒子适应度
        ifitness2 = fitnessfction(X)
        # 计算群体最优适应度
        grpfitness2 = ifitness2.min()
        # 更新每个粒子的历史最优位置
        for j in range(size):
            if ifitness[j] > ifitness2[j]:
                ibest[j] = X[j]
                ifitness[j] = ifitness2[j]
        # 更新群体最优位置
        if grpfitness > grpfitness2:
            gbest = X[ifitness2.argmin()]
            grpfitness = grpfitness2
        # 记录迭代最优结果
        fitness_value_list.append(grpfitness)
        # 迭代次数+1
        i += 1

    # 打印迭代结果
    print("最优值是：%.5f" % fitness_value_list[-1])
    print("最优解是：x=%.5f,y=%.5f" % (gbest[0], gbest[1]))

    # 绘图
    plt.plot(fitness_value_list, color='r')
    plt.title('迭代过程')
    plt.show()


pso()
