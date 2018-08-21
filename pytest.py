#！/usr/bin/env python

import os
import sys
import subprocess

r = os.popen("sc query jenkinsxxx")
text = r.read()
r.close()
print("测试结果++"+text)
