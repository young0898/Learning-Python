import requests
import json
import sys

# 调用图灵机器人的api，采用爬虫的原理，根据聊天消息返回回复内容
def tuling(info):
    appkey = "e5ccc9c7c8834ec3b08940e290ff1559"
    url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
    result = requests.get(url)
    content = result.text
    data = json.loads(content)
    return data['text']

#实现os.system调用
#text = sys.argv[1]
#tuling_reply = tuling(text)
#print(tuling_reply)