import os

print("1当前目录：" + os.getcwd())
#创建目录
if os.path.exists("data"):
    print("data目录存在")
else:
    os.mkdir("data")
    print("data目录不存在，创建目录")

print("进入data目录")
os.chdir("data")  #改变目录，相对路径
#以下通过绝对路径进行目录切换，提供两种方法
#os.chdir(os.getcwd()+"\data")  #字符串相加
#os.chdir(os.path.abspath("data"))  #os.path.abspath返回绝对路径


print("返回上层目录")
#os.chdir(os.getcwd()+"\..")  #改变目录
os.chdir(os.path.abspath(".."))  #os.path.abspath返回绝对路径
print("2当前目录：" + os.getcwd())

os.chdir("data")  #改变目录，相对路径
#删除目录
#os.rmdir("data")

file_name = "text3.txt"
if not os.path.exists(file_name):    #检查文件是否存在
    file_str = open(file_name,"wb+")
    str = "hello world!"
    file_str.write(str.encode())
    file_str.close()
    print("创建文件"+file_name)
else:
    print(file_name+"文件存在")

print("4当前目录：" + os.getcwd())
list = os.listdir(os.getcwd())
print(list)
for each in list:
    if os.path.isdir(each):
        print(each + "是个目录")
    else:
        print(each + "是文件，文件大小为：",os.path.getsize(each))
        #print("文件内容为：")
        #file1 = open(each,"r+")
        #print(file1.read())
        #file1.close()