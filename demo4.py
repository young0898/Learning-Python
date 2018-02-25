import os
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import statsmodels.api as sm
from test_stationarity import *

os.chdir(os.getcwd() + "\data")
print("当前目录：" + os.getcwd())

data = pd.read_excel("234Gliuliang.xlsx")
#data = data.set_index("date")
#data.index = pd.to_datetime(data.index)
print(data.shape)
print(data.dtypes)
print(data.head(2))
print(data.index)
print(data.columns)
print(data[:1])
print(data[2:3]["date"])
print(data["date"][2:3])
print(data.values)
print(data.describe())
print(data[data["4G"]>600000])
#print(data.sort_values(by="4G",ascending=False))
#data1 = data["4G"].diff(1)
#data1 = pd.Series(data1)
#data1 = data1.dropna()
#print(data1.shape)
print(data.dropna())

plt.figure(figsize=(13,6), dpi=100)
plt.plot(data, label="data")
data1 = data.rolling(4).mean()
plt.plot(data1, label="rolling_mean")
diff = data.diff(1)
plt.plot(diff, color="#00ff00",label="diff")
plt.legend(loc="best")
plt.show()

