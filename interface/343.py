# encoding: utf-8
import os
import time
import re

#C:\Users\laraine\Desktop\文件
def find(report_path,firename):
    lists = os.listdir(report_path)
    find=re.search('firename+',lists)



