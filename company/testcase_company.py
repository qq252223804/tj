#coding=utf-8
from selenium import webdriver
from business_company import sousuo_right,sousuo_error,xiugai_xinzeng,xiugai_shanchu

import time
import unittest


class company(unittest.TestCase):
    def setUp(self):
        self.a=webdriver.Chrome()
        self.a.get('http://www.ld-kj.cn/test/ldwutest_zs/admin/login_index.html')

        self.a.find_element_by_id('smcode').send_keys('a01')
        self.a.find_element_by_id('username').send_keys('admin')
        self.a.find_element_by_id('password').send_keys(123456)
        self.a.find_element_by_id('login').click()
        time.sleep(2)
        self.a.switch_to_default_content()  #切换当前窗口 方便定位
        self.a.find_element_by_xpath('//*[@id="empmenu"]/li[3]/a').click() #点击企业管理
    def testcase1(self):
        u"""百度搜索"""
        a=self.a
        a.find_element_by_id('enterpriseName').send_keys('s') #输入数据
        a.find_element_by_xpath('//*[@id="main_content"]/div[1]/div[2]/a[1]').click() #点击搜索

        assert sousuo_right(self)


    def testcase2(self):
        a=self.a
        a.find_element_by_id('enterpriseName').send_keys(0) # 输入数据
        a.find_element_by_xpath('//*[@id="main_content"]/div[1]/div[2]/a[1]').click() #点击搜索

        assert sousuo_error(self)



    def testcase3(self):
        time.sleep(2)
        a=self.a
        a.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[4]/div/a[2]').click()#点击修改
        a.switch_to_default_content()
        time.sleep(2)
        a.find_element_by_id('phone').send_keys('18700000000')
        a.find_element_by_id('linkman').send_keys(u'张')
        a.find_element_by_id('p-baocun').click()      #点击保存

        assert xiugai_xinzeng(self)

    def testcase4(self):
        time.sleep(2)
        a=self.a
        a.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[4]/div/a[2]').click()#点击修改
        a.switch_to_default_content()
        a.find_element_by_id('phone').clear()
        a.find_element_by_id('linkman').clear()
        time.sleep(2)
        a.find_element_by_id('p-baocun').click()

        assert xiugai_shanchu(self)

    def tearDown(self):
        self.a.quit()






