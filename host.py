import io
import sys
import xml.etree.cElementTree as ET
import re
import os
import shutil

hostspath = R"C:\Windows\System32\drivers\etc"
oldehosts = R"\hosts备份"
ymconfigpath = os.getcwd()

global xmltree
global Bhost

def getinput():
    return input("请选择：")

def gettree(note):
    globals
    xmltree = ET.parse(ymconfigpath + R"\B3IPconfig.xml")
    jd =  xmltree.findall(note+"/")
    if jd.__len__() <= 0:
        val = xmltree.find(note)
        global Bhost
        Bhost = val.text
        return
    taglist = []
    for item in jd:
        taglist.append(item.tag)
        print(item.tag)
    global i
    while(True):
        i = getinput()
        if(x is not None and i in taglist):
            break
        for item in taglist:
            print(item)
    gettree(note+"/"+i)

def xghosts():
    globals
    xmltree = ET.parse(ymconfigpath + R"\B3IPconfig.xml")
    trreroot = xmltree.getroot()
    treerotlist = []
    for item in trreroot:
        treerotlist.append(item.tag)
        print(item.tag)

    global x
    while(True):
        x = getinput()
        if(x is not None and x in treerotlist):
            break
        for item in treerotlist:
            print(item)

    gettree(x)

    ym = Bhost.split("\n")
    print(ym.__len__())
    ymlist = []
    for item in ym:
        lines = re.sub(R"\s", "-", item.strip(), 0).split("-")
        ymlist.append(lines[lines.__len__()-1])

    hostfile = open(hostspath + R"\hosts", "r", encoding='utf-8')
    newhostfile = ""
    for item in hostfile.readlines():
        lines = re.sub(R"\s", "-", item.strip(), 0).split("-")
        if lines.__len__() > 0 and lines[lines.__len__()-1] in ymlist:
            continue
        newhostfile += item
    newhostfile += Bhost
    print(newhostfile)

    if not os.path.exists(hostspath + oldehosts):
        print("复制文件")
        shutil.copyfile(hostspath + R"\hosts", hostspath + oldehosts)

    newhostfilewr = open(hostspath + R"\hosts", "w", encoding='utf-8')
    newhostfilewr.write(newhostfile)
    os.system('ipconfig /flushdns')
    print("在hosts文件中添加B3域名成功")



def hyhosts():
    if os.path.exists(hostspath + oldehosts):
        os.remove(hostspath + R"\hosts")
        shutil.copyfile(hostspath + oldehosts, hostspath + R"\hosts")
        os.remove(hostspath + oldehosts)
        print("还原host文件完成")
        os.system('ipconfig /flushdns')
    else:
        print("没有此程序形成备份，不用此程序还原")
     

print("1、在hosts文件中添加B3域名")
print("2、还hosts文件")

rcom = input("请选择：")
if int(rcom) == 1:
    xghosts()
if int(rcom) == 2:
    hyhosts()

os.system('pause')