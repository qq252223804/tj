#coding=utf-8
# import time
# print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# 猜数字游戏
# import random
# s = random.randint(0,10)
# print(s)
# m = int(input('输入整数:'))
# while m != s:
# 	if m > s:
# 		print('大了')
# 		m = int(input('输入整数:'))
# 	if m < s:
# 		print('小了')
# 		m = int(input('输入整数:'))
# 	if m == s:
# 		print('OK')
# 		break
#
# 猜数字游戏
# import random
# num = random.randint(0, 10)
# print(num)
# while 1:
# 	user = int(input('输入整数:'))
# 	if user > num:
# 		print('大了')
# 	if user < num:
# 		print('小了')
# 	if user == num:
# 		print('OK')
# 		break
# a=raw_input('input your name:')
#
# print a

# name=raw_input('what is your name?')
# age=raw_input('how old are you?')
# print 'your name is:',name
# print 'your are '+ age +' years old'
# after_ten =int(age) +10
# print 'you will be '+str(after_ten)+' years old after ten years'



# import random
# a = random.choice(range(10))   #从0到9序列中随机挑选一个整数。
# b = random.randint(0,10)       #从0到9 随机产生一个正整数
# print a , b

# for letter in 'Python':     # 第一个实例  if循环
#    if letter == 'h':
#       break                    #break 在if之后 判断 从第一个字母开始
#    print '当期字母 :', letter   #这时print与 if同级
#
# for letter in 'hello,world':     # 第二个实例
#     if letter == 'h':               #这没有循环只是if 判断 然后打印
#         print '1期字母 :', letter
#
#     if letter == 'd':
#
#         print '2期字母 :', letter
#
# var = 10                    # 第三个实例
# while var > 0:              # while 循环判断是否大于0s
#    print '当期变量值 :', var
#    var = var -1              #设置基数
#    if var == 5:   # 当变量 var 等于 5 时退出循环
#       break

# import socket
#
# client =socket.socket()     # 声明类型   客户端 模拟tcp 发送信息
# # host = socket.gethostname()
# # port =9999
# client.connect(('127.0.0.1',9999))
# socket.bind(('127.0.0.1', 9999))
# client.send(bytes('hello',encoding='utf-8'))  #以字节类型发送消息
# data= client.recv(1024)
# print (data)
# client.close()

# server=socket.socket()      ## 声明类型   服务端 模拟tcp 发送信息
# server.bind(('127.0.0.1',9999))     #绑定ip 端口号
# server.listen()  #监听
# print ('等待链接')
# conn,address =server.accept() #  等coon服务端为客户端链接生成一个
# data= conn.recv(1024)
# print(str(data,encoding='utf-8'))
# conn.send(bytes('我收到了',encoding='utf-8'))





#
# file=open(u"E:\\tj\\lianxi\\输出的txt.txt",'w')    #open函数是open(filename , mode)
#                         #mode包括有"w"(write)， “r”(read) ， w  将循环的内容写进text文档中
# for i in range(1,200):
#     file.write('供应商%d\n'%i)        #\n 为换行 % 通配 i 变量
# file.close()                    # 每次文件操作完成之后，一定要加上file.close()函数将文件关闭。

# file=open(u"E:\\tj\\lianxi\\输出的txt.txt",'r')
# #print file.read()    #  r将  读取text文档内容
#
# a=file.readlines()      # file.readline()可以一次读取文件中内容的一行
#                         # 而readlines()是将所有数据存入list中，每一行作为list的一个element
# print a[0]            #a[1]表示读取list文档第二行内容
# file.close()

#传可变对象实例
# def changme(mylist):
#     '新增传入的列表'
#     mylist.append([1,2,3,4])
#     print '函数内取值',mylist ,'+','结果一样'
# mylist=[10,20,30]
# changme(mylist)
# print '函数外取值',mylist

#可写函数说明
# def printme( str ):
#    "打印任何传入的字符串"
#    print str
#    return
#
# #调用printme函数
# printme('这里不传参数会报错')

#可写函数说明
# def printinfo( name, age ):
#    "打印任何传入的字符串"
#    print "Name: ", name
#    print "Age ", age
#
#
# #调用printinfo函数
# printinfo( age=50, name="miki" )    #用关键字 不需要对应入参顺序
# printinfo('mike',60)

#可写函数说明
# def printinfo( name, age = 35 ):
#    "打印任何传入的字符串"
#    print "Name: ", name
#    print "Age ", age
#    return
#
# #调用printinfo函数
# printinfo( age=50, name="miki" )
# printinfo( name="mike" )


# def printinfo( arg1, *args ):   #   *args代表列表
#    "打印任何传入的参数"
#    print "输出: "
#    print arg1
#    for i in args:
#       print i
#
#
# # 调用printinfo 函数
# printinfo( 10 )
# printinfo( 70, 60, 50 )



# total = 0   #'这是一个全局变量'
# # 可写函数说明
# def sum( arg1, arg2 ):
#    '返回2个参数的和'
#    total = arg1 + arg2   #total在这里是局部变量.
#    print "函数内是局部变量 : ", total
#
# #调用sum函数
# sum( 10, 20 )
# print "函数外是全局变量 : ", total

