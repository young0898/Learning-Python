import os
import re
import openpyxl

os.chdir(os.path.abspath("data"))
fp = open('HKGS13_userid.log',"rb")
str = fp.read()
print(type(str))
fp.seek(0,0) #将指针放到文件开头
str = fp.read().decode('utf-8')
print(type(str))

file_name = "getUserID.xlsx"
excel_file = openpyxl.load_workbook(file_name)
excel_sheet1 = excel_file.active      #获取活动表，即打开时显示的表

#更好的写法
#pattern = re.compile(r'NSENAME-\s*(.*?)[C,\s].*?PGI')
#results = pattern.findall(str)

results = re.findall(r'USER ID:  (.*?)\s*\nPROFILE NAME: (.*?)\s*\n.*? M=.*?(\d+)\s',str,re.S)

i = 1
excel_sheet1['A{0}'.format(i)] = "USER ID"
excel_sheet1['B{0}'.format(i)] = "PROFILE NAME"
excel_sheet1['C{0}'.format(i)] = "M"
for each in results:
    i += 1
    print('{0} {1} {2}'.format(each[0],each[1],each[2]))
    excel_sheet1['A{0}'.format(i)] = each[0]
    excel_sheet1['B{0}'.format(i)] = each[1]
    excel_sheet1['C{0}'.format(i)] = each[2]

excel_file.save(file_name)
excel_file.close()
fp.close()