#coding=utf-8
import time

def sousuo_right(self):
    time.sleep(2)
    self.a.switch_to_default_content()
    a=self.a.find_element_by_xpath('//*[@id="scan_table"]/tr[2]/td[2]').text
    if a=='s':
        print u'搜索已存在的企业成功'
        return True
    else:
        print u'搜索已存在的企业失败'
        return False
def sousuo_error(self):
    time.sleep(2)
    self.a.switch_to_default_content()
    b=self.a.find_element_by_xpath('//*[@id="scan_table"]/tr/td').text

    if b==u'暂无数据':
        print u'搜索不存在的企业成功'
        return True
    else:
        print u'搜索不存在的企业失败'
        return False

def xiugai_xinzeng(self):
    time.sleep(4)
    self.a.switch_to_default_content()
    c=self.a.find_element_by_xpath('//*[@id="main"]/div/div[1]/em').text
    if c==u'中国绿色产品溯源平台->企业管理>企业管理':
        print u'修改-新增内容成功'
        return True
    else:
        print u'修改-新增内容失败'
        return False

def xiugai_shanchu(self):
    time.sleep(4)
    self.a.switch_to_default_content()
    d=self.a.find_element_by_xpath('//*[@id="main"]/div/div[1]/em').text
    if d==u'中国绿色产品溯源平台->企业管理>企业管理':
        print u'修改-删除内容成功'
        return True

    else:
        print u'修改-删除内容失败'
        return False