# Money = 2000
# def AddMoney():
#    # 想改正代码就取消以下注释:
#    global Money
#    Money = Money + 1
#
# print Money
# AddMoney()
# print Money

# import time
# a =dir(time)
# print  a
#
# import math
# b =dir(math)
# print b

# import sys
# c =dir(sys)
# print c
# import os
# d =dir(os)
# print d
# print os.getcwd()

# file= open("foo.txt", "wb")
# print "文件名: ",  file.name
# print "是否已关闭 : ", file.closed
# print "访问模式 : ", file.mode
# print "末尾是否强制加空格 : ", file.softspace
#
# fo=open('foo.txt','wb')
# #以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# fo.write('www,baidu.com!!\nvery good\n')
# fo.close()
#
# # 打开一个文件
# file= open("foo.txt", "r+")  #打开一个文件用于读写。文件指针将会放在文件的开头
# str = file.read(10)
# print "读取的字符串是 : ", str
#
# # 查找当前位置
# position = file.tell()
# print "当前文件位置 : ", position
#
# # 把指针再次重新定位到文件开头
# position = file.seek(0, 0)
# str = file.read(10)
# print "重新读取字符串 : ", str
# # 关闭打开的文件
# file.close()

#
# try:
#     file = open("testfile.txt", "w")
#     file.write("这是一个测试文件，用于测试异常!!")
# except IOError:
#     print "Error: 没有找到文件或读取文件失败"
# else:
#     print "内容写入文件成功"
#     file.close()
#
# sum = lambda arg1, arg2: arg1 + arg2    #lambda  匿名函数
# sum2 =lambda bb1, bb2: bb1 *bb2
#
# # 调用sum函数
# print "相加后的值为 : ", sum( 10, 20 )
# print "相乘后的值为 : ", sum2( 10, 20 )

# def yingshe(x):     #定义一个函数
#     return x**2
# a=map(yingshe,[1,2,3,4,5])
# print a
#
# b=map(lambda x:x**2,[1,3,4,5,6]) #lambda 匿名函数
# print b
#
# c=map(lambda x,y:x+y,[1,2,3,5,6],[2,6,8,9,10]) # 匿名函数两个列表
# print c

#
# class employee():       #定义一个类 员工
#     empcount=0       #员工基数为0
#     def __init__(self,name,salary):
#         self.name =name
#         self.salary =salary
#         employee.empcount +=1
#         # employee.empcount =employee.empcout+1
#     def displaycount(self):
#         print 'total employee %d' %employee.empcount
#     def dispalyemployee(self):
#         print 'name:',self.name ,'salary:',self.salary
# emp1 =employee('tom',2000)
# emp2 =employee('lilei',3000)   #创建类的对象
#
# emp1.dispalyemployee()
# emp2.dispalyemployee()        #利用对象 再调用方法
#
# employee('tom',2000).dispalyemployee() #直接类的实例化  显示员工工资
# employee('liei',3000).displaycount()    #  统计员工数量


# class A_Parent(object):
#     def __init__(self):
#         self.parent = 'I\'m the parent.'
#         print 'Parent'
#
#     def bar(self,message):
#         print message,'from Parent'
#
# class B_Child(A_Parent):
#     def __init__(self):
# # super(B_Child,self) 首先找到 B_Child 的父类（就是类 A_Parent），
# # 然后把类B的对象 B_Child 转换为类 A_Parent 的对象
#         super(B_Child,self).__init__()
#         print 'Child'
#
#     def bar(self,message):
#         super(B_Child, self).bar(message)
#         print 'Child bar fuction'
#         print self.parent
#
# if __name__ == '__main__':
# # 更专业的用法可以用在测试模块、基类、类的重用等等方面。
#     B_Child().bar('HelloWorld')

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# class Point():
#    def __init__( self, x=0,y=0):
#       self.x = x
#       self.y = y
#    def __del__(self):
#       class_name = self.__class__.__name__
#       print class_name, "销毁"
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print id(pt1), id(pt2), id(pt3) # 打印对象的id
# del pt1
# del pt2
# del pt3

# class Parent:        # 定义父类
#    parentAttr = 100
#    def __init__(self):
#       print "调用父类构造函数"
#
#    def parentMethod(self):
#       print '调用父类方法'
#    def setAttr(self, attr):
#       Parent.parentAttr = attr
#    def getAttr(self):
#       print "父类属性 :", Parent.parentAttr
#
# class Child(Parent): # 定义子类
#    def __init__(self):
#       print "调用子类构造函数"
#
#    def childMethod(self):
#       print '调用子类方法 child method'

# c = Child()          # 实例化子类
# c.childMethod()      # 调用子类的方法
# c.parentMethod()     # 调用父类方法
# c.setAttr(200)       # 再次调用父类的方法
# c.getAttr()          # 再次调用父类的方法

# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('TYPE BAO CUO')
#     if x>=0:
#         return x
#     else:
#         return  -x
# a=my_abs(0.3)
# print a

