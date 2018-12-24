#coding=utf-8


def right_dl(self):
    b=self.driver.find_element_by_id('ldapp.preventlosefamily:id/tab_title').text
    if b==u'报警反馈':
        print(u'登陆成功')
        return True
    else:
        print(u'登陆失败')
        return False

def xg_jhr(self):
    c=self.driver.find_element_by_id('ldapp.preventlosefamily:id/tv_allview_name').text
    if c==u'监护人列表':
        print(u'监护人修改成功')
        return True
    else:
        print(u'监护人修改失败')
        return False
def tuichu(self):
    d=self.driver.find_element_by_id('ldapp.preventlosefamily:id/btn_register').text
    if d==u'立即注册':
        print(u'退出成功')
        return True
    else:
        print(u'退出失败')
        return False