'''
import pandas as pd
#import numpy as np
##data = pd.Series(np.arange(10,20,2))  #不指定index，默认
#data = pd.Series(np.arange(10,20,2),index=np.arange(1,6))  #指定index
#data = pd.Series([4,5,6,7]) #不指定index，默认从0开始
#data = pd.Series([4,5,6,7],index=[1,2,3,4])  #指定index
data = pd.Series({"Python":1,"Java":2,"C++":3,"C":4})
print("形状:",data.shape)  #打印数据形状shape
print("类型:",data.dtype)  #打印数据类型dtype
print("维数：",data.ndim)
print("打印所有数据：\n",data)
print("打印序号2的数据：",data[2]) #序号默认从0开始，序号2对应"Java":2
print("打印序号Java的数据：",data["Java"])
'''

import os
import pandas as pd
import numpy as np

os.chdir(os.getcwd()+"\data")
print("当前目录："+os.getcwd())

data = pd.read_excel("234Gliuliang.xlsx") #读取数据
#data = data.set_index("date")  #设置date列为序号
#data.index = pd.to_datetime(data.index)
print(data.shape)  #数据形状
print(data.dtypes)  #数据类型
print(data.head(3))  #打印前3行数据
print(data.tail(3))  #打印后3行数据
print(data.index)  #数据序号
print(data.columns)  #数据列名
print(data[:1])  #打印序号0行数据
print(data[2:3]["date"])  #打印序号2行，date列的数据
print(data["date"][2:3])  #打印序号2行，date列的数据
print(data.values) #打印数据
print(data.describe())  #数据描述信息
print(data["4G"].mean()) #打印4G的平均值
print(data[data["4G"]>600000])  #打印4G大于600000的行数据
#print(data.sort_values(by="4G",ascending=False))  #根据4G列的排序，False降序，True升序

print(data.dropna()) # 删除存在缺失值的样本
print(data.head())
data.columns = ['date','4G(GB)','5G(GB)']
data = data.set_index('date')
print(data.head())
data.to_csv("new2.csv")




