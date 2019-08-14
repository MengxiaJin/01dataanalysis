import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
x = range(1,32)
y=range(51,82)
plt.figure(figsize=(20,8),dpi=80)

#使用scatter方法绘制散点图
plt.scatter(x,a,label="3月份")
plt.scatter(y,b,label="10月份")

#调整x轴的刻度

_x = list(x)+list(y)
_xtick_labels = ["3月{}日".format(i) for i in x]
_xtick_labels +=["10月{}日".format(i) for i in x]
plt.xticks(_x,_xtick_labels,rotation=45)

#绘制网格
plt.grid(alpha=0.8) #设置透明度

plt.legend()

plt.show()
