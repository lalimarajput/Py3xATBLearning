import pytest


@pytest.fixture()
def is_married():
    return True


def test_i_need_confirm(is_married):
    assert is_married == False