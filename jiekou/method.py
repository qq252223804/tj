#coding=utf-8
# import urllib2,urllib
from jiekou.data import ReadExcel
import requests
import json
# def POST(url, data):
url=ReadExcel(0,1,2)
data=ReadExcel(0,1,3)
# print(data)
# print(type(data))

# data1=data.encode('utf-8')  #将 Unicode 转换成 str
# print (data,type(data1))
# datas=eval(data)   #将str 转换成 dict
# print(datas)
# print(type(datas))
# #
html=requests.get(url,data=data)
print (html.status_code)
print( html.text )


# req=urllib2.Request(url,datas)
# response=urllib2.urlopen(req)         #不采取urllib2进行post传参数 失败！
# print response.read()

#写死传参数
# url='http://fanyi.baidu.com/v2transapi'
# data={'from':'en','to':'zh','query':'test'}
# print(type(data))
# datas=urllib.urlencode(data)
# print(type(datas)),datas
# req=urllib2.Request(url,datas)
# response=urllib2.urlopen(req)
# print(response.read())



# return page
#     print response.getcode,response.msg
# return page



def GET(url, data):
    # url=ReadExcel(0,1,2)
    # data=ReadExcel(0,1,3)
    # url1 = url + '?' + data
    # print url1,data
    # req = urllib2.Request(url1)
    # response = urllib2.urlopen(req)
    # page=response.read()                  #  不采取urllib2进行传参数！！！
    # # print response.getcode,response.msg
    # # print(page)
    # return page

    html=requests.get(url,data)
    # print(html.text)
    # print (html.status_code)
    return html.json()

