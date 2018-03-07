import time
import pexpect

def telnet(hostIP, username, password, logfile, cmd):
    prompt = '< '
    enter = "\r\n"
    log = open(logfile, "w")
    child = pexpect.spawn('telnet ' + hostIP)
    child.logfile = log
    child.expect(["ENTER USERNAME <", pexpect.EOF, pexpect.TIMEOUT])
    child.sendline(username + enter)
    child.expect(["ENTER PASSWORD <", pexpect.EOF, pexpect.TIMEOUT])
    child.sendline(password + enter)
    for each in cmd:
        child.expect(prompt)
        child.sendline(each + enter)
    child.expect(prompt)
    child.sendline("ZZZZ;" + enter)
    log.close()
    child.close()

def main():
    server = {"HKGS1": "10.236.9.69",
              "HKGS2": "10.236.8.69",
              "HKGS3": "10.236.8.69"}

    date = time.strftime('%Y%m%d', time.localtime(time.time()))
    UserName = "ZHYZHY"
    PassWord = "Zy#123321"
    cmd = ["ZMVI;","ZAHO;"]

    logfile = "log_hkgs1.log"
    telnet(server["HKGS1"], UserName, PassWord, logfile, cmd)
'''
    for each in server:
        logfile = date + "_" + each + "_" + server[each] + ".log"
        print(logfile)
        telnet(each, server[each], UserName, PassWord, logfile)
'''

if __name__ == "__main__":
    main()