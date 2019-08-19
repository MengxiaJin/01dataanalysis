import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
data_file = "stores.csv"

data_starbucks = pd.read_csv(data_file)

#获取美国，中国店铺数
data_grouped = data_starbucks.groupby(by="CountryCode")["Id"].count()
data_country=data_grouped.sort_values(ascending=False)[:10]
print("美国店铺数量",data_grouped["US"])
print("中国店铺数量",data_grouped["CN"])

_x = data_country.index
_y = data_country.values

plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)
plt.show()
#中国每个省的店铺数量
#data_starbucks = data_starbucks[data_starbucks["CountryCode"] == "CN"]


#data_grouped_city = data_starbucks.groupby(by=[data_starbucks["CountryCode"],data_starbucks["City"]])["Id"].count()
data_grouped_city = data_starbucks[data_starbucks["CountryCode"] == "CN"].groupby(by="City")["Id"].count()
data_city = data_grouped_city.sort_values(ascending=False)[:25]
print(data_city)
_x = data_city.index
_y = data_city.values

plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)
plt.show()