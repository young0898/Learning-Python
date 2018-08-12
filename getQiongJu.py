import requests
import re
import os
import urllib
import time

def getUrls(start=10606, end=10778):
    pagegroup = []
    for i in range(start, end):
        eachUrl = ('http://www.fl5y.com/e/DownSys/DownSoft/?classid=36&id=%s&pathid=0' % i)
        pagegroup.append(eachUrl)
    return pagegroup

def getHtmlSource(url):
    '获取网页源码'
    html = requests.get(url)
    return html.text

def getInfo(str):
    pattern = re.compile('<a  href="(.*?)"  class="btn btn-success " download="(.*?)"  style="width:100%"><em class="icon-download-alt"></em> 电信下载</a></p>', re.S)
    return pattern.findall(str)

def saveFile(url, file_name, file_path='downFile'):
    try:
        if not os.path.exists(file_path):
            print('文件夹', file_path, '不存在，重新建立')
            #os.mkdir(file_path)
            os.makedirs(file_path)
        #获得文件后缀
        file_suffix = os.path.splitext(url)[1]
        #拼接文件名（包含路径）
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
        print('《%s》正在下载,请稍等！' % file_name)
        #下载文件，并保存到文件夹中
        urllib.request.urlretrieve(url, filename=filename)
        print('《%s》下载完毕' % file_name)
    except IOError as e:
        print('文件操作失败',e)
    except Exception as e:
        print('错误：',e)

def main():
    #url = 'http://dd.for1.net/qiongju/0062.mp3'
    urls = getUrls()
    for eachUrl in urls:
        html_str = getHtmlSource(eachUrl)
        results = getInfo(html_str)
        for each_result in results:
            url = each_result[0]
            filename = each_result[1]
            saveFile(url, filename, '琼剧1')
            time.sleep(10)

if __name__ == '__main__':
    main()