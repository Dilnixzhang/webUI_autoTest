from ddt import ddt,data,unpack
from selenium import webdriver
from framework.browser_engine import BrowserEngine
# import HTMLTestRunner
import unittest
# import os
@ddt
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        #setup的代码主要是测试的前提准备工作
        browser = BrowserEngine()
        self.driver = browser.open_browser()
        # self.driver = webdriver.Chrome("../tools/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def tearDown(self):
        #测试结束后的操作，基本都是关闭浏览器
        print("测试结束....")
        self.driver.quit()