# import math
# def move(x,y,step,a=0):
#     nx=x+step*math.cos(a)
#     ny=y-step*math.sin(a)
#     return nx,ny
# x,y = move(100, 100, 60, math.pi / 6)
# print(x,y)


# def power(x,n):
#     s=1
#     while n>0:
#         n=n-1     # 计算x的n次方
#         s=s*x
#     print s
# power(5,2)
# power(5,3)
#
# a=1
# sum=0
#
# while a<101:
#
#     sum=sum+a
#     a=a+1
#
#     print sum

# x =20
# y=8
# a='python' if x>y else 'qiwe'
# b= 'python' if x<y else 'qiwe'     #三元操作符
# print a
# print b

# a =[1,2,3,4,5]
# b=['python','www.baidu.com','qwer']
# length=len(a) if len(a)<len(b) else len(b)     #三元操作符
# print length
# c=[]            # 定义c为一个序列  将 a，b 的内容加起来
# for i in range(length): #因为a 比b的序列值多 为了取最小长度 用三元操作符得出循环三次0,1,2
#     c.append(str(a[i]) +':' +b[i])   #使用切片0,1,2取对应的值 1，2,3
# print c

#
# from selenium import webdriver
#
# import time
# a=webdriver.Chrome()
# a.get('http://www.baidu.com')
# a.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
# a.switch_to_default_content()
# time.sleep(2)
# a.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('18657738815')
# a.find_element_by_id('TANGRAM__PSP_8__password').send_keys('taojian5201314')
# a.find_element_by_id('TANGRAM__PSP_8__submit').click()
# a.quit()
#cookie= driver.get_cookies()
# print cookie

# a.add_cookie({'name':'userName', 'value':'18657738815'})
# a.add_cookie({'name':'password','value':'taojian5201314'})
# for cookie in a.get_cookies():
#     print "%s -> %s" % (cookie['name'], cookie['value'])
# a.get('http://www.baidu.com')
# a.add_cookie({'name':'userName', 'value':'18657738815'})
# a.add_cookie({'name':'password', 'value':'taojian5201314'})
#
# a.get('http://www.baidu.com')



# import re,urllib,urllib2
# x=0
# html = urllib.urlopen('http://www.youmzi.com/meinv.html ' ).read()
# def get_img():
#     pictureRegex = r'img src="(.*?)"'
#     for i in re.findall(pictureRegex, html):
#         filename = i.split("/")[-1]
#         global x
#         x+=1
#         urllib.urlretrieve(filename, "F:\\image1\%s.jpg" %x )  # 下载
#         print "正在下载%s" % filename
#
# get_img()


# import csv
# my_file='c:\\file.csv'
# data =csv.reader(file('c:\\file.csv','rb'))
# for user in data:
#     print user[0]   #读取第一列
#     print user[1]    #切片  读取第二列
#     print user[2]
#
#
# file =open('c:\\tellphone.txt','r','utf-8')
# shuru=file.readlines()
# print  shuru

# #生成固定格式一定大小的文件
# f=open('c:\\file2.csv','w')
#
# # f.seek(1024 * 1024 * 1 -1)
# name =['tom','ben','lucy']
# age=[18,22,24]
# sex=['男','女','女']
# f.write('姓名，年龄，性别\n')
# for x,y,z in zip(name,age,sex):
#     f.write('%s,%s,%s\n' %(x,y,z))
# f.close()  #  关闭操作

# import csv
# csvfile=open('c:\\file3.csv','w',newline ='')   #newline 一行结束符 None -\n
# try:
#     writer =csv.writer(csvfile) #传入参数是文件对象
#     print(type(writer))
#     writer.writerow('姓名','学号','年龄','性别')
#     for i in range(90):
#         writer.writerow(i,i+3,i*2,i*8)
#     print('文件操作成功')
# except Exception as  e:
#     print(e)
#     print('文件操作失败')
# finally:
#     csvfile.close()



#1
# try:
#     print aa
# except NameError,msg:    #变量名捕捉报错
#     print(msg)
#  #2
# try:
#     open("abc.txt",'r')
# except IOError,msg:     #  IO 文件捕捉报错
#     print(msg)
# #3
# filename =raw_input('please inpt file name :')
# if filename =='hello':
#     raise TypeError('input file name error')
   # 如果屏幕输入的是hello  则raise抛出异常 我们定义的
# #4
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get("http://www.baidu.com")
# browser.maximize_window()  # 窗口最大化
# #捕捉百度输入框异常
# try:
#     browser.find_element_by_id("kwsss").send_keys("selenium")
#     browser.find_element_by_id("su").click()
# except:
#     browser.get_screenshot_as_file("C:\\error_png.jpg")
#

