import os

print("当前目录1："+os.getcwd())
os.chdir("D:\\python\demo")
print("当前目录2："+os.getcwd())
#os.mkdir("data")
if os.path.exists("data"):
    print("the dir is exist.")
else:
    os.mkdir("data")
    print("create dir")



print("当前目录4：" + os.path.abspath("data"))
os.chdir("data")
#print "当前目录3："+os.getcwd()
#os.chdir("D\\python\demo")

#os.rmdir("data")

file_name = "text3.txt"
if not os.path.exists(file_name):
    file_str = open(file_name,"wb")
    file_str.write("hello word")
    file_str.close()
    print("create file")
else:
    print("the file is exist.")

print("当前目录5："+os.getcwd())
list = os.listdir(os.getcwd())
print(list)
for each in list:
    if os.path.isdir(each):
        print(each + " is dir.")
    else:
        print(each + " is file.")
        print(os.path.getsize(each))
        file1 = open(each,"r+")
        print(file1.read())
        file1.close()

