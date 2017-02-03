import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mycode.mymath
class TestMe:
    def test_add(self):
        assert mycode.mymath.add(2, 3) == 5

    def test_example(self, tmpdir):
        path = str(tmpdir.join('abc'))
        os.system('python example.py > {}'.format(path))
        with open(path) as fh:
            result = fh.read()
        assert result.rstrip("\n") == "5"