#coding=utf-8
# import urllib
# import urllib2
# from bs4 import BeautifulSoup
# import re
# x=0
# i=0
# def crawl():
#     url='http://www.meizitu.com/a/more_1.html'
#     headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3084.400 QQBrowser/9.6.11346.400'}
#     req=urllib2.Request(url,headers=headers)
#     page=urllib2.urlopen(req,timeout=20)
#     contents=page.read()
#     print contents
#     socp=BeautifulSoup(contents,'html.parser')
#     my_girl=socp.find_all('img')
#     for girl in my_girl:
#         link=girl.get('src')
#         print link
#         global x
#         urllib.urlretrieve(link,'c:\\image1\%s.jpg'%x)
#         x+=1
#         print('正在打印第%s张'%x)
# crawl()

    # url='http://www.meizitu.com/a/more_1.html'
    # global x
    # # global i
    # for i in range(1,9):
    #     x+=1
    #
    #     urllib.urlretrieve('http://mm.howkuai.com/wp-content/uploads/2017a/05/18/%s.jpg'%i,'c:\\image1\%s.jpg'%x)
    #
    #
    #     print  '报告长官下载完毕'
# crawl()
# import urllib
# import urllib2
#
# import re
# def crawl_1(url):
#
#     headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3084.400 QQBrowser/9.6.11346.400'}
#     req=urllib2.Request(url,headers=headers)
#     page=urllib2.urlopen(req,timeout=20)
#     contents=page.read()
#     return contents
#
# def getImg(contents):
#     soup=r'src="(.+?.jpg)"'
#
#     imgre =re.compile(soup)
#
#     my_girl=re.findall(imgre,contents)
#     x=0
#     for girl in  my_girl:
#         urllib.urlretrieve(girl,'c:\\image1\%s.jpg'%x)
#         x+=1
#     print '报告长官  打印完毕'
# contents=crawl_1('http://www.mmjpg.com')
# getImg(contents)

#
# import os
# #列出某个文件夹下的所有case,这里用的是python，
# #所在py 文件运行一次后会生成一个pyc 的副本
# caselist=os.listdir('E:\\tj\\lianxi')
# for a in caselist:       #循环遍历
#     s=a.split('.')[1] #选取后缀名为py 的文件  split 为分割符 例如'testcase.py'被分成 'testcae','py'
#     if s=='py':
# #此处执行dos 命令并将结果保存到log.txt
#         os.system('E:\\tj%s 1>>log.txt 2>&1'%a)

# from selenium import webdriver
# import  json
# import time
# a =webdriver.Chrome()
# a.get('http://mp.weixin.qq.com')
# a.find_element_by_name('account').send_keys('563024145')
# a.find_element_by_name('')
# cookies =a.get_cookies()  #直接登陆后获取cookies
# cookie ={}
# for item in cookies:
#     cookies[item.get('name')] =item.get('value')
# with open('cookie.txt','w') as f:
#     f.write(json.dumps(cookie))

# from time import ctime
# print time.time()
# print time.ctime()
# print time.strftime('%y-%m-%d %H:%M:%S' ,time.localtime())

# from time import sleep, ctime
# import thread
# import time
# def loop0():
#     print 'start loop 0 at:',ctime()
#     sleep(4)
#     print 'loop 0 done at:', ctime()
# def loop1():
#     print 'start loop 1 at:', ctime()
#     sleep(2)
#     print 'loop 1 done at:', ctime()
# def main():
#     print 'start:', ctime()
#     # loop0()
#     # loop1()
#     thread.start_new_thread(loop0, ())
#     thread.start_new_thread(loop1, ())
#     sleep(6)
#
#     print 'all end:', ctime()
# if __name__ == '__main__':
#     main()
# else:
#     print('不导用')

# def print_time(thredname,delay):
#     count =0
#     while count <5:
#         time.sleep(delay)
#         count+=1
#         print '%s:%s' %(thredname,ctime(time.time()))
# try:
#     thread.start_new_thread(print_time,('thread_1',2))
#     thread.start_new_thread(print_time,('thread_2',4))
# except:
#    print "Error: unable to start thread"
# while 1:
#    pass

# import threading,time
# from time import ctime
#
# def thread_job1():
#     print("T1 start",ctime(time.time()))
#     time.sleep(4)
#     print("T1 finish",ctime(time.time()))
# def thread_job2():
#     print("T2 start",ctime(time.time()))
#     time.sleep(2)
#     print("T2 finish",ctime(time.time()))
# def main():
#     thread1 = threading.Thread(target=thread_job1, name='T1')
#     thread2 = threading.Thread(target=thread_job2, name='T2')
#     thread1.start()
#     thread2.start()
#     thread1.join()
#     thread2.join() #join是指thread1,2一起执行
#     print("all done\n")
# main()



# import urllib
#
# a='http://www.baidu.com'
# b=urllib.urlopen(a)    #打开网页
# c=b.read() # 读取网页源码
# # print b      #打印源码
# d=b.info()    # 返回头部信息
# # print d
# e=b.getcode()   #返回HTTP状态
# # print e
# f=b.geturl()     #f 返回网址
# # print f
#
# g=urllib.urlencode({"name":"qiwsir","web":"itdiffer.com"})
# print g  #将 dict 或者包含两个元素的元组列表转换成 url 参数。
#
#
# h=urllib.urlretrieve('http://ww1.sinaimg.cn/bmiddle/.jpg','C:me.jpg')
#urlretrieve() 是将远程服务器的图片保存在本地中图片名必须一致
# #
# import urllib2
# import urllib
#
# req=urllib2.Request('http://www.baidu.com')  #  以get方式请求打开页面
# response=urllib2.urlopen(req)
# page=response.read()            # 读取网页源码
# print page
#
# #以post 登陆网站
# url = 'http://www.ld-kj.cn/test/ldwutest/admin/login.php'  #登陆网址
#
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3084.400 QQBrowser/9.6.11346.400',
#             }                            #  浏览器头部信息
#
# data = {"method":"login","opFrom":"1","userName":"admin","password":"123456"}   #设置post 的数据  fiddler抓取 然后解密
# post_data =urllib.urlencode(data)     # 对data 数据解码
# req = urllib2.Request(url,headers) # 发送请求  模拟浏览器信息
# response = urllib2.urlopen(req,post_data) ## 打开登陆界面的url，并将data　post出去，
# the_page = response.read() #读取反馈的内容
#
# print the_page





