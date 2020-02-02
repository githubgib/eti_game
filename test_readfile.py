# # Tests here?
# import pytest
from game import *


def test_mazefileread():
    test = readFileName()
    assert test == "Menu displayed."