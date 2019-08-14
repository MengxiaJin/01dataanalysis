import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
x = range(11,31)

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y1,label="自己",color="orange",linestyle=":")
plt.plot(x,y2,label ="同桌",color="cyan",linestyle="--")
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels)
plt.yticks(range(0,9))
#绘制网格
plt.grid(alpha=0.8) #设置透明度

#添加图例
plt.legend(loc = "upper left")  #标的位置，默认是右上

plt.show()