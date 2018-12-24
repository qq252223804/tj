#coding=utf-8
class A_Parent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')

    def bar(self,message):
        print (message,'from Parent')

class B_Child(A_Parent):
    def __init__(self):
# super(B_Child,self) 首先找到 B_Child 的父类（就是类 A_Parent），
# 然后把类B的对象 B_Child 转换为类 A_Parent 的对象
        super(B_Child,self).__init__()
        print('Child')

    def bar(self,message):
        super(B_Child, self).bar(message)
        print ('Child bar fuction')
        print (self.parent)

if __name__ == '__main__':
# 更专业的用法可以用在测试模块、基类、类的重用等等方面。
    B_Child().bar('HelloWorld')
    print('验证是否作为主程序运行')
else:
    print('验证是否作为模块调用')

#总结：在if __name__ == "__main__"：之后的语句作为模块被调用的时候，语句之后的代码不执行,执行else部分；
# 直接使用的时候，语句之后的代码执行。通常，此语句用于模块测试中使用。































