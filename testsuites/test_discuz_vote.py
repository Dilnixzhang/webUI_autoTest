import unittest
import time
from pageobjects.Discuz_homepage import HomePage
from testsuites.base_testcase import BaseTestCase

class DiscuzVote(BaseTestCase):
    def test_discuz_vote(self):
        """发起投票并获得结果"""
        vote_page = HomePage(self.driver)
        vote_page.open_url("http://127.0.0.1/forum.php")
        vote_page.login("username","username")
        time.sleep(3)
        vote_page.send_vote("周末除了学习能干嘛","学习","睡觉","出去玩")
        time.sleep(5)
        vote_page.send_vote_submit()
        time.sleep(5)
        vote_page.get_vote()
        time.sleep(5)
        vote_page.logout()
        time.sleep(3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
