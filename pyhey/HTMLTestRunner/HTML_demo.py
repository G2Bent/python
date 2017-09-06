import unittest
from HTMLTestRunner import HTMLTestRunner

class ExampleCasel(unittest.TestCase):
    def setUp(self):
        self.a = 4
        self.b = 3

    def test_add(self):
        self.assertEqual(self.a + self.b,7)

    def test_minus(self):
        print("这是什么鬼")
        self.assertEqual(self.a - self.b,2)

class ExampleCase2(unittest.TestCase):
    def setUp(self):
        self.a,self.b = 4,3

    def test_plus(self):
        self.assertEqual(self.a * self.b,11)

class ExampleCase3(unittest.TestCase):
    def setUp(self):
        self.a,self.b = 4,2
    def test_devide(self):
        self.assertEqual(self.a / self.b,2)

if __name__ == "__main__":
    report_title = "这是测试结果报告"
    desc = "用于展示修改样式后的测试报告"
    report_file = "../report.html"

    testsuite = unittest.TestSuite()
    testsuite.addTest(ExampleCasel("test_add"))
    testsuite.addTest(ExampleCasel("test_minus"))
    testsuite.addTest(ExampleCase2("test_plus"))
    testsuite.addTest(ExampleCase3("test_devide"))

    with open(report_file,'wb') as report:
        runner = HTMLTestRunner(stream = report,title=report_title,description=desc)
        runner.run(testsuite)