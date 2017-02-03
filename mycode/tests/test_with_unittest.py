import unittest
import sys, os
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, root)
import mycode.mymath

class TestCode(unittest.TestCase):
    def test_main(self):
        print(sys.version_info)
        print(sys.platform)
        print(sys.executable)
        print(os.uname())
        self.assertEqual(mycode.mymath.add(1, 2), 3)

#    def test_other(self):
#        self.assertEqual(mycode.mymath.add(1, 1, 1), 3)

# vim: expandtab
