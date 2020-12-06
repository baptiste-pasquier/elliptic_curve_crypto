from eccrypto.corps_fini import invmod
import pytest


def test_invmod():
    assert invmod(123, 812) == 779


def test_invmod2():
    with pytest.raises(ValueError):
        invmod(123, 0)
