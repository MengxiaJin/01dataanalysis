import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
data_file = "911.csv"
data_911 = pd.read_csv(data_file)
#print(data_911.head(1))

#print(data_911.info())

#获取分类情况
temp_list = data_911["title"].str.split(":").tolist()
cate_list = list(set([i[0] for i in temp_list]))
print(temp_list)
print(cate_list)
#构造为0的数组
zeros_df = pd.DataFrame(np.zeros((data_911.shape[0],len(cate_list))),columns=cate_list)
print(zeros_df)
#赋值
#for cate in cate_list:
#    zeros_df[data_911["title"].str.contains(cate)] =1

for i in range(data_911.shape[0]):
    zeros_df.loc[i,temp_list[i][0]] = 1

sum_ret = zeros_df.sum(axis=0)
print(sum_ret)