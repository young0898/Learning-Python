#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

def draw_ts(timeseries):
    timeseries.plot()
    plt.show()

data = pd.read_csv("demo1.csv")
#print data.shape
#print data.head()

data = data.set_index("No")
draw_ts(data['A'])


diff = data.diff().dropna()
td = diff.describe()
print td['25%']

#high = td['75%'] + 1.5 * (td['75%'] - td['25%'])
#low = td['25%'] - 1.5 * (td['75%'] - td['25%'])
#print high,low




