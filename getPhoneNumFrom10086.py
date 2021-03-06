import re
import requests
import time
import os
import openpyxl

def getZoneUrl(url, provinceNum, cityNum):
    link = re.sub('134_(\d+)_(\d+)_', '134_%d_%d_' % (provinceNum, cityNum), url, re.S)
    return link

def getPageUrl(url, total_page, provinceNum, cityNum):
    '组合url'
    pagegroup = []
    for i in range(1, total_page+1):
        #link = re.sub('898_898_(\d+)_0_0_0\.html', '898_898_%d_0_0_0.html' % i, url, re.S)
        link = re.sub('134_(\d+)_(\d+)_(\d+)_', '134_%d_%d_%d_' % (provinceNum, cityNum, i), url, re.S)
        pagegroup.append(link)
    return pagegroup

def getHtmlSource(url):
    '获取网页源码'
    html = requests.get(url)
    return html.text

def getInfo(html, info):
    pattern = re.compile(info, re.S)
    return pattern.findall(html)

def openFile(fileDir="output", fileName="output.txt"):
    if not os.path.exists(fileDir):
        print(fileDir + "目录不存在，新建目录")
        os.mkdir(fileDir)
    os.chdir(os.path.abspath(fileDir)) #切换目录，将结果放在该目录下
    fp = open(fileName, "wb+") #结果保存在该文件中
    os.chdir(os.path.abspath(".."))  # os.path.abspath返回绝对路径
    return fp

def getZoneNum(file_name, sheet_name):
    os.chdir(os.path.abspath("input"))  # os.path.abspath返回绝对路径
    excel_file = openpyxl.load_workbook(file_name)
    excel_sheet1 = excel_file[sheet_name]  #根据表名获取
    data=[]
    for row in excel_sheet1.rows:
        data_row = []
        for cell in row:
            data_row.append(cell.value)
        data.append(data_row)
    excel_file.close()
    os.chdir(os.path.abspath(".."))  # os.path.abspath返回绝对路径
    return data

def spider(url, zoneData):
    data = []
    totalPhoneNum = 0
    totalNum = getInfo(getHtmlSource(url), '<em class="marginRight20">第1/(\d+)页</em><em class="marginRight20">共(\d+)条</em>')  # 获取爬取的总页数和条数
    if totalNum:
        totalPageNum = int(totalNum[0][0])
        totalPhoneNum = int(totalNum[0][1])
        if (totalPhoneNum > 0):
            urls = getPageUrl(url, totalPageNum, zoneData[1], zoneData[3])
            for each_url in urls:
                print(each_url)
                html_str = getHtmlSource(each_url)
                results = getInfo(html_str, '<td class="name">(.*?)</td>.*?<td class="fontYaHei">.*?(\d+)</td>.*?<td><a href="(.*?)" target.*?>立即购买</a></td>')
                for each_result in results:
                    line = zoneData[0]+' '+zoneData[2]+' '+each_result[0]+' '+each_result[1]+' '+each_result[2]
                    data.append(line)
                time.sleep(2)  # 延时2秒
    return totalPhoneNum, data

def main():
    initUrl = ["https://shop.10086.cn/list/134_898_898_0_0_0_0_0_0.html",  #全部
               "https://shop.10086.cn/list/134_898_898_0_0_0_0_1_0.html",  #尾号AABB
               "https://shop.10086.cn/list/134_898_898_0_0_0_0_2_0.html",  #尾号AAAB
               "https://shop.10086.cn/list/134_898_898_0_0_0_0_3_0.html",  #尾号ABBA
               "https://shop.10086.cn/list/134_898_898_0_0_0_0_4_0.html",  #尾号ABAB
               "https://shop.10086.cn/list/134_898_898_0_0_0_0_5_0.html",  #尾号AAAA
               "https://shop.10086.cn/list/134_898_898_0_0_0_0_6_0.html",  #尾号ABCD
               "https://shop.10086.cn/list/134_898_898_0_0_0_0_7_0.html",  #尾号ABAC
    ]
    zoneNum = getZoneNum("AllCityZoneList.xlsx", 'Sheet2')
    filename = "phoneNum_" + time.strftime("%Y%m%d%H%M%S") + ".txt"
    fp = openFile("output", filename)
    for i in range(1,8):
        for each in zoneNum:
            zoneUrl = getZoneUrl(initUrl[i], each[1], each[3])
            print(zoneUrl)
            totalPhoneNum, data = spider(zoneUrl, each)
            for one in data:
                print(one)
                fp.write((one+'\n').encode('utf-8'))
            print(each[0]+" "+each[2]+"共计"+str(totalPhoneNum)+"个号码")
            time.sleep(2)  # 延时2秒
    fp.close

if __name__ == '__main__':
    main()