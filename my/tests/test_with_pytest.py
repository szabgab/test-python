import sys, os
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, root)
import my.code

class TestCode():
    def test_anagram():
        assert my.code.is_anagram("abc", "acb")
        assert my.code.is_anagram("one", "two")

#    def test_multiword_anagram():
#        assert my.code.is_anagram("ana gram", "naga ram")
#        assert is_anagram("anagram", "nag a ram")

# vim: expandtab
