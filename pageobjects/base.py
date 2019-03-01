#自定义封装基类，将一些selenium方法封装到basepage这个类里
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import time
import os.path
#调用logger文件里的getlog方法
logger = Logger(logger="BasePage").getlog()

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
    #后退
    def back(self):
        self.driver.back("Click back on current page.")
        logger.info("Click back on current page.")
    #前进
    def forward(self):
        self.driver.forward("Click forward on current page.")
    #打开
    def open_url(self,url):
        self.driver.get(url)
    #退出
    def quit_browser(self):
        self.driver.quit()
    #关闭
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser")
        except Exception as e:
            logger.error("Failed to quit the browser with %s" % e)
    #查找元素
    def find_element(self, *loc):
        try:
            #显示等待
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)   #传一个元组类型的
            logger.info("找到页面元素-->" %loc)
        except:
            logger.error("%s页面中未找到%s元素" % (self, loc))

    #保存图片
    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to take screenshot! %s" % e)

    #输入
    def sendkeys(self,text,*loc):     #*loc  这个值是定位信息 是元组是放在最后
        el = self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容" + text)
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()
    #清除文本框
    def clear(self,*loc):
        el = self.find_element(*loc)
        try:
            el.clear()
            logger.info("Clear text in input box before typing")
        except Exception as e:
            logger.error("Failed to click the element with %s" % e)
            self.get_windows_img()
    #点击元素
    def click(self,*loc):
        el = self.find_element(*loc)
        try:
            el.click()
        except Exception as e:
            logger.error("Failed to click the element with %s" %e)

    def get_text(self,*loc):
        el = self.find_element(*loc)
        try:
            return el.text
            # print(el.text)
            logger.info("文本信息为 %s" + el.text)
        except Exception as e:
            logger.error("获得文本信息失败" % e)



    #获得文本信息
    # def get_text(self, by_type, by_value):
    #     """获得控件元素的文本信息"""
        # self.until_display(by_type, by_value)
        # return self.get_element(by_type, by_value).text



