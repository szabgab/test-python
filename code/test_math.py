import unittest
import sys, os
import code.math

class TestCod(unittest.TestCase):
    def test_main(self):
        print(sys.version_info)
        print(sys.platform)
        print(sys.executable)
        print(os.uname())
        self.assertEqual(code.math.add(1, 2), 3)

#    def test_ohter(self):
#        self.assertEqual(code.math.add(1, 1, 1), 3)

# vim: expandtab