#第二步：进入个人中心编辑页面
#注意上面cookie已经保存好了，而且注意是用这个cookie创建了httpcookieprocessor，又用这个httphandler创建了opener，所以这个opener就跟cookie关联上了，那么接下来进入个人中心就直接用这个opener就可以了
# response2 = opener.open("http://www.zhihu.com/people/edit")
#完事 谢谢



# coding=utf-8

# from selenium import webdriver
# import unittest
# import HTMLTestRunner
# class nimei(unittest.TestCase):
#     def setUp(self):
#         self.a = webdriver.Chrome()
#
#     def testcase1(self):
#         self.a.get("https://www.baidu.com")
#         print self.a.title
#
#         title=self.a.title
#         if title==u'百度一下，你就知道':
#             print '测试成功'
#             return True
#         else:
#             print '测试失败'
#             return False
#
#
#     def tearDwon(self):
#         self.a.quit()
#
# if __name__ == '__main__':
#     b = unittest.makeSuite(nimei)
#     b.addTest(unittest.makeSuite(nimei,'testcase1'))
#     filename = 'E:\\myreport.html'
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'my unit test', description=u'This is a report test')
#     runner.run(b)
#     fp.close()




# coding:utf-8
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.implicitly_wait(10)
# # 获取当前窗口句柄
# h = driver.current_window_handle
# # 定位网页、贴吧等链接
# # s = driver.find_element_by_css_selector("#u1>a")
# names=('tj_trnews','tj_trhao123')
# for one_name in names:
# # s=driver.find_element_by_css_selector("[name='tj_trhao123']")
# # s.click()
#     s=driver.find_element_by_css_selector("[name=one_name]")
#     s.click()
#     text =s.text
#     time.sleep(2)
#     all_h = driver.window_handles
#     for i in all_h:
#
#         if i != h:
#             driver.switch_to.window(i)
#             time.sleep(1)
#         print driver.title


# r = [u'新闻',u'hao123',u'地图',u'视频',u'贴吧',u'学术']
# for a, b in zip(s, r):
#     a.click()
#     text = a.text
#     time.sleep(2)
#     all_h = driver.window_handles
#     # 循环判断是否与首页句柄相等
#     for i in all_h:
#         # print i.get_attribute('href')
#         if i != h:
#             driver.switch_to.window(i)
#             time.sleep(1)
#     print driver.title
#     if b in driver.title:
#         print(text+u"页面打开正常")
#     else:
#         print(text+u"页面测试失败")
# driver.close() # 关闭当前页面




# 链接数据库
# import MySQLdb
# conn=MySQLdb.connect(host='112.74.192.99 ',user='root',passwd='Ld123456BJ',db='test',port=3307,charset="utf8")

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

# import socket               # 导入 socket 模块
#
# s = socket.socket()         # 创建 socket 对象
# host = socket.gethostname() # 获取本地主机名
# port = 3306                # 设置端口好
#
# s.connect((host, port))
# print s.recv(1024)
# s.close()
#
#
# def add(func):
#     def wra():
#         print func()+' world'
#     return wra
# def hello():
#     return 'hello'
# a=add(hello)
# print a()

# udids=('c9e75238','HC4BVYC00421')
# ports=(4723,4725)
# for udid in udids:
#    # print(udid)
#     def ui():
#         print('cesi '+ str(udid))
#     ui()
# for port in ports:
#     def ul():
#         print('cesi '+ str(port))
#
#     ul()

# coding=utf-8
# '''
# Created on 2016-8-16
# @author: Jennifer
# Project:使用Firefox浏览器
# '''
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')


# def changeme(mylist):
#     '修改传入的列表'
#     mylist.append([1,2,3,4])
#     print u'函数内取值',mylist
#     return
# mylist=[10,20]
# changeme(mylist)
# print '函数外取值',mylist

# 可写函数说明
# def printinfo( arg1, *vartuple ):  #加了星号（*）的变量名会存放所有未命名的变量参数。
#    "打印任何传入的参数"
#    print "输出: "
#    print arg1
#    for var in vartuple:  #var 未命名的变量参数
#       print var
#    return
#
# # 调用printinfo 函数
# printinfo( 10 )
# printinfo( 70, 60, 50 )


