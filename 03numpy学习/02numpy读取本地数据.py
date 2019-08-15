import numpy as np

data1 = r"C:\Users\baiwang-123\Desktop\发票查询列表.csv"
t1 = np.loadtxt(data1,delimiter=",",dtype="int",unpack=True)
t2=t1.transpose()
t3=t1.T
'''print(t1)
print(t2)
print(t3)
'''
'''
print(t2[2])  #取第三行t2[2]
print(t2[2:])  #取第三行之后的每一行t2[2:]
print(t2[[2,4,5]])  #取不连续的多行。第3,5,6行t2[[2,4,5]]

print(t2[1,:])  #取列，第二行及其所有列
print(t2[2:,:])  #取列，第三行之后所有行及所有列
print(t2[[2,4,6],:])  #第3,11,4行及其所有列
'''
print(t2[:,0])
print(t2[:,2:])
print(t2[:,[0,2]])

print(t2[2,3])  #3行4列
print(type(t2[2,3]))

print(t2[2:4,1:3])

print(t2[[0,1],[3,4]])