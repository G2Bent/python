import unittest
from Calculate import Calculate

class TestModule(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_add(self):
        c = Calculate(2,3)
        self.assertEqual(c.add(),5)
    def test_sub(self):
        c = Calculate(5,3)
        self.assertEqual(c.sub(),2)
    def test_mul(self):
        c = Calculate(2,3)
        self.assertEqual(c.mul(),6)
    def test_div(self):
        c = Calculate(6,3)
        self.assertEqual(c.div(),2)

if __name__ == '__main__':
    unittest.main()
