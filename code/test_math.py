import unittest
import code.math

class TestCod(unittest.TestCase):
    def test_main(self):
        self.assertEqual(code.math.add(1, 2), 3)

#    def test_ohter(self):
#        self.assertEqual(code.math.add(1, 1, 1), 3)

