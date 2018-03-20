import time
import pexpect
import os

os.chdir(os.getcwd()+"/logfile_mss") #for linux

UserName = "ZHYZHY"
PassWord = "Zy#123321"
cmd_for_HKGS1_2_4 = ["ZUSI;",
                "ZAHO;",
                "ZDOI;",
                "ZDOI::M;",
                "ZCEL:ST=NO-WO;",
                "ZIFO:CHU,0:GSMCHA:;",
                "ZIFO:CHU,1:GSMCHA:;",
                "ZIFO:CHU,2:GSMCHA:;",
                "ZIFO:CHU,3:GSMCHA:;",
                "ZOYV:SGSAP;",
                "ZOYI::A;",
                "ZIFO:OMU:MEAXML;",
                "ZISI:,OMU:WDU;",
                "ZIWX::::%,%,;",
                "ZDCD;",
                "ZZZZ;"]
cmd_for_HKGS3_11 = ["ZUSI;",
                "ZAHO;",
                "ZDOI;",
                "ZDOI::M;",
                "ZCEL:ST=NO-WO;",
                "ZIFO:CHU,0:GSMCHA:;",
                "ZIFO:CHU,1:GSMCHA:;",
                "ZIFO:CHU,2:GSMCHA:;",
                "ZOYV:SGSAP;",
                "ZOYI::A;",
                "ZIFO:OMU:MEAXML;",
                "ZISI:,OMU:WDU;",
                "ZIWX::::%,%,;",
                "ZDCD;",
                "ZZZZ;"]
cmd_for_HKGS6_7_8_12_13_14 = ["ZUSI;",
                "ZAHO;",
                "ZDOI;",
                "ZDOI::M;",
                "ZCEL:ST=NO-WO;",
                "ZIFO:CHU,0:GSMCHA:;",
                "ZIFO:CHU,1:GSMCHA:;",
                "ZOYV:SGSAP;",
                "ZOYI::A;",
                "ZIFO:OMU:MEAXML;",
                "ZISI:,OMU:WDU;",
                "ZIWX::::%,%,;",
                "ZDCD;",
                "ZZZZ;"]
cmd_for_HKGS17 = ["ZUSI;",
               "ZAHO;",
               "ZDOI;",
               "ZDOI::M;",
               "ZCEL:ST=NO-WO;",
               "ZIFO:CHU:GSMCHA:;",
               "ZOYV:SGSAP;",
               "ZOYI::A;",
               "ZIFO:OMU:MEAXML;",
               "ZISI:,OMU:WDU;",
               "ZIWX::::%,%,;",
               "ZDCD;",
               "ZZZZ;"]
servers = {"HKGS1": "10.236.9.69",
          "HKGS2": "10.236.8.69",
          "HKGS3": "10.236.8.85",
          "HKGS4": "10.236.8.101",
          "HKGS6": "10.236.6.101",
          "HKGS7": "10.236.6.117",
          "HKGS8": "10.236.9.85",
          "HKGS11": "10.236.13.133",
          "HKGS12": "10.236.20.85",
          "HKGS13": "10.236.20.165",
          "HKGS14": "10.236.22.5",
          "HKGS17":"10.209.148.12"}

def telnet(hostName, hostIP, username, password, logfile, cmd):
    prompt = '< '
    enter = "\r\n"
    log = open(logfile, "a")
    child = pexpect.spawn('telnet ' + hostIP)
    #print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + hostName + " connecting..."
    child.expect(["ENTER USERNAME < ", pexpect.EOF, pexpect.TIMEOUT])
    child.send(username + enter)
    child.expect(["ENTER PASSWORD < ", pexpect.EOF, pexpect.TIMEOUT])
    child.send(password + enter)
    child.logfile = log  #logfile
    child.expect(["MAIN LEVEL COMMAND <___>", pexpect.EOF, pexpect.TIMEOUT])
    #print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + hostName + " login successful"

    for each in cmd:
        child.expect(prompt,timeout=90)
        #print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + hostName + " send " + each
        child.send(each + enter)
    log.close()
    child.close()
    #print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + hostName + " logout successful"

def main():
    date = time.strftime('%Y%m%d', time.localtime(time.time()))
    for eachServer in servers:
        if eachServer == "HKGS17":
            cmd = cmd_for_HKGS17
        elif eachServer == "HKGS6" or eachServer == "HKGS7" or eachServer == "HKGS8":
            cmd = cmd_for_HKGS6_7_8_12_13_14
        elif eachServer == "HKGS12" or eachServer == "HKGS13" or eachServer == "HKGS14":
            cmd = cmd_for_HKGS6_7_8_12_13_14
        elif eachServer == "HKGS3" or eachServer == "HKGS11":
            cmd = cmd_for_HKGS3_11
        else:
            cmd = cmd_for_HKGS1_2_4
        #print "+++++++++++++++++++++++++++++++++++++++++++++++"
        logfile = date + "_" + eachServer + "_" + servers[eachServer] + ".log"
        telnet(eachServer, servers[eachServer], UserName, PassWord, logfile, cmd)

if __name__ == "__main__":
    main()