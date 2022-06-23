from pytest_tutorial import __version__
from pytest_tutorial import *


def test_version():
    assert __version__ == "0.1.0"


def test_is_miscall_AA_AA_AB():
    assert is_miscall("AA", "AA", "BB") == True
