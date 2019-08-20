import pandas as pd
import numpy as np
import matplotlib.pyplot as plt






plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
data_file = "911.csv"
data_911 = pd.read_csv(data_file)
data_911["timeStamp"] = pd.to_datetime(data_911["timeStamp"])

temp_list_title = data_911["title"].str.split(":").tolist()
cate_list = list([i[0] for i in temp_list_title])
data_911["cate"]=pd.DataFrame(np.array(cate_list).reshape((data_911.shape[0],1)))
data_911.set_index("timeStamp",inplace=True)
print(data_911.head(1))
plt.figure(figsize=(20,8),dpi=80)
#分组

for group_name,group_data in data_911.groupby(by="cate"):
    count_by_month = group_data.resample("M").count()["title"]
    # 画图
    _x = count_by_month.index
    _x = [i.strftime("%Y%m%d") for i in _x]
    _y = count_by_month.values
    # print(_x)

    plt.plot(range(len(_x)), _y, label=group_name)


plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc='best')
plt.show()






