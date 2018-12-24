# coding=utf-8
#  @Author  : leizi
import requests,json
import yaml,unittest,HTMLTestRunnerCN



class Test_tuling(unittest.TestCase):
    def setUp(self):

        self.data_file = open(r"C:\Users\taojian\Desktop\tj\jiekou_1\data.yaml","r")
        self.data = yaml.load(self.data_file)
        self.post_data=self.data['post']

    def tearDown(self):
        pass
    def test_post1(self):

        self.url=self.post_data['post1']['url']
        self.data=self.post_data['post1']['data'].encode('utf-8')  #从yaml中取出来变为Unicode在转成str
        self.datas=eval(self.data)   #将str 转换成 dict python只能用字典传入

        self.fangshi=self.post_data['post1']['fangshi']
        self.code=self.post_data['post1']['code']

        self.me=requests.post(url=self.url,params=self.datas)

        # code=json.loads(self.me.text)['code']  #  将返回的状态码定义一个变量
        self.assertEquals(self.me.status_code,200,msg='url或者服务器错误')
        code=self.me.json().get('code')
        self.assertEqual(code,self.code,msg=self.me.text)# 如果状态不等 抛出返回信息

    def test_post2(self):

        self.url=self.post_data['post2']['url']
        self.data=self.post_data['post2']['data'].encode('utf-8')  #从yaml中取出来变为Unicode在转成str
        self.datas=eval(self.data)   #将str 转换成 dict python只能用字典传入

        self.fangshi=self.post_data['post2']['fangshi']
        self.code=self.post_data['post2']['code']

        self.me=requests.post(url=self.url,params=self.datas)

       # code=json.loads(self.me.text)['code']  #  将返回的状态码定义一个变量
        self.assertEquals(self.me.status_code,200,msg='url或者服务器错误')
        code=self.me.json().get('code')
        self.assertEqual(code,self.code,msg=self.me.text)# 如果状态不等 抛出返回信息

    def test_post3(self):

        self.url=self.post_data['post3']['url']
        self.data=self.post_data['post3']['data'].encode('utf-8')  #从yaml中取出来变为Unicode在转成str
        self.datas=eval(self.data)   #将str 转换成 dict python只能用字典传入

        self.fangshi=self.post_data['post3']['fangshi']
        self.code=self.post_data['post3']['code']

        self.me=requests.post(url=self.url,params=self.datas)

        # code=json.loads(self.me.text)['code']  #  将返回的状态码定义一个变量
        self.assertEquals(self.me.status_code,200,msg='url或者服务器错误')
        code=self.me.json().get('code')
        self.assertEqual(code,self.code,msg=self.me.text)# 如果状态不等 抛出返回信息



    def test_post4(self):
        self.url=self.post_data['post4']['url']
        self.data=self.post_data['post4']['data'].encode('utf-8')  #从yaml中取出来变为Unicode在转成str
        self.datas=eval(self.data)   #将str 转换成 dict python只能用字典传入

        self.fangshi=self.post_data['post4']['fangshi']
        self.code=self.post_data['post4']['code']

        self.me=requests.post(url=self.url,params=self.datas)  #发送post请求

        # code=json.loads(self.me.text)['code']  #  将返回的状态码定义一个变量
        self.assertEquals(self.me.status_code,200,msg='url或者服务器错误')
        code=self.me.json().get('code')
        self.assertEqual(code,self.code,msg=self.me.text)# 如果状态不等 抛出返回信息
        # if self.me.status_code==200:
        #     code=self.me.json().get('code')
        #     self.assertEquals(code,self.code,msg=self.me.text)
        # else:
        #     print('url或者服务器错误')


# if __name__ == '__main__':

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test_tuling,'test'))
report_path='C:/Users/taojian/Desktop/result2.html'
fp=file(report_path,'wb')# 调用HTMLtestrunner来执行脚本并生成测试报告，html格式的
runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='report',description='demo')
runner.run(suite)
fp.close()







