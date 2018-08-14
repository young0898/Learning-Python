import re
import requests
import time
import os

def getUrls(url, total_page):
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

def main():
    fp = openFile("data","getPhoneNumFrom10086.txt")
    url = "https://shop.10086.cn/list/134_898_898_0_0_0_0.html"
    totalNum = getInfo(getHtmlSource(url), '<em class="marginRight20">第1/(\d+)页</em><em class="marginRight20">共(\d+)条</em>') #获取爬取的总页数和条数
    totalPageNum = int(totalNum[0][0])
    totalPhoneNum = int(totalNum[0][1])
    if(totalPhoneNum > 0):
        urls = getUrls(url, totalPageNum)
        for each_url in urls:
            html_str = getHtmlSource(each_url)
            results = getInfo(html_str, '<td class="name">(.*?)</td>.*?<td class="fontYaHei">.*?(\d+)</td>')
            for each_result in results:
                print(each_result[0]+' 售价'+each_result[1]+'元')
                info = (each_result[0]+' 售价'+each_result[1]+'元\n').encode('utf-8')
                fp.write(info)
            time.sleep(2) #延时2秒
    print('共计'+str(totalPhoneNum)+'个号码')
    fp.write(('共计'+str(totalPhoneNum)+'个号码').encode('utf-8'))
    fp.close

if __name__ == '__main__':
    main()