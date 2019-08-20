import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
data_file = "BeijingPM20100101_20151231.csv"

pm_bj = pd.read_csv(data_file)

#print(pm_bj.head(1))
#print(pm_bj.info())

#把分开的时间字符串通过periodIndex的方法转化为pandas的时间类型
period = pd.PeriodIndex(year=pm_bj["year"],month=pm_bj["month"],day=pm_bj["day"],hour=pm_bj["hour"],freq="H")

pm_bj["datetime"] = period
pm_bj.set_index("datetime",inplace=True)

pm_bj = pm_bj.resample("7D").mean()
#处理缺失数据(先将缺的去掉，画图看看)
data = pm_bj["PM_Dongsi"].dropna()


#画图
_x = data.index
_x = [i.strftime("%Y%m%d") for i in _x]
_y = data.values

plt.plot(range(len(_x)), _y)

plt.xticks(range(0,len(_x),10),list( _x)[::10],rotation=45)
plt.show()