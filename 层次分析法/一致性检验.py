import numpy as np


# 定义矩阵A，np.array()是NumPy库中的一个函数，用于创建数组。它将输入的对象(如列表、元组、数组等)转换为Numpy数组
A = np.array([[1, 2, 3, 5], [1/2, 1, 1/2, 2], [1/3, 2, 1, 2], [1/5, 1/2, 1/2, 1]])

# shape是获取形状信息，参数为0为获取A的行，参数为1则是获取A的列
n = A.shape[0]

# 求出最大特征值以及对应的特征向量，np.linalg.eig()用于计算方阵的特征值与特征向量
# eig_val是特征值，eig_vec是特征向量
eig_val, eig_vec = np.linalg.eig(A)

# 求最大特征值
max_eig = max(eig_val)

CI = (max_eig-n) / (n-1)
RI = [0, 0.0001, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]

CR = CI / RI[n-1]

print('一致性指标CI = ', CI)
print('一致性比例CR = ', CR)

if CR < 0.10:
    print("因为CR < 0.10,所以该判断矩阵A的一致性可以接受!")
else:
    print("此时CR >= 0.10,所以该判断矩阵A需要进行修改使其通过一致性判断!")

