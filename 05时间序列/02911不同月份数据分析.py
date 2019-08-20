import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
data_file = "911.csv"
data_911 = pd.read_csv(data_file)
print(data_911.head(1))

temp_list = data_911["timeStamp"].str[:7]
temp_list_title = data_911["title"].str.split(":").tolist()
cate_list = list([i[0] for i in temp_list_title])
data_911["timeStamp_year_mounth"]=temp_list
data_911["cate"]=cate_list
print(cate_list)
timeStamp_year_mounth=data_911.groupby(by=['timeStamp_year_mounth','cate'])["title"].count()
print(timeStamp_year_mounth)