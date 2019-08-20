import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
data_file = "911.csv"
data_911 = pd.read_csv(data_file)

data_911["timeStamp"] = pd.to_datetime(data_911["timeStamp"])
data_911.set_index("timeStamp",inplace=True)
temp_list = data_911.resample("M").count()["title"]
print(temp_list)

#画图
_x = temp_list.index
_x = [i.strftime("%Y%m%d") for i in _x]
_y = temp_list.values

plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x,rotation=45)
plt.show()