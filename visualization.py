import os
import sys
import pygal
import requests
import bs4 as sp
import pandas as pd
from matplotlib import pyplot as plt
import pygal

#数据源！！
url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-1.shtml'

#数据采集！！
condition = requests.get(url)
datasource = condition.text
# print(datasource)
# print(datasource.text)

#数据清洗！！
soup = sp.BeautifulSoup(datasource,'html.parser')
# print(soup)
tr_list = soup.find_all('tr')
th_list = soup.find_all('th')
td_list = soup.find_all('td')
# print(tr_list)
# print(type(tr_list)) #<class 'bs4.element.ResultSet'>
# for tr in tr_list:  #正则表达式搜索数据
# id = tr_list[0]
    # id,brand,model,type,desc,typical,datatime,status = tr_list[0]
for th in tr_list[0]:#遍历title
    id,brand,model,type,desc,typical,datatime,status = th_list[0].text,th_list[1].text,th_list[2].text,th_list[3].text,th_list[4].text,th_list[5].text,th_list[6].text,th_list[7].text

df = pd.DataFrame(columns= [id,brand,model,type,desc,typical,datatime,status])
# print(df)

#单个数据读取测试
# # for td in tr_list[3]:
#     # td_list = soup.find('td',tr_list[3])
# data_id, data_brand = td_list[8].text,td_list[9].text
# df.loc[0] = [data_id,data_brand]
#
# print(df)

#所有数据读取
for i in range(30):
        data_id, data_brand,data_model,data_type,data_desc,data_typical,data_datatime,data_status = td_list[8*i+0].text, td_list[8*i+1].text, td_list[8*i+2].text, td_list[8*i+3].text, td_list[8*i+4].text, td_list[8*i+5].text, td_list[8*i+6].text, td_list[8*i+7].text
        df.loc[i] = [data_id, data_brand,data_model,data_type,data_desc,data_typical,data_datatime,data_status]

print(df)

#数据分析！！

# df1 = df.groupby('投诉品牌')['典型问题']
df1 = df.groupby('投诉品牌')['典型问题'].agg(['count'])

#重新成为一个dataframe，可读取数据
df2 = df1.reset_index()
# df1 = df.groupby('投诉品牌')['典型问题'].reset_index().rename(columns= ['品牌','投诉'])
# df_brand_count = df1.sort_values(by='count')
# print(df2)

#数据保存！！

df.to_csv('visulization.csv',index=False,encoding='gbk')#excel乱码问题如何解决？需要 utf-8或gbk解码

#可视化！！

# 遍历groupby里的数据
# for name,data_count in df1:
#     print(name)
#     print(data_count)

# print(df2.iloc[0,0])

line_chart = pygal.Bar()
line_chart.title = '品牌投诉'
line_chart.x_labels = map(str, range(0, 2))
for i in range(17):
    line_chart.add(df2.iloc[i,0], df2.iloc[i,1])
line_chart.render_to_file('bar.svg')

# # pie_chart = pygal.Pie()
# # pie_chart.title = 'Browser usage in February 2012 (in %)'
# # pie_chart.add(df_brand_count[0], df_brand_count[1])
# # pie_chart.render()

