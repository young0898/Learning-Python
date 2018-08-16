import requests
import re

class spider:
    def __init__(self):
        self.loginUrl = 'https://www.falcomm.cn:8081/falcomm/frontend/web/index.php?r=site%2Flogin'
        self.postUrl = 'https://www.falcomm.cn:8081/falcomm/frontend/web/index.php?r=site%2Flogin'
        self.getUrl = 'https://www.falcomm.cn:8081/falcomm/frontend/web/index.php?r=team-weekly%2Fmine'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'www.falcomm.cn:8081'
        }

    def login(self, username, password):
        req = requests.get(self.loginUrl,headers = self.headers)
        self._csrf = re.findall('name=\"_csrf\" value=\"(.*?)\"',req.text,re.S)[0]
        #print(self._csrf)

        post_data = {
            '_csrf' : self._csrf,
            'LoginForm[username]' : username,
            'LoginForm[password]' : password,
            'login-button' : None
        }
        respon_login = requests.post(self.postUrl, data=post_data, headers=self.headers)
        self.cookies = respon_login.cookies
        #print(respon_login)
        #print(self.cookies)

    def getInfo(self):
        respon_index = requests.get(self.getUrl, cookies=self.cookies, headers=self.headers)
        #print(respon_index.text)
        results = re.findall('<td width="10%">张阳</td><td>(\d+).*?normal;">(.*?)</td>',respon_index.text,re.S)
        for each in results:
            print(each[0])
            print(each[1])

if __name__ == '__main__':
    falcomm = spider()
    falcomm.login('zhangyang','18389308036')
    falcomm.getInfo()