#coding=utf-8
import urllib2,urllib
#post
# url='http://www.ld-kj.cn/test/ldwutest_zs/admin/login_index.html'
# values={'smcode':'a01',
# 'username':'admin',
# 'password':123456
# }
# data=urllib.urlencode(values)
# request=urllib2.Request(url,data)
# response=urllib2.urlopen(request)
# print(response.read())

#get
# url='http://www.ld-kj.cn/test/ldwutest_zs/admin/login_index.html'
# values={}  #以字典的方式传入,
# values['smcode']='a01'
# values['username']='admin'
# values['password']=123456
# data=urllib.urlencode(values)
# print(data)
# geturl=url+'?'+data
# request=urllib2.Request(geturl)
# response=urllib2.urlopen(request)
# print(response.read())



#urlError与 httpError的区别
# import urllib2
#
# request = urllib2.Request('http://www.baidu123.com')
# try:
#     urllib2.urlopen(request)
# except urllib2.URLError, e:
#     print e.reason
#
# #HTTPerror
# request = urllib2.Request('http://blog.csdn.net/cqcr1')  #网址故意填错加1
# try:
#     a=urllib2.urlopen(request)
#     print a.getcode()
#     print a.read()
# except urllib2.HTTPError, e: #  HTTPError错误
#     print e.getcode()  #打印出错误状态码
#     print e.reason     #打印出错误信息  说明服务器禁止访问
#
# #我们知道，HTTPError的父类是URLError，根据编程经验，父类的异常应当写到子类异常的后面，如果子类捕获不到，
# req=urllib2.Request('http://blog.csdn.net/cqcr1')
# try:
#     urllib2.urlopen(req)
# except urllib2.HTTPError,e:
#     print e.getcode()
# except urllib2.URLError,e:
#     print e.reason
# else:
#     print('ok')

#1）获取Cookie保存到变量
# import urllib2
# import cookielib
# #声明一个CookieJar对象实例来保存cookie
# cookie = cookielib.CookieJar()
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler=urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print 'Name = '+item.name
#     print 'Value = '+item.value


#2）保存Cookie到文件
# import urllib2
# import cookielib
# #设置保存cookie的文件，同级目录下的cookie。txt
# filename='cookie.txt'
# #声明一个MoziallaCookieJar对象实例保存cookie之后写入文件
# cookie=cookielib.MozillaCookieJar(filename)
# #利用Urllib2库的HTTPcookieProcessor对象来创建cookie湖里区
# handler=urllib2.HTTPCookieProcessor(cookie)
# #通过handler来创建opener
# opener=urllib2.build_opener(handler)
# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.baidu.com')
# # 保存cookie到文件
# cookie.save(ignore_discard=True,ignore_expires=True)

 #4）利用cookie模拟网站登录
# import urllib
# import urllib2
# import cookielib
# filename='cookie1.txt'  #声明一个MoziallaCookieJar对象实例保存cookie之后写入文件
# cookie=cookielib.MozillaCookieJar(filename)
# opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata=urllib.urlencode({
#     'adminName':'an_admin_2882','adminPwd':'2882_8102'
# })
# loginurl='http://xyzcadmin.kongapi.com/login_v'  #登录接口
# response=opener.open(loginurl,postdata)   #登录请求
# cookie.save(ignore_discard=True,ignore_expires=True)   #保存cookie到文件，并进行模拟登录
# other_url='http://xyzcadmin.kongapi.com/app_v'  #应用管理接口
# result=opener.open(other_url)
# print result.read(),result.getcode()

# 以上程序的原理如下

# 创建一个带有cookie的opener，在访问登录的URL时，将登录后的cookie保存下来，然后利用这个cookie来访问其他网址。
import re
pattern=re.compile(r'hello')
result1=re.match(pattern,'hello')
result2=re.match(pattern,'helloooo cqc!')
result3=re.match(pattern,'he3lo cqc!')
result4=re.match(pattern,'hello cqc!')

if result1:
    print result1.group()
else:
    print '1匹配失败'

if result2:
    print result2.group()
else:
    print '2匹配失败'

if result3:
    print result3.group()
else:
    print '4匹配失败'

if result4:
    print result4.group()
else:
    print '4匹配失败'
