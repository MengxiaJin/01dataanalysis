import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
data_file = "books.csv"
data_books = pd.read_csv(data_file)
data_books = data_books[pd.notnull(data_books["original_publication_year"])]
data_year = data_books.groupby(by="original_publication_year")["title"].count()
print (data_year)
data_average_rating = data_books.groupby(by="original_publication_year")["average_rating"].mean()

print (data_average_rating)
#画图
_x = data_average_rating.index
_y = data_average_rating.values

plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)),_y)
plt.xticks(list(range(len(_x)))[::10],_x[::10])
plt.show()