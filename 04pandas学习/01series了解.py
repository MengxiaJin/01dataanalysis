import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\baiwang-123\Desktop\IMDB-Movie-Data.csv")
#print(df.head(1))

#print(df["Genre"])


temp_list = df["Genre"].str.split(",").tolist()
genre_list = list(set(i for j in temp_list for i in j))
#print(genre_list)
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)


for i in range(df.shape[0]):
    zeros_df.loc[i,temp_list[i]] = 1

#print(zeros_df)

genre_count = zeros_df.sum(axis=0)


genre_count=genre_count.sort_values()
print(genre_count)
_x = genre_count.index
_y = genre_count.values

plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)

plt.show()