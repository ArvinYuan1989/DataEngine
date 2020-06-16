import pandas as pd
svw_score = {
    '姓名':['张飞','关羽','刘备','典韦','许褚'],
    '语文':[68,95,98,90,80],
    '数学':[65,76,86,88,90],
    '英语':[30,98,88,77,90],
}
data1 = pd.DataFrame(svw_score)
# data2 = pd.DataFrame(svw_score,columns = ['姓名','语文','数学','英语'])
print(data1)
# print(data2)
avergae = data1.mean()

score_min = data1.drop(columns='姓名').min() #如何去除关羽
score_max = data1.drop(columns='姓名').max()
score_var = data1.var()
score_std = data1.std()

#总成绩排序
data1['all'] = data1.sum(axis = 1)
data1_sort = data1.sort_values(by= 'all')


print('aver:\n',avergae)
print(score_min)
print(score_max)
print(score_var)
print(score_std)
print(data1_sort)