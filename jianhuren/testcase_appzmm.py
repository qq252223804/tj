 #-*- coding:utf-8 -*-
import time
import unittest
from appium import  webdriver
from jianhuren.business_zmm import right_dl,xg_jhr,tuichu



# 获取屏幕宽和高
# def getSize():
#     x=driver.get_window_size()['width']
#     y=driver.get_window_size()['height']
#     return (x,y)
#
#
# #向左滑动
# def swipeLeft(t):
#     l=getSize()
#     x1=int(l[0]*0.75)
#     y1=int(l[1]*0.5)
#     x2=int(l[0]*0.25)
#     driver.swipe(x1,y1,x2,y1,t)
#
#
#
#
# # #向右滑动
# def swipeRight(t):
#     l=getSize()
#     x1=int(l[0]*0.25)
#     y1=int(l[1]*0.5)
#     x2=int(l[0]*0.75)
#     driver.swipe(x1,y1,x2,y1,t)
# #
# # #向上滑动
# def swipeUp(t):
#     l=getSize()
#     x1=int(l[0]*0.5)
#     y1=int(l[1]*0.75)
#     y2=int(l[1]*0.25)
#     driver.swipe(x1,y1,x1,y2,t)
# #
# # #向下滑动
# def swipeDown(t):
#     l=getSize()
#     x1=int(l[0]*0.5)
#     y1=int(l[1]*0.25)
#     y2=int(l[1]*0.75)
#     driver.swipe(x1,y1,x1,y2,t)


# time.sleep(5)
# swipeRight(1000)


#点击注册
# driver.find_element_by_id('ldapp.preventlosefamily:id/btn_register').click()


# class Guardian(unittest.TestCase):
#
#     def setUp(self):
#         a ={}
#         a["platformName"]="Android"
#         a["platformVersion"]="6.0"
#         a["deviceName"]="c9e75238"
#         self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',a)
#         #
#         # a['appPackage']='ldapp.preventlosefamily'
#         # a['appActivity']='.ui.register.WelcomeActivity'
#
#         a['appWaitActivity']='.ui.register.LoginActivity'

    #用账号密码登陆
    # time.sleep(5)   #第一次启动 一定要给大量的时间
    #     time.sleep(5)
    #     self.driver.find_element_by_id('ldapp.preventlosefamily:id/et_phone_number').send_keys('18657738815')
    #     time.sleep(3)
    #     self.driver.find_element_by_id('ldapp.preventlosefamily:id/et_user_pwss').send_keys('a123456')
    #     time.sleep(5)
    #     self.driver.find_element_by_id('ldapp.preventlosefamily:id/btn_login').click()
    #
    #     # self.driver.implicitly_wait(10)  #隐性等待10秒
    #     assert right_dl(self)
    #
    # def testcase1(self):
    #     u"""修改监护人"""
    #     time.sleep(5)
    #
    #     self.driver.find_element_by_name('监护人').click()
    #     time.sleep(1)
    #     self.driver.find_element_by_name('详情').click()
    #     time.sleep(1)
    #     self.driver.find_element_by_name('编辑').click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id('ldapp.preventlosefamily:id/contact_choose_address_et').click()
    #     time.sleep(1)
    #     self.driver.swipe(500,1800,500,1500,1000)
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element_by_id('ldapp.preventlosefamily:id/btn_ok').click()
    #     time.sleep(1)
    #     self.driver.find_element_by_id('ldapp.preventlosefamily:id/contact_address_et').clear()
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element_by_id('ldapp.preventlosefamily:id/contact_address_et').send_keys('123a')
    #     self.driver.implicitly_wait(10)
    #     self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":"1040", "y":"1120"})
    #     self.driver.implicitly_wait(10)
    #     self.driver.find_element_by_id('ldapp.preventlosefamily:id/true_submit').click()
    #
    #     assert xg_jhr(self)
    #     time.sleep(3)
    #     self.driver.find_element_by_id('ldapp.preventlosefamily:id/btn_allview_back').click()      #点击返回
    #
    # def testcase2(self):
    #     u"""安全退出"""
    #
    #     time.sleep(5)
    #     self.driver.find_element_by_name('我的').click()   #点击我的
    #     time.sleep(1)
    #     self.driver.find_element_by_id('ldapp.preventlosefamily:id/setting_goto_layout').click()      #点击设置
    #     time.sleep(1)
    #     self.driver.find_element_by_id('ldapp.preventlosefamily:id/btn_cancel').click()        #点击安全退出
    #     time.sleep(1)
    #     self.driver.find_element_by_id('ldapp.preventlosefamily:id/dialog_posi_btn').click()   #提示  确定注销
    #     assert tuichu(self)
    # def tearDown(self):
    #     self.driver.quit()