#lambda 匿名函数
# sum = lambda arg1, arg2: arg1 + arg2
# sum2 =lambda arg1, arg2: arg1 * arg2
#
# print sum(10,20), sum2(20,20)

# def reverse(li):
#     for i in range(0, len(li)/2):
#         li[i], li[-i - 1] = li[-i - 1], li[i]
# l = [1, 2, 3, 4, 5]
# reverse(l)
# print(l)

#冒泡排序
# def sort():
#     array = [1, 2, 5, 3, 6, 8,4]
#     for i in range(len(array)-1,0,-1 ): #控制循环次数
#             # print(i)
#         for j in range(0,i): #控制循环取值  i值为1-6 j取到值为（0,1.。5）
#
#             if array[j] > array[j + 1]:  #按list表取2个值比较 【5+1】表示第7个数
#                       array[j], array[j + 1] = array[j + 1], array[j]
#
#     print(array)
#
# # if __name__ == "__main__":
# sort()

#列表反转
# def daoxu(li):
#     for i in range(0, len(li)/2):
#         print li[i],li[-i-1]
#         li[i], li[-i - 1] = li[-i - 1], li[i]  # 首尾对比2次
#
#
# li=[1,2,3,4,5]
# a=li[-1]
# b=li[-2]
# daoxu(li)
# print(li),a,b

# import sys,os
# print sys.stdout.write("a"),os.getcwd()
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# fo=open('foo.txt','wb') #wb用于打开或者新建文本 指针在前写入
# fb=open('fbb.txt','a')   #a用于打开或者新建文本 指针在后写入
# fc=open('fbb.txt','r+')   #r用于打开并读取文档 r+表示读写，
# fo.write('www.baidu.com\n''cesi')
#
# fb.write('cesi\n''百度\n')
# fb.write('搜狗输入法\n')
# print fc.read()
#
# fo.close(),fb.close(),fc.close()
# print '文件名:',fo.name,\
#     '是否关闭',fo.closed

# try:
#     fh=open('testfile1','r+')
#     fh.write('这是测试文件，用于测试异常')
# except IOError:
#     print('error:没有找到文件或者读取失败')
# else:
#     print('内容写入成功')
#     fh.close()

# def temp_covert(var):
#     try:
#
#         return int(var)
#
#     except ValueError, docunment:
#         print('参数没有包含数字\n'),docunment
#
# temp_covert('测试')

#用户自定义异常
# class Networkerror():
#     def __init__(self,var):
#         self.var=var
# try:
#
#     raise Networkerror('cesi')
#
# except Networkerror,e:
# #在try语句块中，用户自定义的异常后执行except块语句，变量e是用于创建Networkerror类的实例。
#     print(e.var)

#urllib2 get请求
#coding=utf8
# import urllib2
# url='http://www.baidu1.com'
# req=urllib2.Request(url)
# response=urllib2.urlopen(req)
# page=response.read()

# print page
# print(response.getcode())  #获取状态码
# print(response.headers)

#urllib2 post 请求
# import json,urllib,urllib2,urlparse
# #1111
# sr = urlparse.urlsplit('http://www.baidu.com:80/doc?age=5#ff')
# print(sr)  #拆分url 详情
# #2222
# url='http://www.tuling123.com/openapi/api'
# data={'key':'yours',
#     'info':'你好'
#                    }
# data1=urllib.urlencode(data)  #将URL中的键值对编码以连接符&划分为参数传递并处理中文--Unicode
# # datas1=json.dumps(data)
# print(data1)
# #
# req=urllib2.Request(url,data=data1)
# response=urllib2.urlopen(req)
# print(response.getcode(),response.msg)
# print(response.read())


#requests get 请求
# import requests
# r=requests.get('http://ww.baidu.com')
# print(r.headers)

#requests post 请求
# dict={'key1':'value1','keys':'value2'}
# r1=requests.post('http://httpbin.org/post',data=dict)
# print(r1.text)


#python 数列化和反序列化

# import json
# print(json.__all__) #json库的主要方法?􀁍􀁖􀁒􀁑 􁓃􂲴􀑫􃾱􁯩􂌅􀀝?􀁖􀁒􀁑 􁓃􂲴􀑫􃾱􁯩􂌅􀀝
#
# zidian={'name':'雷子','age':24,'address':'北京'}
# print u'未序列化前的数据类为:',type(zidian)
# print u'未序列化前的数据:',json.dumps(zidian,encoding='utf-8',ensure_ascii=False)
# #字典中有中文的处理方法 进行序列化      json.dumps   输出str格式
# zidian2=json.dumps(zidian)
# print type(zidian2)

#对序列化后的中文进行反序列化         json.loads 输出dict格式

# zidian3=json.loads(zidian2)
# print u'反序列化后的数据类为:',type(zidian3)
# print u'反序列化后的数据:',zidian3


#urllib2  与request模块请求的区别
# import requests,json,urllib2,urllib
# url='http://fanyi.baidu.com/v2transapi'
# datas={'from':'en',
#        'to':'zh',
#        'query':'test'}

