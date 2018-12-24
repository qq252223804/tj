 #-*- coding:utf-8 -*-
from appium import  webdriver
import time

a ={}
a["platformName"]="Android"
a["platformVersion"]="6.0"
a["deviceName"]="SDN6T16729003866"
b=webdriver.Remote('http://127.0.0.1:4723/wd/hub',a)

time.sleep(10)
b.find_element_by_id('')



