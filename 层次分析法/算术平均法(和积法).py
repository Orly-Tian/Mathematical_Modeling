import numpy as np


# 定义判断矩阵
A = np.array([[1, 2, 3, 5], [1/2, 1, 1/2, 2], [1/3, 2, 1, 2], [1/5, 1/2, 1/2, 1]])

# 计算每列的和
# np.sum()可以计算一维数组中所有元素的和,参数axis=0则对列求和,axis=1则对行求和
Asum = np.sum(A, axis=0)

# 获取A的行
n = A.shape[0]

# 归一化
stand_A = A / Asum

# 各列相加到同一行
Asums = np.sum(stand_A, axis=1)

# 计算权重向量
weight = Asums / n
print(weight)

