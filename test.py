import numpy as np
import matplotlib.pyplot as plt
import sympy
import sympy as sp
import pandas as pd


# 定义螺距
p = -0.55
# time_v = [0, 60, 120, 180, 240, 300]
# 定义时间
time_v = np.arange(0, 301)
# 龙头节点的x坐标
head_x = []
# 龙头节点的y坐标
head_y = []
# 龙头节点的极角
head_theta = []
# 龙头节点的极径
head_r = []
# 定义龙身的节数
# body_n = np.array(1, 222)

# 计算从0秒到300秒的龙头坐标
for i in time_v:
    # 计算每秒龙头的极角
    head_theta_v = -np.sqrt((4 * np.pi * i) / p + (32 * np.pi) ** 2)
    # 计算每秒龙头的x坐标
    head_x_v = (p / (2*np.pi) * head_theta_v * np.cos(-head_theta_v))
    # 计算每秒龙头的y坐标
    head_y_v = (p / (2*np.pi) * head_theta_v * np.sin(-head_theta_v))
    # 计算每秒龙头的极径
    head_r_v = (p/2*np.pi)/head_theta_v
    # 将每秒龙头的平面直角坐标、极角和极径全部保存
    head_theta.append(head_theta_v)
    head_r.append(head_r_v)
    head_x.append(head_x_v)
    head_y.append(head_y_v)

# 画出龙头的运动轨迹
# plt.plot(head_x, head_y)
# plt.text(head_x[1], head_y[1], "A")
# plt.axis('equal')
# plt.show()


# 保存龙头的坐标值
for i in range(0, 301):
    print("%f\t%f", head_x[i], head_y[i])
col1 = 'X'
col2 = 'Y'
data = pd.DataFrame({col1: head_x, col2: head_y})
data.to_excel("./head.xlsx", sheet_name="sheet1", index=False)



# 定义龙头与第一节龙身的间距
l = 2.86
# 定义未知量
body_theta = sp.symbols('body_theta')
# 定义龙身1的极角
body1_theta = []
# 定义龙身1的x坐标
body1_x = []
# 定义龙身1的y坐标
body1_y = []


# 计算从0秒到300秒的龙身1坐标
for i in time_v:
    # 通过极坐标两点间距离公式定义方程
    equation = sympy.Eq((
        ((p / (2 * np.pi) * head_theta[i]) - p / (2 * np.pi) * body_theta) ** 2 +
        (head_theta[i] - body_theta) ** 2) ** 1 / 2, l)
    # 解方程
    v = sp.solve(equation, body_theta)
    # 保存龙身1极角的值
    body1_theta.append(v[1])
    # 计算龙身1
    # body1_theta[i]为sympy.solve()函数的返回值，数据类型并非float，而是此第三方库作者自定义的一个Float类
    body1_x_value = (p/(2*np.pi)*body1_theta[i] * np.cos(float(body1_theta[i])))
    body1_y_value = (p/(2*np.pi)*body1_theta[i] * np.sin(float(body1_theta[i])))
    body1_x.append(body1_x_value)
    body1_y.append(body1_y_value)


# body1_data = pd.DataFrame({col1: body1_x_value, col2: body1_y_value})
# body1_data.to_excel("body.xlsx", sheet_name="sheet1", index=False)

# 通过同样方法定义求龙身坐标的函数
# def body_addr(n, body_n_1, body_n):
#     # 定义未知量
#     body_theta = sp.symbols('body_theta')
#     # 定义龙身1的极角
#     bodyn_theta = []
#     # 定义龙身1的x坐标
#     bodyn_x = []
#     # 定义龙身1的y坐标
#     bodyn_y = []
#     for i in time_v:
#         # 通过极坐标两点间距离公式定义方程
#         equation = sympy.Eq((
#             ((p / (2 * np.pi) * body_addr()) - p / (2 * np.pi) * body_n) ** 2 +
#             (body_n_1[i] - body_n) ** 2) ** 1 / 2, l)
#         # 解方程
#         v = sp.solve(equation, body_theta)
#         # 保存龙身1极角的值
#         bodyn_theta.append(v[1])
#         # 计算龙身1
#         # bodyn_x_value = (p/(2*np.pi)*bodyn_theta[i] * np.cos(bodyn_theta[i]))
#         # bodyn_y_value = (p/(2*np.pi)*bodyn_theta[i] * np.sin(bodyn_theta[i]))
#         # bodyn_x.append(bodyn_x_value)
#         # bodyn_y.append(bodyn_y_value)
#         return bodyn_theta
#
# for i in range(1, 223):
#     body_theta(i, head_theta)


# 求龙头的速度
head_v_x = np.array(time_v)
head_v_y = np.array(head_r)
# 求导算出龙头的法线方向分速度
head_v_fa = np.gradient(head_v_y, head_v_x)
head_v = []
# 求从第0秒到300秒的龙头速度
for i in time_v:
    # 通过计算切线方向的分速度与法线方向的分速度求合速度
    head_v_v = np.sqrt(head_v_fa[i]**2 + 1**2)
    # 保存龙头的最终合速度
    head_v.append(head_v_v)


# 导出数据
head_v_data = pd.DataFrame(head_v)
head_v_data.to_excel("head_v.xlsx", sheet_name="sheet1", index=False)

# 通过同样方法定义求龙身速度的函数
def body_v(n, body_theta, body_r):
    body_v_x = np.array(time_v)
    body_v_y = np.array(body_r)
    body_v_fa = np.gradient(body_v_y, body_v_x)
    body_v = []
    for i in time_v:
        body_v_v = np.sqrt(body_v_fa[i]**2 + 1**2)
        body_v.append(body_v_v)
