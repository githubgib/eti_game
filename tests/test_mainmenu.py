# Tests here?
import pytest


@pytest.fixture
def sample_test():
    print("sample test working here")
    assert "test" == "test"


@pytest.fixture
def sample_test2():
    print("sample test2 working here")
    assert "test1" != "test"
