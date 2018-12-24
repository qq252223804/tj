#coding=utf-8
from demo.demo1 import test1
from demo.demo2 import test2  #直接从目录下导入方法
import demo1,demo2 #导入目录模块
import userinfo
#1
test1()
test2()  #第一种调用
#2       #第二种调用
demo1.test1()
demo2.test2()

# #3
info =userinfo.zidian()
for us1,pw1 in info.items():  #通过items()循环读取元组（键/值对）
    print us1
    print pw1
#
# #4
# import shelve
# s=shelve.open("c:\\info.db")
# print s["username"]




