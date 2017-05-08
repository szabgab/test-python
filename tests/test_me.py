import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import my.code

class TestMe:
    def test_is_anagram(self):
        assert my.code.is_anagram("abc", "cba")

#    def test_is_multiword_anagram(self):
#        assert my.code.is_anagram("a b c", "c b a")

    def test_example(self, tmpdir):
        path = str(tmpdir.join('abc'))
        os.system('python example.py > {}'.format(path))
        with open(path) as fh:
            result = fh.read()
        assert result == "True\nFalse\n"
