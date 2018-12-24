#coding=utf-8
from selenium import webdriver
import time


class Task:
    def __init__(self):
        self.a=webdriver.Chrome()
        self.a.get('http://www.ld-kj.cn/test/ldwutest_zs/admin/login_index.html')
        self.a.find_element_by_id('smcode').send_keys('a01')
        self.a.find_element_by_id('username').send_keys('admin')
        self.a.find_element_by_id('password').send_keys(123456)
        self.a.find_element_by_id('login').click()
        time.sleep(3)
        self.a.switch_to_default_content()
        self.a.find_element_by_xpath('//*[@id="empmenu"]/li[4]/a').click()   # 点击任务管理
    def xj_renwu(self,pici):

        a=self.a
        a.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/a[1]').click() #点击创建任务
        time.sleep(3)
        a.switch_to_default_content()
        a.find_element_by_id('enterpriseID').click()
        a.find_element_by_xpath('//*[@id="enterpriseID"]/option[2]').click()
        time.sleep(2)
        a.find_element_by_id('proSeriesID').click()
        a.find_element_by_xpath('//*[@id="proSeriesID"]/option[2]').click()
        time.sleep(2)
        a.find_element_by_id('proID').click()
        a.find_element_by_xpath('//*[@id="proID"]/option[2]').click()
        time.sleep(2)
        a.find_element_by_id('batchNO').send_keys(pici)
        a.find_element_by_id('packRatioID').click()                         #包装比例选择1
        a.find_element_by_xpath('//*[@id="packRatioID"]/option[10]').click()
        a.find_element_by_id('codeCount').send_keys(10)
        a.find_element_by_id('produceDate').send_keys('2017-06-19')

        time.sleep(2)
        a.find_element_by_id('p-baocun').click()
        time.sleep(4)

        b=a.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[18]').text

        if b==u'未审核':

            print u'创建任务成功'
        else:
            print u'创建任务失败'
        a.close()
    def pl_fuma(self,i):
        time.sleep(2)
        a=self.a
        a.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[19]/div/a[1]').click()#点击审核
        a.switch_to_default_content()
        time.sleep(1)
        a.find_element_by_id('p_queding').click()     # 弹窗点击确定
        time.sleep(2)
        c=a.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[18]').text

        if c==u'已审核':
            print u'审核成功'
        else:
            print u'审核失败'
        time.sleep(2)
        a.switch_to_default_content()
        a.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[19]/div/a[1]').click()  #点击批量赋码
        a.switch_to_default_content()
        a.find_element_by_xpath('//*[@id="main"]/div[2]/button').click()      #点击手动增加




        #打开生成的码值 txt文档 进行读取
        file=open(u"D:\\中绿生成码值\\codelist_%d.txt" %i,'r')
        bianma=file.readlines()

        a.find_element_by_id('add-1').send_keys(bianma[0])           #起始编码 号
        a.find_element_by_id('add-2').send_keys(bianma[9])          #结束编码 号
        a.find_element_by_id('baocun').click()           #点击保存
        a.find_element_by_id('p-baocun').click()
        time.sleep(3)
        a.switch_to_default_content()
        d=a.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[18]').text
        if d==u'完工':
            print u'批量赋码成功'
        else:
            print u'批量赋码失败'
        a.close()
PICI =[777,888,999]
for pici in PICI:
    Task().xj_renwu(pici)
Task().pl_fuma(153)



