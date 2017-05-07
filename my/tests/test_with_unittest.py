import unittest
import sys, os
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, root)
import my.code

class TestCode(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(my.code.is_anagram("abc", "acb"))
        self.assertFalse(my.code.is_anagram("one", "two"))

#    def test_multiword_anagram(self):
#        self.assertTrue(my.code.is_anagram("ana gram", "naga ram"))
#        self.assertTrue(is_anagram("anagram", "nag a ram"))

# vim: expandtab
