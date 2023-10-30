import HTMLTestRunnerNew
from ui_test import *

suite = unittest.defaultTestLoader.discover(".", pattern="ui_test.py")
with open("reports.html", "wb+") as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(f, 2, title="测试报告", description="login reports", tester="111")
    runner.run(suite)
