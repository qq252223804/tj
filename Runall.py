#coding= utf-8


# import HTMLTestRunner
import HTMLTestRunnerCN   #中文版
import  unittest
# from BeautifulReport import BeautifulReport
# import BSTestRunner
#
# from jiekou.testcase import Testbaiduapi
from jiekou_1.testcase import Test_tuling


# a=unittest.TestSuite()    #定义一个测试容集
# a.addTest(unittest.makeSuite(Testbaiduapi,'testcase'))       #addTest  往容器里面加测试项，makeSuite指要执行的用例类
# b=file("C:/Users/taojian/Desktop/result.html","wb")     #file用于文件的读写   ./result.html指在哪个目录下生成文件名字  w是对文件执行写操作，b为每次覆盖
# c=HTMLTestRunner.HTMLTestRunner(stream=b,title=u'自动化测试报告',description=u'本次执行情况')  #stream报告来自的内容 tittle标题，description 描述
# c.run(a)
# b.close()

# suit=unittest.TestSuite()    #定义一个测试容集
# suit.addTest(unittest.makeSuite(Testbaiduapi,'testcase'))       #addTest  往容器里面加测试项，makeSuite指要执行的用例类
# fb=file("C:/Users/taojian/Desktop/result1.html","wb")     #file用于文件的读写   ./result.html指在哪个目录下生成文件名字  w是对文件执行写操作，b为每次覆盖
# c=HTMLTestRunnerCN.HTMLTestRunner(stream=fb,title=u'自动化测试报告',description=u'本次执行情况',tester=u'陶健')  #stream报告来自的内容 tittle标题，description 描述
# c.run(suit)
# fb.close()

# suit=unittest.TestSuite()    #定义一个测试容集
# suit.addTest(unittest.makeSuite(Testbaiduapi,'testcase'))       #addTest  往容器里面加测试项，makeSuite指要执行的用例类
# fb=file("C:/Users/taojian/Desktop/result2.html","wb")     #file用于文件的读写   ./result.html指在哪个目录下生成文件名字  w是对文件执行写操作，b为每次覆盖
# c=BSTestRunner.BSTestRunner(stream=fb,title=u'自动化测试报告',description=u'本次执行情况')  #stream报告来自的内容 tittle标题，description 描述
# c.run(suit)
# fb.close()

# if __name__ == '__main__':
#     suit=unittest.defaultTestLoader.discover('jiekou',pattern='testcase.py')
#     report=BeautifulReport(suit)
#     report.report(filename=u'接口测试报告',description=u'接口测试',log_path='report')