class Guardian(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        devices=('c9e75238','HC4BVYC00421')
        ports=(4723,4725)
        self.device=devices[0]
        self.port=ports[0]
        a ={}
        a["platformName"]="Android"
        a["platformVersion"]="6.0"
        a["deviceName"]=self.device
        url='http://127.0.0.1:%s/wd/hub' % str(self.port)
        self.driver=webdriver.Remote(url ,a)


        # a['appPackage']='ldapp.preventlosefamily'
        # a['appActivity']='.ui.register.WelcomeActivity'

        a['appWaitActivity']='.ui.register.LoginActivity'
        #用账号密码登陆
        time.sleep(5)   #第一次启动 一定要给大量的时间
        time.sleep(5)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/et_phone_number').send_keys('18657738815')
        time.sleep(3)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/et_user_pwss').send_keys('a123456')
        time.sleep(5)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/btn_login').click()

        # self.driver.implicitly_wait(10)  #隐性等待10秒
        assert right_dl(self)


    def testcase1(self):
        u"""修改监护人"""
        time.sleep(5)

        self.driver.find_element_by_name('监护人').click()
        time.sleep(1)
        self.driver.find_element_by_name('详情').click()
        time.sleep(1)
        self.driver.find_element_by_name('编辑').click()
        time.sleep(1)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/contact_choose_address_et').click()
        time.sleep(1)
        self.driver.swipe(500,1800,500,1500,1000)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/btn_ok').click()
        time.sleep(1)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/contact_address_et').clear()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/contact_address_et').send_keys('123a')
        self.driver.implicitly_wait(10)
        self.driver.execute_script("mobile: tap", {"touchCount":"1", "x":"1040", "y":"1120"})
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/true_submit').click()

        assert xg_jhr(self)
        time.sleep(3)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/btn_allview_back').click()      #点击返回

    def testcase2(self):
        u"""安全退出"""

        time.sleep(5)
        self.driver.find_element_by_name('我的').click()   #点击我的
        time.sleep(1)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/setting_goto_layout').click()      #点击设置
        time.sleep(1)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/btn_cancel').click()        #点击安全退出
        time.sleep(1)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/dialog_posi_btn').click()   #提示  确定注销
        assert tuichu(self)
    # def tearDown(self):
    #     self.driver.quit()

#用验证码登陆
# def YZM_denglu(self):
#     self.driver.find_element_by_id('ldapp.preventlosefamily:id/question_iamge_tv').click()
#     time.sleep(3)
#     self.driver.find_element_by_id('ldapp.preventlosefamily:id/et_phone_number').send_keys('18657738815')
#     time.sleep(2)
#     self.driver.find_element_by_id('ldapp.preventlosefamily:id/verify_code_btn').click()
#     time.sleep(2)
#     self.driver.find_element_by_id('ldapp.preventlosefamily:id/btn_login').click()

#访问权限点击允许（读取照片，文件）
# def quanxian_accept(self):
#     self.driver.find_element_by_id('com.lbe.security.miui:id/permission_allow_button').click()
# #访问权限点击允许（调用摄像头）
#     self.driver.find_element_by_id('com.lbe.security.miui:id/permission_allow_button').click()
# def  quanxian_dismiss(self):
# #访问权限点击拒绝（读取照片，文件）
#     self.driver.find_element_by_id('com.lbe.security.miui:id/permission_deny_button').click()
# #访问权限点击拒绝（调用摄像头）
#     self.driver.find_element_by_id('com.lbe.security.miui:id/permission_deny_button').click()
#
# #安全退出操作
# def teardown(self):
#
#     self.driver.find_element_by_name('我的').click()   #点击我的
#     time.sleep(1)
#     self.driver.find_element_by_id('ldapp.preventlosefamily:id/setting_goto_layout').click()      #点击设置
#     time.sleep(1)
#     self.driver.find_element_by_id('ldapp.preventlosefamily:id/btn_cancel').click()        #点击安全退出
#     time.sleep(1)
#     self.driver.find_element_by_id('ldapp.preventlosefamily:id/dialog_posi_btn').click()   #提示  确定注销
# # time.sleep(1)
# # driver.find_element_by_id('ldapp.preventlosefamily:id/dialog_neg_btn')        #提示  取消注销

