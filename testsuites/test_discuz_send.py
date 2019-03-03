import unittest
import os
import time
from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_homepage import HomePage

class DiscuzSend(BaseTestCase):
    def test_discuz_send(self):
        """用户默认板块下发帖"""
        home_page_send = HomePage(self.driver)
        # home_page_send.open_url("http://127.0.0.1/forum.php")
        time.sleep(5)
        home_page_send.login("username","username")
        time.sleep(5)
        home_page_send.posting("haotest","好乱好乱好乱好乱好难定位啊啊啊啊啊！！！！")
        time.sleep(3)
        home_page_send.reply("真的是好难！！！！！啊！！！啊")
        time.sleep(3)
        home_page_send.logout()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main(verbosity=2)




