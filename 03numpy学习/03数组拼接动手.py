import numpy as np

t = np.array(range(10)).reshape(2,5).astype("float")

t[1,2:] = np.nan
#print(t.shape[1])

for i in range(t.shape[1]):  #遍历每一列
    temp_col = t[:,i]
    nan_num = np.count_nonzero(temp_col!=temp_col)
    if nan_num!=0:
        temp_not_nan_col =  temp_col[temp_col==temp_col]  #当前一列不为nan的array

        temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()  #选中当前为nan的位置，把值赋值为均值

print(t)