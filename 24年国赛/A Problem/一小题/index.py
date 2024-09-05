import numpy as np
import matplotlib.pyplot as plt

# 定义螺旋线的参数
theta = np.linspace(0, 30 * np.pi, 22400)  # 生成从0到4π的1000个点
r = theta  # 螺旋线的半径随着θ线性增加，你可以根据需要修改这个表达式

# 计算螺旋线在极坐标下的x和y坐标
x = r * np.cos(theta)
y = r * np.sin(theta)

# 绘制螺旋线
plt.plot(x, y)

# 设置图表标题和坐标轴标签
plt.title('螺旋线')
plt.xlabel('X 轴')
plt.ylabel('Y 轴')

# 显示图表
plt.grid(True)  # 显示网格
plt.axis('equal')  # 保持x轴和y轴比例一致，使螺旋线看起来不扭曲
plt.show()
