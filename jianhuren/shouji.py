#coding=utf-8
from appium import  webdriver
import time
class shoujiTest():
    def shouji_test(self, udid, port):
        a ={}
        a["platformName"]="Android"
        a["platformVersion"]="6.0"
        a["deviceName"]=udid
        port=bytes(port)
        self.driver=webdriver.Remote('http://127.0.0.1:'+str(port)+'d/wd/hub',a)
        #
        # a['appPackage']='ldapp.preventlosefamily'
        # a['appActivity']='.ui.register.WelcomeActivity'

        a['appWaitActivity']='.ui.register.LoginActivity'
        time.sleep(5)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/et_phone_number').send_keys('18657738815')
        time.sleep(3)
        self.driver.find_element_by_id('ldapp.preventlosefamily:id/et_user_pwss').send_keys('a123456')
        time.sleep(5)
#         self.driver.find_element_by_id('ldapp.preventlosefamily:id/btn_login').click()
shoujiTest().shouji_test('c9e75238',4723)
shoujiTest().shouji_test('HC4BVYC00421',4725)

