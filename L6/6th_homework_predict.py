from statsmodels.tsa.arima_model import ARMA
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from itertools import product
import calendar
import matplotlib.pyplot as plt


# 读取数据,以天为单位聚合
df = pd.read_csv('train.csv')
df.Datetime = pd.to_datetime(df.Datetime)
# df['Datetime'] = pd.to_datetime(df['Datetime'])
df.index = df.Datetime

# 不设定范围，则默认从Month的第一天开始
df_day = df['2012-08-25':'2014-09-25'].resample('D').sum()
df_day = df_day[['Count']]
# print(df_day)


# 设置参数范围
ps = range(0, 3)
qs = range(0, 3)
parameters = product(ps, qs)
parameters_list = list(parameters)
# 寻找最优ARMA模型参数，即best_aic最小
results = []
best_aic = float("inf") # 正无穷
for param in parameters_list:
    try:
        model = ARMA(df_day[['Count']],order=(param[0], param[1])).fit()
    except ValueError:
        print('参数错误:', param)
        continue
    aic = model.aic
    if aic < best_aic:
        best_model = model
        best_aic = aic
        best_param = param
    results.append([param, model.aic])
# 输出最优模型
print('最优模型: ', best_model.summary())

# 设置future_month，需要预测的时间date_list
df_month2 = df_day[['Count']]
future_month = 7
last_month = pd.to_datetime(df_month2.index[len(df_month2)-1])
#print(last_month)
date_list = []
for i in range(future_month):
    # 计算下个月有多少天
    year = last_month.year
    month = last_month.month
    if month == 12:
        month = 1
        year = year+1
    else:
        month = month + 1
    next_month_days = calendar.monthrange(year, month)[1]
    #print(next_month_days)
    last_month = last_month + timedelta(days=next_month_days)
    date_list.append(last_month)
print('date_list=', date_list)

# 添加未来要预测的7个月
future = pd.DataFrame(index=date_list, columns= ['Count'])
df_month2 = pd.concat([df_month2, future])
df_month2['forecast'] = best_model.predict(start=0, end=len(df_month2))
# 第一个元素不正确，设置为NaN
df_month2['forecast'][0] = np.NaN
print(df_month2)

# 预测结果显示
plt.rcParams['font.sans-serif']=['SimHei']#黑体
plt.figure(figsize=(30,7))
df_month2.Count.plot(label='实际')
df_month2.forecast.plot(color='r', ls='--', label='预测')
plt.legend()
plt.title('流量预测')
plt.xlabel('时间')
plt.ylabel('流量')
plt.show()