#coding=utf-8
from selenium import webdriver

import time


class company():
    def __init__(self):
        self.a=webdriver.Chrome()
        self.a.get('http://www.ld-kj.cn/test/ldwutest_zs/admin/login_index.html')
        self.a.find_element_by_id('smcode').send_keys('a01')
        self.a.find_element_by_id('username').send_keys('admin')
        self.a.find_element_by_id('password').send_keys(123456)
        self.a.find_element_by_id('login').click()
        time.sleep(3)
        self.a.switch_to_default_content()  #切换当前窗口 方便定位
        self.a.find_element_by_xpath('//*[@id="empmenu"]/li[3]/a').click() #点击企业管理


        # self.a.findElement(By.xpath("//*[contains(text(),'企业管理')]/parent::*")).click();




    def sousuoRight(self):
        self.a.find_element_by_id('enterpriseName').send_keys('s') #输入数据
        self.a.find_element_by_xpath('//*[@id="main_content"]/div[1]/div[2]/a[1]').click() #点击搜索
        time.sleep(3)
        b=self.a.find_element_by_xpath('//*[@id="scan_table"]/tr[2]/td[2]').text
        if b=='s':
            print u'搜索成功'
        else:
            print u'搜索失败'
        self.a.close()
    def sousuoError(self):
        self.a.find_element_by_id('enterpriseName').send_keys(0) # 输入数据
        self.a.find_element_by_xpath('//*[@id="main_content"]/div[1]/div[2]/a[1]').click() #点击搜索
        time.sleep(3)
        c=self.a.find_element_by_xpath('//*[@id="scan_table"]/tr/td').text
        print c
        if c==u'暂无数据':
            print u'搜索成功'
        else:
            print u'搜索失败'
        self.a.close()
    def xiugai_add(self):
        time.sleep(3)
        self.a.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[4]/div/a[2]').click()#点击修改
        self.a.switch_to_default_content()
        self.a.find_element_by_id('phone').send_keys('18700000000')
        self.a.find_element_by_id('linkman').send_keys(u'张')
        time.sleep(2)
        self.a.find_element_by_id('p-baocun').click()
        self.a.close()
    def xiugai_del(self):
        time.sleep(3)
        self.a.find_element_by_xpath('//*[@id="scan_table"]/tr[1]/td[4]/div/a[2]').click()#点击修改
        self.a.switch_to_default_content()
        self.a.find_element_by_id('phone').clear()
        self.a.find_element_by_id('linkman').clear()
        time.sleep(2)
        self.a.find_element_by_id('p-baocun').click()
        self.a.close()




company().sousuoRight()
company().sousuoError()
company().xiugai_add()
company().xiugai_del()


