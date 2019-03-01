import unittest
import os
import HTMLTestRunner

cur_path = os.path.dirname(os.getcwd())
report_path = os.path.join(cur_path,'test_report')
if not os.path.exists(report_path): os.mkdir(report_path)
test_dir = './testsuites'

suites = unittest.TestLoader().discover(test_dir,pattern='test_*.py')

if __name__ == "__main__":
    html_report = report_path + r"\result.html"
    fp = open(html_report,"wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="discuz实战测试报告",description="用例测试情况")
    runner.run(suites)