#！/usr/bin/env python

import io
import sys
import xml.etree.cElementTree as ET
import re
import os
import shutil
import threading
import datetime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None

def execmd
r = os.popen("sc query jenkinsxxx")
text = r.read()
r.close()
print("测试结果++"+text)


def loop(pdcomm,fzcomm,hxcomm):
    os.system()
    
    return jg





list = [1, 2, 3, 4, 5]

tlist = []
for j in list:
    t = MyThread(loop, (j,), loop.__name__)
    t.start()
    tlist.append(t)

for itme in tlist:
    itme.join()
    print(itme.get_result())
