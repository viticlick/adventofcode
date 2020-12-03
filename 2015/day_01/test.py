import unittest
from exercise01 import elevator, basement

class TestParenthesis(unittest.TestCase):

    def test_1(self):
        self.assertEqual(elevator('(())'), 0)

    def test_2(self):
        self.assertEqual(elevator('()()'), 0)

    def test_3(self):
        self.assertEqual(elevator('((('), 3)

    def test_4(self):
        self.assertEqual(elevator('(()(()('), 3)

    def test_5(self):
        self.assertEqual(elevator('))((((('), 3)

    def test_6(self):
        self.assertEqual(elevator('())'), -1)

    def test_7(self):
        self.assertEqual(elevator('))('), -1)

    def test_8(self):
        self.assertEqual(elevator(')))'), -3)

    def test_9(self):
        self.assertEqual(elevator(')())())'), -3)

    def test_basement_1(self):
        self.assertEqual(basement(')'), 1)

    def test_basement_2(self):
        self.assertEqual(basement('()())'), 5)

if __name__ == '__main__':
    unittest.main()
