#coding=utf-8
from selenium import webdriver
import time
class code():
    def __init__(self):
        self.a=webdriver.Chrome()
        self.a.get('http://www.ld-kj.cn/test/ldwutest_zs/admin/login_index.html')
        self.a.find_element_by_id('smcode').send_keys('a01')
        self.a.find_element_by_id('username').send_keys('admin')
        self.a.find_element_by_id('password').send_keys(123456)
        self.a.find_element_by_id('login').click()
        time.sleep(3)
        self.a.switch_to_default_content()
        self.a.find_element_by_xpath('//*[@id="empmenu"]/li[2]/a').click()          #点击 编码管理模块
    def hdy_shengcheng(self,i):
        b =self.a
        b.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/span[2]').click()   #点击后定义编码
        time.sleep(2)
        b.switch_to_default_content()
        b.find_element_by_id('codeCount').send_keys('%d'%i)          #定位文本框 输入生成，码值数量
        b.find_element_by_xpath('//*[@id="main_content"]/div[1]/div[2]/a').click()    #点击生成
        time.sleep(2)

        c =b.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[6]').text    #定位下载 状态文本框

        if c==u'未下载':
            print u'后定定义码值生成成功'
        else:
            print u'后定定义码值生成失败'
        b.quit()
    def hdy_xiazai(self,s):
        b =self.a
        b.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/span[2]').click()   #点击后定义编码
        time.sleep(2)
        b.switch_to_default_content()
        b.find_element_by_xpath(('//*[@id="scan_table"]/tr[%s]/td[7]/div/a[1]')%s).click()    #点击下载

        time.sleep(2)

        d=b.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[6]').text

        if d==u'已下载':
            print u'后定义码值下载成功'
        else:
            print u'后定义码值下载失败'
        b.quit()


shuliang=[10,100,200]
for i in shuliang:
    code().hdy_shengcheng(i)
S =[1,2,3]
for s in S:
    code().hdy_xiazai(s)







