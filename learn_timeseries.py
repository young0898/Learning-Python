import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir(os.getcwd() + "\data")  #切换到data目录

def draw_ts(timeseries):
    timeseries.plot()
    plt.show()

data = pd.read_csv("demo1.csv")

data = data.set_index("date")
data.index = pd.to_datetime(data.index)
print("data_shape:",data.shape)
print(data.head())
#draw_ts(data['A'])


diff = data.diff(2)
diff = diff.dropna()
print("data_shape:",diff.shape)
print(diff.head())

td = diff.describe()
print(type(td))


#high = td['75%'] + 1.5 * (td['75%'] - td['25%'])
#low = td['25%'] - 1.5 * (td['75%'] - td['25%'])
#print high,low




