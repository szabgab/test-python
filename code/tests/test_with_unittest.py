import unittest
import sys, os
test_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(test_dir, '..'))
import mymath

class TestCode(unittest.TestCase):
    def test_main(self):
        print(sys.version_info)
        print(sys.platform)
        print(sys.executable)
        print(os.uname())
        self.assertEqual(mymath.add(1, 2), 3)

#    def test_other(self):
#        self.assertEqual(mymath.add(1, 1, 1), 3)

# vim: expandtab
