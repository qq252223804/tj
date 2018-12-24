from selenium import webdriver
import unittest
import HTMLTestRunner

class nimei(unittest.TestCase):
    def setUp(self):
        self.b = webdriver.Chrome()
        self.b.get("https://www.baidu.com")
    def testcase1(self):

        print self.b.title
        print ('ss')

    def tearDwon(self):
        self.b.quit()

if __name__ == '__main__':

    a=unittest.TestSuite()
    a.addTest (nimei('testcase1'))
    filename = 'C:/baidu.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'my unit test', description=u'This is a report test')
    runner.run(a)