#1
# data=urllib.urlencode(datas)
# print(data)
# req=urllib2.Request(url,data)
# response=urllib2.urlopen(req)
# print type(response),response.getcode,response.msg  #打印状态信息
# print(response.read())     #getcode获取状态码   read()读取返回数据
# #
# #2
# html=requests.post(url,data=datas)
# print type(html.json()),(html.json())
#
# print html.status_code   # status_code 获取状态码
# print type(html.text)            #html。text获取返回数据
# print(html.text)


#3
# page= json.loads(html.text)   #将返回数据进行反序列化
# s= page['liju_result']['tag']
#
# print(s)
# a=str(s).replace('u\'','\'')
# b=a.decode("unicode-escape")   ##将list列表中的Unicode转换成中文
#
# print b
# if u'测验' in b:
#             print u'正确'
#
# else:
#      print u'cuo'


# import json,requests
# r=requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
# print r.text
# print u'数据类型:' ,type(r.text)
# r1=json.loads(r.text)
# print r1
# print u'数据类型为：',type(r1)
#

# class person(object):
#     def __init__(self,data):
#         self.data=data
#     def speak(self,a,b):
#         print self.data
#         print a,b
# person('cesi').speak(3,'中文')

# import requests

# url='http://openapi.ele.me/v2/restaurants/?consumer_key=7284397484&sig=e76dfee7276f0c7a382b4f0dbdad802a95c642aa&timestamp=1374908054'
#
# r=requests.get(url)
# s=r.text
# print(s)

# import httplib,urllib
# url='http://waimaiopen.meituan.com/api/v1/poi/shippingtime/update'
# data={"app_poi_code":'25381',"shipping_time":"7:00-9:00,11:30-19:00"}
# datas=urllib.urlencode(data)
# re=urllib2.Request(url,data=datas)
# reponse=urllib2.urlopen(re)
# print(reponse.read())


# 定义函数
# def temp_convert(var):
#     try:
#         return int(var)
#     except ValueError, e:
#         print "参数没有包含数字\n", e
#
# # 调用函数
# temp_convert("xyz")

#装饰器
# def add(func):
#     def wrapper():
#         print func() +'world'
#     return wrapper  #这是最外层返回
# def hello():
#     print('cesi')
#     return 'hello'
#
# a=add(hello)
# print a()


#coding=utf-8
# def cesi():
#     filename = raw_input('please input file name:')
#
#     if filename=='hello':
#         raise NameError('input file name zhengque !')
#     else:
#         raise NameError('input file name error')
# cesi()

# name=raw_input(u'请输入你的姓名:')
# print('姓名为:%s'%name)

# class yichang():
#     kaiguan =False #这里默认关闭屏蔽
#     def call(self,expr):
#         try:
#             print eval(expr)  #eval 是将str转为pyt显示的dict格式
#         except ZeroDivisionError:
#             if self.call:
#                 print  'k开关打开 抛出异常'
#             else:
#                 raise
#
# yichang().kaiguan=True
# yichang().call('2*6')



# def cesi():
#     try:
#         x = input('Enter the first number: ')
#         y = input('Enter the second number: ')
#         print x/y
#     except ZeroDivisionError:
#         print "输入的数字不能为0！"
#     except TypeError:           # 对字符的异常处理
#         print "请输入数字！"
#
# cesi()


#if else 嵌套
# sex=raw_input('请输入你的性别：')
# if sex=='女':
#     color = raw_input('你白么？')
#     money =raw_input('请输入你的财产总和：')
#     beautiful =raw_input('你美么？')
#     if color =='白' and money>100000 and beautiful=='美':
#         print('白富美')
#     else:
#         print('土肥圆')
# else:
#     print("判断高富帅的信息在下面")
#     high =int(raw_input('你的身高为：'))
#     money =raw_input('请输入你的财产总和：')
#     beautiful =raw_input('你帅吗？')
#     if high>=175 and money>100000 and beautiful=='帅':
#         print('高富帅')
#     else:
#         print('矮穷矬')


#while嵌套

# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print "*" ,  #加个逗号不换行  *打印25遍
#         j+=1
#     i+=1
#打印矩形
#  i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print "*",  #加个逗号不换行  * 一排5个不换行
#         j+=1
#     print ''    # 空的表示换行   *循环5遍
#     i+=1
#

#打印三角形
# i=1
# while i<=5:
#     j=1
#     while j<=i:  #打印三角形 1-5每行递增一个
#         print "*",
#         j+=1
#     print ''
#     i+=1

#99乘法表
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print "%d*%d=%d \t"%(j,i,j*i) , #加个逗号不换行,\t表示制表位table键
#         j+=1
#     print ''
#     i+=1

# import random
# i=random.randint(0,3)
# print(i)

#打印所有的偶数

# i=1
# while i<=100:
#     if i%2 ==0:
#         print(i)
#     i+=1
#打印所有的基数
# i=1
# while i<=100:
#     if i%2 ==1:
#         print(i)
#
#     i+=1
#打印1-100中前20个偶数
# i=1
# num=0
# while i<=100:
#     if i%2 ==0:
#         print(i)
#         num+=1
#     if num==20:
#         break   #break 结束while的循环
#     i+=1

