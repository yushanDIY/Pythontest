import sys
import os
import textwrap
import io

iplist = []
iplist.append("11.8.35.1")
iplist.append("11.8.35.2")
iplist.append("11.10.167.1")
iplist.append("11.10.167.2")
iplist.append("11.10.167.3")
iplist.append("11.10.167.4")
iplist.append("11.10.167.5")
iplist.append("11.10.167.6")
iplist.append("11.10.167.7")
iplist.append("11.10.167.8")
iplist.append("11.10.167.9")
iplist.append("11.10.167.10")
iplist.append("11.10.167.11")
iplist.append("11.10.166.129")
iplist.append("11.10.166.130")
iplist.append("11.10.166.131")
iplist.append("11.10.166.132")
iplist.append("11.10.166.133")
iplist.append("11.10.166.134")
iplist.append("11.10.166.135")
iplist.append("11.10.166.136")
iplist.append("11.10.166.137")
iplist.append("11.10.166.138")
iplist.append("11.10.166.139")
iplist.append("11.10.166.140")
iplist.append("11.10.166.141")
iplist.append("11.10.166.142")
iplist.append("11.10.166.143")
iplist.append("11.10.166.144")
iplist.append("11.10.166.145")


for item in iplist:
    os.system("ping "+item)
