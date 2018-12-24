#coding=utf-8
from selenium import webdriver
import os,time

import time
class product():
    def __init__(self):
        self.a=webdriver.Chrome()
        self.a.get('http://www.ld-kj.cn/test/ldwutest_zs/admin/login_index.html')

        self.a.find_element_by_id('smcode').send_keys('a01')
        self.a.find_element_by_id('username').send_keys('admin')
        self.a.find_element_by_id('password').send_keys(123456)
        self.a.find_element_by_id('login').click()
        time.sleep(3)
        self.a.switch_to_default_content()  #切换当前窗口 方便定位
    def list_add(self,i):     #默认产品列表管理

        self.a.find_element_by_xpath('//*[@id="main_content"]/div[2]/div[4]/a[2]').click() #点击添加
        self.a.switch_to_default_content()        #切换当前窗口 方便定位
        time.sleep(2)
        self.a.find_element_by_name('productName').send_keys(u'信阳毛尖%s'%i)
        self.a.find_element_by_name('productStandard').send_keys(u'1斤')
        self.a.find_element_by_name('validDate').send_keys(365)
        self.a.find_element_by_name('enterpriseID').click() #定位所属企业下拉框
        self.a.find_element_by_xpath('//*[@id="enterpriseID"]/option[3]').click()  #定位具体所属企业
        self.a.find_element_by_name('proSeriesID').click()   #定位所属系列下拉框
        self.a.find_element_by_xpath('//*[@id="proSeriesID"]/option[2]').click()   #定位具体所属企业

        self.a.find_element_by_xpath('//*[@id="l_img"]/label/img').click()     #点击照片上传按钮 打开上传窗口
        time.sleep(2)
        os.system(r'C:\tp\zl_tp.exe')
        # os.system('%s  "%s" "%s" "%s" %d %s' % ('upload.exe','打开','Edit1','Button1',3,r'C:\tp\5.jpg'))
        time.sleep(2)
        self.a.find_element_by_id('p-baocun').click()   #点击保存
        self.a.switch_to_default_content()            #切换窗口
        time.sleep(2)
        b=self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr[1]/td[4]').text   #判断跳转后的文本是否相等

        if b==(u'信阳毛尖%s'%i):
            print u'添加-成功'
        else:
            print u'添加-失败'
        self.a.close()
    def list_details(self):
        self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr[1]/td[10]/div/a[1]').click()  #点击详情
        self.a.switch_to_default_content()
        time.sleep(2)
        c=self.a.find_element_by_xpath('//*[@id="prodect-list"]/li[1]/div[1]/span[2]').text   #判断跳转后的文本是否相等

        if c==u'产 品 名 称：':
            print u'点击详情-跳转正确'
        else:
            print u'点击详情-跳转失败'
        self.a.find_element_by_id('p-cancel').click() # 点击返回
        self.a.close()
    def list_alter(self):
        self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr[1]/td[10]/div/a[2]').click() #点击修改
        self.a.switch_to_default_content()
        time.sleep(2)
        self.a.find_element_by_name('productName').clear()  #清空产品名称
        self.a.find_element_by_name('productName').send_keys(u'信阳毛尖1') #修改后产品名称
        self.a.find_element_by_id('p-baocun').click()  #点击保存
        self.a.switch_to_default_content()
        time.sleep(2)
        d=self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr[1]/td[4]').text

        if d==u'信阳毛尖1':
            print u'修改-成功'
        else:
            print u'修改-失败'
        self.a.close()
    def list_del(self):
        self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr[1]/td[10]/div/a[3]').click()  #点击删除第一条信阳毛尖1
        self.a.find_element_by_id('p_queding').click()
        self.a.switch_to_default_content()
        time.sleep(2)
        e=self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr[1]/td[4]').text #定位产品名称文本 判断是否删除成功

        if e==u'信阳毛尖1':
            print u'删除-失败'
        else:
            print u'删除-成功'
        self.a.close()

    def list_sousuo_all(self):
        self.a.find_element_by_id('enterpriseID').click()
        self.a.find_element_by_xpath('//*[@id="enterpriseID"]/option[2]').click()
        self.a.find_element_by_id('proSeriesID').click()
        self.a.find_element_by_xpath('//*[@id="proSeriesID"]/option[2]').click()
        self.a.find_element_by_id('proNames').click()     #下拉列表都单选一个
        self.a.find_element_by_xpath('//*[@id="proNames"]/option[2]').click()
        self.a.find_element_by_xpath('//*[@id="main_content"]/div[2]/div[4]/a[1]').click()
        time.sleep(2)
        self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr/td[4]').click()  #点击搜索
        self.a.switch_to_default_content()
        f=self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr/td[4]').text  #判断搜索的内容是否一致

        if f==u'山东毛尖':
            print u'搜索—下拉框选精确成功'
        else:
            print u'搜索—下拉框选精确失败'
        self.a.close()
    def list_sousuo_one(self):
        self.a.find_element_by_id('category').send_keys(u'茶叶')
        time.sleep(1)
        self.a.find_element_by_xpath('//*[@id="main_content"]/div[2]/div[4]/a[1]').click() #点击搜索
        time.sleep(2)
        self.a.switch_to_default_content()
        g=self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr[1]/td[3]').text
        if g==u'茶叶':
            print u'搜索-单个文本框输入成功'
        else:
            print u'搜索-单个文本框输入失败'
        self.a.close()
    def list_sousuo_more(self):
        self.a.find_element_by_id('category').send_keys(u'茶叶')
        self.a.find_element_by_id('productCode').send_keys(101)
        time.sleep(2)
        self.a.find_element_by_xpath('//*[@id="main_content"]/div[2]/div[4]/a[1]').click() #点击搜索
        time.sleep(2)
        self.a.switch_to_default_content()
        gg=self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr/td[3]').text
        h=self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr/td[6]').text

        if   gg==u'茶叶' and h=='101':
            print u'搜索-多个文本框输入成功'
        else:
            print u'搜索-多个文本框输入失败'
        self.a.close()
    def series_sousuo(self):
        self.a.find_element_by_id('seriesName').send_keys(u'茶叶')
        time.sleep(1)
        self.a.find_element_by_xpath('//*[@id="main_content"]/div[1]/div[2]/a[1]').click()  #点击搜索
        time.sleep(2)
        self.a.switch_to_default_content()
        aa=self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr/td[2]').text
        if aa==u'茶叶':
            print u'搜索-产品系列成功'
        else:
            print u'搜索-产品系列成功'
        self.a.close()
    def series_add(self):
        self.a.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[2]/span[2]').click()  #点击产品系列管理
        self.a.find_element_by_xpath('//*[@id="main_content"]/div[1]/div[2]/a[2]').click()  #点击添加
        time.sleep(2)
        self.a.switch_to_default_content() # 获取当前窗口

        self.a.find_element_by_xpath('/html/body/div[2]/div[4]/div/div/div[2]/ul/li[1]/input[1]').send_keys(u'碧螺春')
        self.a.find_element_by_name('enterprise').click()  # 点击所属企业列表
        self.a.find_element_by_xpath('//*[@id="enterprise"]/option[2]').click() #下拉单选企业名称
        self.a.find_element_by_id('p-baocun').click()
        time.sleep(2)
        self.a.switch_to_default_content()

        bb=self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr[1]/td[2]').text
        if bb==u'碧螺春':
            print u'添加-产品系列成功'
        else:
            print u'添加-产品系列失败'
        self.a.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/span[1]').click()  #点击产品列表管理
        time.sleep(2)
        self.a.switch_to_default_content()
        self.a.find_element_by_id('proSeriesID').click()
        cc=self.a.find_element_by_xpath('//*[@id="proSeriesID"]/option[2]').text

        if cc==u'碧螺春':
            print u'添加-检验列表管理产品系列成功'
        else:
            print u'添加-检验列表管理产品系列失败'
        self.a.find_element_by_xpath('//*[@id="prodect-table"]/tr[1]/td[10]/div/a[3]').click()
        self.a.close()








product().list_add(2)
# product().list_details()
# product().list_alter()
# product().list_del()
# product().list_sousuo_all()
# product().list_sousuo_one()
# product().list_sousuo_more()
# product().series_add()
