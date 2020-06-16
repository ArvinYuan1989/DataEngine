import pandas as pd

car_complain = pd.read_csv('car_complain.csv',encoding='utf-8') #乱码问题
# car_complain = pd.DataFrame(result)
# print(type(result))
print(car_complain)
# car_complain.to_csv('1.csv',index=False)

#品牌投诉总数
# df_brand_count = car_complain.groupby('brand')['problem'].count()
# print(df_brand_count)

#车型投诉总数
# df_car_count = car_complain.groupby('car_model')['problem'].count()
# print(df_car_count)

#投诉最多的品牌车型
df_brand_count = car_complain.groupby('brand')['problem'].agg(['count'])
# df_car_count = car_complain.groupby('car_model')['problem'].count()
# print(type(df_brand_count))
print(df_brand_count)