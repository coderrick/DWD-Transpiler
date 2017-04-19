import os
import sys
import nose

sys.path.insert(0, os.path.abspath('../../'))
from dwd.core import *


def test_something():
    assert True


if __name__ == '__main__':
    nose.main()
