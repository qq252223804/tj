#coding=utf-8
def cesi():
    try:
        x = input('Enter the first number: ')
        y = input('Enter the second number: ')
        print x/y
    except ZeroDivisionError:
        print "输入的数字不能为0！"
    except TypeError:           # 对字符的异常处理
        print "请输入数字！"

cesi()