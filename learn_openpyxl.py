import os
import openpyxl

os.chdir("data")
file_name = "timeseries.xlsx"
excel_file = openpyxl.load_workbook(file_name)
print(excel_file.sheetnames)      #获取所有表名
excel_sheet1 = excel_file.active      #获取活动表，即打开时显示的表
excel_sheet2 = excel_file['Sheet2']  #根据表名获取
print(excel_sheet2.title)
#A1 = excel_sheet1["A2"].value
A4 = excel_sheet1['A4']
print(A4)
excel_sheet1['C1'] = 1
print(f'({A4.column}, {A4.row}) is {A4.value}')  # 返回的数字就是int型
# 因为按行，所以返回A1, B1, C1这样的顺序
# A1, A2, A3这样的顺序
for column in excel_sheet1.columns:
    for cell in column:
        print(cell.value)

excel_sheet2['A1'] = 21


excel_file.save(file_name)
excel_file.close()
