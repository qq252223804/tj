#coding= utf-8
import HTMLTestRunner
from jianhuren.testcase_appzmm import Guardian
import unittest
a=unittest.TestSuite()    #定义一个测试容集
a.addTest(unittest.makeSuite(Guardian,'testcase'))
# a.addTest(unittest.makeSuite(Guardian,'testcase2'))#addTest  往容器里面加测试项，makeSuite指要执行的用例类
b=file("E:/result_APP.html","wb")     #file用于文件的读写   ./result.html指在哪个目录下生成文件名字  w是对文件执行写操作，b为每次覆盖
c=HTMLTestRunner.HTMLTestRunner(stream=b,title=u'自动化测试报告',description=u'本次执行情况')  #stream报告来自的内容 tittle标题，description 描述
c.run(a)
b.close()