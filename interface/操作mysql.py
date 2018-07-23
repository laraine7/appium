# encoding: utf-8


# import pymysql
import os

report_path = r"D:\Test\fash_tech\fash_report_"  # 生成测试报告的路径
lists=os.listdir(report_path)

    # 重新按时间对目录下的文件进行排列
lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))

file=(os.path.join(report_path,lists[-1]))
print(file)
# print(lists[-1])
print(lists[-1])