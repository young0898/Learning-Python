import os
import pandas as pd
import matplotlib.pylab as plt

os.chdir(os.getcwd() + "\data")

data = pd.read_excel("234Gliuliang.xlsx")
data = data.set_index("date")
data.index = pd.to_datetime(data.index)
print(data.shape)
print(data.head(3))
print(data.tail(3))
data = data.dropna()  #删除空格行
print(data.tail(3))


plt.figure(figsize=(10,5), dpi=100)  #设置画布大小

plt.plot(data, color="#0000ff", label="4G")  #往添加数据
plt.legend(loc="best")

data_mean = data.rolling(4).mean()
plt.plot(data_mean, color="#ff0000", label="4G_rolling_mean")
plt.legend(loc="best")

diff1 = data_mean.diff(1).dropna()
print(diff1.head(3))
plt.plot(diff1, color="#00ff00",label="4G_rolling_mean_diff1")
plt.legend(loc="best")
plt.show()

