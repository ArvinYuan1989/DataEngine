from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np


data = pd.read_csv('CarPrice_Assignment.csv')

# print(data.loc[0])
# print(data)

data_op = data.drop(columns= ['car_ID','CarName','enginelocation','enginelocation','enginetype'])

# print(data_op)
# print(index_list[0])
#
# LabelEncoder,将非数值转换为数值
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
columns_list = data_op.loc[0].index
for column in columns_list:
    data_op[column] = le.fit_transform(data_op[column])

# print(data_op)


# 规范化到 [0,1] 空间,计算平均值，不同列之间还需做好标准统一
min_max_scaler=preprocessing.MinMaxScaler()
data_op=min_max_scaler.fit_transform(data_op)
pd.DataFrame(data_op).to_csv('temp.csv', index=False)
print(data_op)


### 使用KMeans聚类
kmeans = KMeans(n_clusters=7)
kmeans.fit(data_op)
predict_y = kmeans.predict(data_op)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
# 将结果导出到CSV文件中
result.to_csv("customer_cluster_result.csv",index=False)

# K-Means 手肘法：统计不同K取值的误差平方和
import matplotlib.pyplot as plt
sse = []
for k in range(1, 50):
	# kmeans算法
	kmeans = KMeans(n_clusters=k)
	kmeans.fit(data_op)
	# 计算inertia簇内误差平方和
	sse.append(kmeans.inertia_)
x = range(1, 50)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()
