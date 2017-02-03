import sys, os
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, root)
import mycode.mymath

class TestCode():
    def test_main(self):
        assert 2 == 2
        assert mycode.mymath.add(1, 2) == 3
        assert mycode.mymath.add(1, 1, 1) == 3
        assert mycode.mymath.add(-1, 1) == 0
        #assert mycode.mymath.add("a", "b") == "ab"


# vim: expandtab
