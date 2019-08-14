import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

import random
a = [random.randint(20,35) for i in range(120)]
b = range(1,121,1)
#设置中文
plt.figure(figsize=(20,8),dpi=80)
plt.plot(b,a)
_x = list(b)[::3]
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels+= ["11点{}分".format(i) for i in range(60)]
plt.xticks(_x[::5],_xtick_labels,rotation=45)#旋转的度数

#添加描述信息

plt.xlabel("时间")
plt.ylabel("温度 单位(℃)")
plt.title("10点到12点每分钟的气温变化情况")
plt.show()