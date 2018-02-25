import pandas
import numpy
import matplotlib.pyplot as plt
import statsmodels.api as sm

data1 = [10930, 10318, 10595, 10972, 7706,
        6756, 9092, 10551, 9722, 10913,
        11151, 8186, 6422, 6337, 11649,
        11652, 10310, 12043, 7937, 6476,
        9662, 9570, 9981, 9331, 9449,
        6773, 6304, 9355, 10477, 10148,
        10395, 11261, 8713, 7299, 10424,
        10795, 11069, 11602, 11427, 9095,
        7707, 10767, 12136, 12812, 12006,
        12528, 10329, 7818, 11719, 11683,
        12603, 11495, 13670, 11337, 10232,
        13261, 13230, 15535, 16837, 19598,
        14823, 11622, 19391, 18177, 19994,
        14723, 15694, 13248, 9543, 12872,
        13101, 15053, 12619, 13749, 10228,
        9725, 14729, 12518, 14564, 15085,
        14722, 11999, 9390, 13481, 14795,
        15845, 15271, 14686, 11054, 10395
        ]

data = pandas.Series(data1)
data.index = pandas.Index(sm.tsa.datetools.dates_from_range('1926', '2015'))
print(data.head(3))

data.plot(figsize=(10, 5), label="data_orogin")
plt.legend(loc="best")

#第一步：确定d，根据diff1和diff2的图像看，两种差不多，故选择d=1
diff_1 = data.diff(1).dropna()
diff_1.plot(figsize=(10,5), label="data_diff1")
plt.legend(loc="best")

diff_2 = data.diff(2).dropna()
diff_2.plot(figsize=(10,5), label="data_diff2")
plt.legend(loc="best")
plt.show()

#d=1
arma_mode = sm.tsa.ARMA(diff_1, (8, 0)).fit()
arma_predict = arma_mode.predict('2015', '2050', dynamic=True)

fig, ax = plt.subplots(figsize=(10,5))
ax = diff_1.ix['1926':].plot(ax=ax)
arma_predict.plot(ax=ax)
plt.show()

#第三步、将预测的差分值还原为
lastValue = data[len(data)-2]
#print(lastValue)
#print("+++++++++")
for p in arma_predict:
    lastValue = lastValue + p
    #print(p)
    print(lastValue)
    data1.append(lastValue)

