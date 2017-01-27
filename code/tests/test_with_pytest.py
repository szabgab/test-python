import sys, os
test_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(test_dir, '..'))
import mymath

class TestCode():
    def test_main(self):
        assert 2 == 2
        assert mymath.add(1, 2) == 3
#        assert mymath.add(1, 1, 1) == 3
        assert mymath.add(-1, 1) == 0


# vim: expandtab
