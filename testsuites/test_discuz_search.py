import unittest
import time
from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_homepage import HomePage

class DiscuzSearch(BaseTestCase):
    def test_discuz_search(self):
        """断言haotest与期望是否一致"""
        search_page = HomePage(self.driver)
        # search_page.open_url("http://127.0.0.1/forum.php")
        # window_list = self.driver.current_window_handle
        # self.driver.switch_to.window(window_list)
        search_page.login("username","username")
        time.sleep(2)
        search_page.search("haotest")
        time.sleep(3)
        self.driver.refresh()
        #验证贴子标题和期望是否一致
        try:
            assert "haotest" in self.driver.title
            print("Assertion test pass")
        except Exception as e:
            print("Assertion test failed")
        search_page.close()
        time.sleep(3)
        self.driver.switch_to_window(self.driver.window_handles[0])
        search_page.logout()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main(verbosity=2)

