import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 生成x和y的数据
X = np.arange(-5.12, 5.12, 0.1)
Y = np.arange(-5.12, 5.12, 0.1)
X, Y = np.meshgrid(X, Y)
pi = np.pi

Z = 20+X**2-10*np.cos(2*pi*X)+Y**2-10*np.cos(2*pi*Y)

# 绘图
fig = plt.figure()
ax = Axes3D(fig,auto_add_to_figure=False)
fig.add_axes(ax)
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
plt.show()
