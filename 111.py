#coding=utf-8
from selenium import webdriver

import time
import unittest

class company(unittest.TestCase):
    def setUp(self):

        self.a=webdriver.Ie()
        self.a.get('http://www.ld-kj.cn/test/ldwutest_zs/admin/login_index.html')

        self.a.find_element_by_id('smcode').send_keys('a01')
        self.a.find_element_by_id('username').send_keys('admin')
        self.a.find_element_by_id('password').send_keys(123456)
        self.a.find_element_by_id('login').click()
        time.sleep(2)
        self.a.switch_to_default_content()  #切换当前窗口 方便定位
        self.a.find_element_by_xpath('//*[@id="empmenu"]/li[3]/a').click() #点击企业管理
    # def testcase1(self):
    #     a=self.a
    #     a.find_element_by_id('enterpriseName').send_keys('s') #输入数据
    #     a.find_element_by_xpath('//*[@id="main_content"]/div[1]/div[2]/a[1]').click() #点击搜索
    #     time.sleep(2)
    #     b=a.find_element_by_xpath('//*[@id="scan_table"]/tr[2]/td[2]').text
    #     if b=='s':
    #         print u'搜索已存在的企业成功'
    #         return True
    #
    #     else:
    #         print u'搜索已存在的企业失败'
    #         return False
    #
    # def testcase2(self):
    #     a=self.a
    #     a.find_element_by_id('enterpriseName').send_keys(0) # 输入数据
    #     a.find_element_by_xpath('//*[@id="main_content"]/div[1]/div[2]/a[1]').click() #点击搜索
    #     time.sleep(2)
    #     c=self.a.find_element_by_xpath('//*[@id="scan_table"]/tr/td').text
    #
    #     if c==u'暂无数据':
    #         print u'搜索不存在的企业成功'
    #         return True
    #     else:
    #         print u'搜索不存在的企业失败'
    #         return False

    def testcase1(self):
        a=self.a
        time.sleep(2)
        a.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[4]/div/a[2]').click()#点击修改
        a.switch_to_default_content()
        time.sleep(2)
        a.find_element_by_id('phone').send_keys('18700000000')
        a.find_element_by_id('linkman').send_keys(u'张')

        a.find_element_by_id('p-baocun').click()      #点击保存
        time.sleep(4)

        d=a.find_element_by_class_name('showmes').text
        a.switch_to_default_content()
        print d

        if d==u'添加成功':
            print u'修改-新增内容成功'
            return True
        else:
            print u'修改-新增内容失败'
            return False



    def testcase4(self):
        a=self.a
        time.sleep(2)
        a.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[4]/div/a[2]').click()#点击修改
        a.switch_to_default_content()
        a.find_element_by_id('phone').clear()
        a.find_element_by_id('linkman').clear()
        time.sleep(2)
        a.find_element_by_id('p-baocun').click()
        time.sleep(4)
        a.switch_to_default_content()
        e=a.find_element_by_xpath('//*[@id="main"]/div/div[1]/em').text

        if e==u'中国绿色产品溯源平台->企业管理>企业管理':
            print u'修改-删除内容成功'
            return True

        else:
            print u'修改-删除内容失败'
            return False




    def tearDown(self):
        self.a.quit()

