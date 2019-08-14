import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]

b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

x_14 =list(range(len(a)))
x_15 = [i+0.2 for i in x_14]
x_16 = [i+0.2*2 for i in x_14]

plt.bar(x_16,b_16,width=0.2,label="9月16")
plt.bar(x_15,b_15,width=0.2,label="9月15")
plt.bar(x_14,b_14,width=0.2,label="9月14")

#设置x_15刻度
plt.xticks(x_15,a,rotation=45)

plt.legend()
plt.show()