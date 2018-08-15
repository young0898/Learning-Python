import re
import requests
import time
import os
import openpyxl

def getZoneUrl(url, provinceNum, cityNum):
    link = re.sub('(\d+)_(\d+)_0_0_0_0\.html', '%d_%d_0_0_0_0.html' % (provinceNum, cityNum), url, re.S)
    return link

def getPageUrl(url, total_page):
    '组合url'
    pagegroup = []
    for i in range(1, total_page+1):
        #link = re.sub('898_898_(\d+)_0_0_0\.html', '898_898_%d_0_0_0.html' % i, url, re.S)
        link = re.sub('_(\d+)_0_0_0\.html', '_%d_0_0_0.html' % i, url, re.S)
        pagegroup.append(link)
    return pagegroup

def getHtmlSource(url):
    '获取网页源码'
    html = requests.get(url)
    return html.text

def getInfo(html, info):
    pattern = re.compile(info, re.S)
    return pattern.findall(html)

def openFile(fileDir="data", fileName="output.txt"):
    if not os.path.exists(fileDir):
        print(fileDir + "目录不存在，新建目录")
        os.mkdir(fileDir)
    os.chdir(os.path.abspath(fileDir)) #切换目录，将结果放在该目录下
    fp = open(fileName, "wb+") #结果保存在该文件中 'getPhoneNumFrom10086.txt'
    return fp

def getZoneNum(file_name):
    #os.chdir("data")
    #file_name = "全国地市区号表.xlsx"
    excel_file = openpyxl.load_workbook(file_name)
    excel_sheet1 = excel_file['Sheet1']  #根据表名获取
    data=[]
    for row in excel_sheet1.rows:
        data_row = []
        for cell in row:
            data_row.append(cell.value)
        data.append(data_row)
    excel_file.close()
    return data

def spider(url, province, city):
    data = []
    totalNum = getInfo(getHtmlSource(url), '<em class="marginRight20">第1/(\d+)页</em><em class="marginRight20">共(\d+)条</em>')  # 获取爬取的总页数和条数
    if totalNum:
        totalPageNum = int(totalNum[0][0])
        totalPhoneNum = int(totalNum[0][1])
        if (totalPhoneNum > 0):
            urls = getPageUrl(url, totalPageNum)
            for each_url in urls:
                html_str = getHtmlSource(each_url)
                results = getInfo(html_str, '<td class="name">(.*?)</td>.*?<td class="fontYaHei">.*?(\d+)</td>')
                for each_result in results:
                    line = province + ' ' + city + ' ' + each_result[0] + ' ' + each_result[1]
                    data.append(line)
                time.sleep(2)  # 延时2秒
    return totalPhoneNum, data

def main():
    initUrl = "https://shop.10086.cn/list/134_898_898_0_0_0_0.html"
    fp = openFile("data","getPhoneNumFrom10086.txt")
    zoneNum = getZoneNum("全国地市区号表.xlsx")
    for each in zoneNum:
        url = getZoneUrl(initUrl, each[1], each[3])
        print(url)
        totalPhoneNum, data = spider(url, each[0], each[2])
        for one in data:
            print(one)
            fp.write((one+'\n').encode('utf-8'))
        print(each[0]+" "+each[2]+"共计"+str(totalPhoneNum)+"个号码")
    fp.close

if __name__ == '__main__':
    main()