import numpy as np


# 定义判断矩阵
A = np.array([[1, 2, 3, 5], [1/2, 1, 1/2, 2], [1/3, 2, 1, 2], [1/5, 1/2, 1/2, 1]])

# 获取A的行
n = A.shape[0]

# 求出特征值和特征向量
eig_values, eig_vectors = np.linalg.eig(A)

# 找出最大特征值的索引,np.argmax()用于返回数组中最大值的索引
max_index = np.argmax(eig_values)

# 找出对应的特征向量
max_vector = eig_vectors[:, max_index]

# 对特征向量进行归一化处理,得到权重
weight = max_vector / np.sum(max_vector)
print(weight)
