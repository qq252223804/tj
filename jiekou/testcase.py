#coding=utf-8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from jiekou.method import GET,POST
from jiekou.data import ReadExcel
# from BeautifulReport import BeautifulReport

import requests,unittest,json
class Testbaiduapi(unittest.TestCase):
    def setUp(self):
        pass
    def testcase1(self):
        ''' 饿了么接口GET'''
        url=ReadExcel(0,1,2)
        data=ReadExcel(0,1,3)
        page=ReadExcel(0,1,5)
        GET(url,data)
        # 判断返回是否相等

        assert page

        # assert "code"!=1003
        # assert "data"!=''
        # assert "message"!="invalid consumer_key"
        # assert "request_id"!="o011299a6ac3f9ff5343f3af0631cf82"

    def testcase2(self):
        ''' 美团接口POST'''
        url=ReadExcel(0,2,2)
        data=ReadExcel(0,2,3)
        page=ReadExcel(0,2,5)
        POST(url,data)
        assert page


    def testcase3(self):
        '''百度接口POST'''
        url=ReadExcel(0,3,2)
        data=ReadExcel(0,3,3)
        page=ReadExcel(0,3,5)
        # print(page)

        pages=POST(url,data)
        print (pages)
        page1=json.loads(pages)    #将返回的text文本进行序列化
        # print page1
        s= page1['liju_result']['tag']
        print(s)
        a=str(s).replace('u\'','\'')    #将list列表中的Unicode转换成中文
        b=a.decode("unicode-escape")
        print(b)



        assert page ==b   #判断返回截取内容是否相等



        # if u'学习' in s:
        #     return True
        # else:
        #     return False
    def tearDown(self):
        pass

# if __name__=='__main__':
#     unittest.main(verbosity=3)

a=Testbaiduapi()
print(a.testcase1())


