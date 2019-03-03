import unittest
# from selenium import webdriver
from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_homepage import HomePage
import time

class DiscuzSecond(BaseTestCase):
    def test_admin_user(self):
        """用户新版块下发帖"""
        center_page = HomePage(self.driver)
        #管理员登录
        center_page.login("admin","admin")
        #进入默认板块 删除帖子
        center_page.delete_msg()
        time.sleep(3)
        #创建新版块
        center_page.add_new_section("admin","discuz实战3")
        time.sleep(3)
        center_page.close()
        #管理员退出
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])
        center_page.logout()
        time.sleep(5)
        #普通用户登录
        self.driver.refresh()
        center_page.login("username","username")
        #在新模块发帖  进入新版块
        time.sleep(5)
        center_page.newposting("退不出去","我怎么进啊啊啊啊啊啊啊！！！")
        time.sleep(5)
        center_page.reply("我要睡觉！！！！")
        center_page.logout()
        time.sleep(5)


if __name__ == '__main':
    unittest.main(verbosity=2)