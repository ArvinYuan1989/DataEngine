import pandas as pd

car_complain = pd.read_csv('car_complain.csv',encoding='utf-8') #乱码问题
# car_complain = pd.DataFrame(result)
# print(type(result))
# print(car_complain)
# car_complain.to_csv('1.csv',index=False)

#品牌投诉总数
df1 = car_complain.groupby('brand')['problem'].agg(['count'])
df_brand_count = df1.sort_values(by='count')
print(df_brand_count)

#车型投诉总数
df2 = car_complain.groupby('car_model')['problem'].agg(['count'])#agg 聚合
df_car_count = df2.sort_values(by='count')
print(df_car_count)


#投诉最多的品牌车型
df3 = car_complain.groupby(['brand','car_model'])['problem'].agg(['count'])
df = df3.sort_values(by='count')
print(df)
# df_optimize = car_complain.drop(columns = ['id','type','desc','datetime','status'])
# df_count = df_optimize.groupby('problem').count()
# # df_brand_count = car_complain.groupby('brand')['problem'].agg(['count'])
# # df_car_count = car_complain.groupby('car_model')['problem'].count()
# # print(type(df_brand_count))
# # print(df_brand_count)
# # print(df_optimize)
# print(df_count)