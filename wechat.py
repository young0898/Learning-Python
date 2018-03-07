from itchat.content import *
import itchat
from tulingAPI import tuling

model = {1:"陪聊", 2:"勿扰", 3:"告警", 0:"退出"}
usageMsg = "使用方法：\n1.陪聊模式\n2.勿扰模式\n3.告警模式"
replyMsg = {2:"[消息助手]：\n您好！我的主人正在休息，未能及时回复，请谅解。"}

#返回UserName，参数：微信号或昵称
def getUserName(name):
    user = itchat.search_friends(name=name)
    return user[0]['UserName']

@itchat.msg_register(TEXT)
def text_reply(msg):
    global run_model
    print("%s" % (msg.text))
    message = msg.text    #接收文本消息
    FromUserName = msg['FromUserName']  # 消息发送方
    ToUserName = msg['ToUserName']      # 消息接收方

    if ToUserName == "filehelper":
        if message == model[1] or message == '1':
            run_model = 1
            itchat.send(model[run_model]+"模式已开启，回复0退出", "filehelper")
        elif message == model[2] or message == '2':
            run_model = 2
            itchat.send(model[run_model]+"模式已开启，回复0退出", "filehelper")
        elif message == model[3] or message == '3':
            run_model = 3
            itchat.send(model[run_model]+"模式已开启，回复0退出", "filehelper")
        elif run_model != 0 and (message == model[0] or message == '0'):
            itchat.send(model[run_model]+"模式已退出", "filehelper")
            run_model = 0
        elif run_model == 0:
            itchat.send(usageMsg, "filehelper")
        else:
            itchat.send("正处于"+model[run_model]+"模式，回复0退出", "filehelper")
    elif run_model == 1:
        itchat.send(tuling(message), FromUserName)
    elif run_model == 2:
        itchat.send(replyMsg[run_model], FromUserName)

run_model = 0 #无模式
itchat.auto_login(hotReload=True,enableCmdQR=-1)  #扫描二维码登录网页版微信
#itchat.auto_login(hotReload=True)  #扫描二维码登录网页版微信
itchat.send('您正在使用微信机器人', getUserName('young'))
itchat.run() # 运行并保持网页版在线状态