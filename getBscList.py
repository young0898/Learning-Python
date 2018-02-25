import os
import re

os.chdir(os.path.abspath("data"))
fp = open('2018-01-22_HKMME04BNK',"rb")
str = fp.read()
print(type(str))
fp.seek(0,0) #将指针放到文件开头

str = fp.read().decode('utf-8')
print(type(str))
#更好的写法
#pattern = re.compile(r'NSENAME-\s*(.*?)[C,\s].*?PGI')
#results = pattern.findall(str)

results = re.findall('NSENAME-\s*(.*?)[C,\s].*?PGI', str)
output = []
for each in results:
    if each not in output:
        output.append(each)
        print(each)
print(output)