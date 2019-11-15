import pytest


def test_succeed():
    if not True:
        pytest.xfail("failing configuration (but should work)")
    assert False


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False