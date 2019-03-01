import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()
#定义浏览器引擎类 BrowerEngine
class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))    #注意相对路径的取法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    firefox_driver_path = dir + '/tools/geckodriver.exe'

    #read the browser type from config.ini file  return the driver
    def open_browser(self):
        config = ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("you had select %s browser." % browser)
        url = config.get("testServer","URL")
        logger.info("the test server url is: %s" % url)

        if browser == "Firefox":
            #启动Firefox实例
            driver = webdriver.Firefox(self.firefox_driver_path)
            logger.info("Starting firefox browser.")

        elif browser == "Chrome":
            #启动Chrome实例
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")

        elif browser == "IE":
            #启动IE实例
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(5)
        logger.info("Set implicitly wait 5 seconds")
        return driver
    def quit_browser(self):
        logger.info("Close and quit the browser")
        self.driver.quit()
        # self.quit_browser()
