import os
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

os.chdir(os.getcwd() + "\data")

data = pd.read_excel("234Gliuliang.xlsx")
data = data.set_index("date")
data.index = pd.to_datetime(data.index)
print(data.shape)
print(data.head(2))
print(data.tail(2))
data = data.dropna()
print(data.tail(2))


plt.figure(figsize=(10,5))  #设置画布大小

plt.plot(data, label="data")  #往添加数据
data1 = data.rolling(4).mean()
plt.plot(data1, label="rolling_mean")

diff = data.diff(1)
plt.plot(diff, color="#00ff00",label="diff")
plt.legend(loc="best")
plt.show()

