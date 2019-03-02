import unittest
import os
import HTMLTestRunner
from testsuites.test_discuz_send import DiscuzSend
from testsuites.test_admin_user import DiscuzSecond
from testsuites.test_discuz_search import DiscuzSearch
from testsuites.test_discuz_vote import DiscuzVote

cur_path = os.path.dirname(os.getcwd())
report_path = os.path.join(cur_path,'test_report')
if not os.path.exists(report_path): os.mkdir(report_path)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(DiscuzSend))
suite.addTest(unittest.makeSuite(DiscuzSecond))
suite.addTest(unittest.makeSuite(DiscuzSearch))
suite.addTest(unittest.makeSuite(DiscuzVote))

if __name__ == "__main__":
    html_report = report_path + r"\result.html"
    fp = open(html_report, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="discuz实战测试报告", description="用例测试情况")
    runner.run(suite)


