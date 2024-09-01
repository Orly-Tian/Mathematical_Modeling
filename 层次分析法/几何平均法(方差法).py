import numpy as np


# 定义判断矩阵
A = np.array([[1, 2, 3, 5], [1/2, 1, 1/2, 2], [1/3, 2, 1, 2], [1/5, 1/2, 1/2, 1]])

# 获取A的行
n = A.shape[0]

# 将A中的每一行所有元素相乘得到一个列向量
# np.prod()可以计算一维数组所有元素的乘积
prod_A = np.prod(A, axis=1)

# 新列向量的每个分量开n次方
# np.power()函数对数组元素进行幂运算,
# 例如np.power(A, 3)即数组a内的每个元素ai都成为ai^3
prod_n_A = np.power(prod_A, 1/n)

# 归一化处理
re_prod_A = prod_n_A / np.sum(prod_n_A)

# 结果即权重
print(re_prod_A)