#while循环中if 后的break 跟continue区别
# i=1
# while i<=10:
#     i+=1
#     print('---')
#     if i==3:
#         continue   #continue 继续while循环 但后面print i不执行
#     print(i)
# print('====')

# name='abcdeFGH'
# print name[0:5]


# lname = [ { 'Num': '001', 'Name': '张三', 'Workingtime': 'Monday', 'Money': '100' },{ 'Num': '002', 'Name': '李四', 'Workingtime': 'Tuesday', 'Money': '200' }]
# x=raw_input('xingming:')
# for y in range(len(lname)):  #列表遍历
#     if x == '张三':
#         lname.pop(y)      #用 pop。
#         # a=str(lname).encode('raw_unicode_escape')    #将list列表中的Unicode转换成中文
#
#         print lname
#         break
#     else:
#         print('ss')

# d = {1:"one", 2:"two", 3:"three"}
# # {1:"first", 4:"forth"}
#
# d.update({1:"first", 4:"forth"})
# print(d)
#
# def budingc(a,b,*args,**kwargs):  #*args表示元祖参数，**kwargs表示字典参数
#     # print(a)
#     # print(b)
#     # print(args)
#     result=a+b
#     for num in args:
#         # print(args)
#         result=result+num
#         #     result+=num   #  加法缩写
#         print result  #66是11+22+33 110是11+22+33+44
#     print('result=%d'%result)
#     print kwargs.keys(),kwargs.values(),kwargs
# # budingc(11,22,33,44)
# A=(44,55,66)
# B={'name':'laowang','age':18}
# budingc(11,22,*A,**B)  #拆包

# result=22
# arg=(33,44)
# for num in arg:
#     # print a
#     # result=result+num    #循环叠加
#     result+=num
#     print result

# def test(a,b,func):
#     result=func(a,b)
#     print(result)
# func_new=input('请输入一个匿名函数') #lambda x,y:x+y+11
# test(5,6,func_new)


#烤地瓜
# class SweetPotato:
#     def __init__(self):
#         self.cookedstring='生的'
#         self.cooedLevel =0
#         self.condiments=[]  #为了存储更多的数据。设置一个属性
#
#     def __str__(self):
#         return '地瓜 状态：%s(%d),添加的佐料有:%s'%(self.cookedstring,self.cooedLevel,self.condiments)
#     def cook(self,cooked_time):
#         self.cooedLevel+=cooked_time
#         if self.cooedLevel>=0 and self.cooedLevel<3:
#             self.cookedstring='生的'
#         elif self.cooedLevel>=3 and self.cooedLevel<5:
#             self.cookedstring ='半生不熟'
#         elif self.cooedLevel>=5 and self.cooedLevel<8:
#             self.cookedstring= '烤熟了'
#         elif self.cooedLevel>=8:
#             self.cookedstring ='烤熟了'
#
#     def addzuoliao(self,item):
#         self.condiments.append(item)
# #创建一个地瓜对象
# digua=SweetPotato()
# print(digua)
# #开始烤地瓜
# digua.cook(2)  #2表示烤2分钟
# print(digua)
# digua.cook(2)  #2表示烤2分钟
# print(digua)
# digua.addzuoliao('大蒜')
# digua.cook(3)  #2表示烤2分钟
# print(digua)
# digua.addzuoliao('番茄酱')
# digua.cook(2)
# print(digua)

#存放家具
# class Home:
#     def __init__(self,area,info,addr):
#         self.area=area
#         self.info=info
#         self.addr=addr
#         self.left_area= area
#         self.contain_items =[]
#     def __str__(self):
#         msg='房子的面积是：%d，可用面积为：%d，户型是:%s,地址是:%s'%(self.area,self.left_area,self.info,self.addr)
#         msg+='当前房子里的物品有%s'%(self.contain_items)
#
#         return msg
#     def add_item(self,item):
#         self.left_area -=item.get_area()
#         self.contain_items.append(item.get_name())
# class Bed:
#     def __init__(self,name,area):
#         self.name=name
#         self.area=area
#     def __str__(self):
#         return "%s占用面积是：%d"%(self.name,self.area)   #描述属性
#     def get_area(self):
#         return self.area
#     def get_name(self):
#         return self.name
#
# fangzi =Home(129,'三室一厅','北京朝阳区')
# print(fangzi)
# bed1=Bed(u'席梦思',4)
# bed2=Bed(u'婴儿床',2)
# fangzi.add_item(bed1)
#
# print(fangzi)
# fangzi.add_item(bed2)
# print(fangzi)
#
# 列表生成式
# a =[i for i in range(10)]
# b =[i for i in range(10) if i%2==0 ]
# print a,    b
# d=[(i,j) for i in range(3) for j in range(2)]
# print d
#字符串拼接 加join用法
word='''awfesdafhjkcasadckjsdackjsadvcnksausafdsch
'''
b='SufhwrifjiEIJFDIEJDIej'
list1 = list(word+b)
print list1
while '\n' in list1:
    list1.remove('\n')
    list2 = sorted(list1)
    print(list2)
    print(''.join(list2))

# seq1 = ['hello','good','boy','doiido']
# print ':'.join(seq1)