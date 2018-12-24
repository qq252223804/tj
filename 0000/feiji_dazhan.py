#coding=utf-8
class Person(object):
    '''人的类'''
    def __init__(self,name):
        super(Person,self).__init__()
        self.name=name
class Gun(object):
    '''枪的类'''
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name=name  #记录枪的类型

class Danjia(object):
    '''弹夹类'''
    def __init__(self,max_num):
        super(Danjia,self).__init__()
        self.max_num=max_num  #用来记录最大子弹数量
        self.zidan_list=[]    #用来记录所有子弹的引用
    def baocun_zidan(self,zidan_temp):
        self.zidan_list.append(zidan_temp)
class Zidan(object):
    '''子弹类'''
    def __init__(self,sha_shang_li):
        super(Zidan,self).__init__()
        self.sha_shang_li=sha_shang_li #这颗子弹的威力

def main():
    '''用来控制整个程序的流程'''
