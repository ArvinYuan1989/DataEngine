import requests
import bs4 as sp
import pandas as pd
import re

#数据源！！
url = 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8'

#数据采集！！
datasource = requests.get(url)

#数据清洗！！
soup = sp.BeautifulSoup(datasource.text,'html.parser')#读取html的文本数据，bs从HTML或XML文件中提取数据
item_list = soup.find('div',class_ ='search-result-list')#为什么不能遍历到下一层item？<class 'bs4.element.Tag'>
# print(type(item_list))
# print(item_list.text)

a_list = item_list.find_all('a')
# print(type(a_list))#<class 'bs4.element.ResultSet'>，结果类型没有部分句柄
# print(a_list)
# print(len(a_list))

pd_list = pd.DataFrame(columns=['名称','最低价格','最高价格','产品图片链接'])

for i in range(len(a_list)):
    p_list = a_list[i].find_all('p')#两个P，遍历得到名称
    pattern = re.compile('[1-9]\d*.\d*|0.\d*[1-9]\d*')#正则，找到两个价格放入list
    price = pattern.findall(p_list[1].text)
    if price == []:
        pd_list.loc[i] = [p_list[0].text, p_list[1].text, p_list[1].text, 'http:' +a_list[i].img['src']]
    else:
        pd_list.loc[i] = [p_list[0].text, price[0] + '万', price[1] + '万', 'http:' + a_list[i].img['src']]


#导出
pd_list.to_csv('Project A.csv',encoding='gbk')


