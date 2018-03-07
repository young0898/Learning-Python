import re
import requests
import time
import os

def getUrls(url, total_page):
    '组合url'
    page_str = re.search('898_898_(.*?)_0_0_0_0_0\.html\?p=([0-9]+)', url, re.S)
    page = page_str.group(1)
    nowpage = int(page)
    pagegroup = []
    for i in range(nowpage, total_page + 1):
        link = re.sub('898_898_(.*?)_0_0_0_0_0\.html\?p=([0-9]+)', '898_898_%s_0_0_0_0_0.html?p=%s' % (i, i), url, re.S)
        pagegroup.append(link)
    return pagegroup

def getHtmlSource(url):
    '获取网页源码'
    html = requests.get(url)
    return html.text

def getInfo(str):
    pattern = re.compile('<td class="name">(.*?)</td>.*?<td class="fontYaHei">.*?(\d+)</td>', re.S)
    return pattern.findall(str)

def main():
    url = "http://shop.10086.cn/list/134_898_898_1_0_0_0_0_0.html?p=1"
    urls = getUrls(url,5) #需要爬取的页数
    if os.path.exists("data"):
        print("data目录存在")
    else:
        os.mkdir("data")
        print("data目录不存在，创建目录")
    os.chdir(os.path.abspath("data")) #切换目录，将结果放在该目录下
    fp = open('getPhoneNumFrom10086.txt', "wb+") #结果保存在该文件中
    count = 0
    for each_url in urls:
        html_str = getHtmlSource(each_url)
        results = getInfo(html_str)
        for each_result in results:
            print(each_result[0]+' 售价'+each_result[1]+'元')
            info = (each_result[0]+' 售价'+each_result[1]+'元\n').encode('utf-8')
            fp.write(info)
            count+=1
        time.sleep(2) #延时2秒
    print('共计'+str(count)+'个号码')
    fp.write(('共计'+str(count)+'个号码').encode('utf-8'))
    fp.close

if __name__ == '__main__':
    main()