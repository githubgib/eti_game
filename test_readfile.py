# # Tests here?
# import pytest
from game import *


def test_mazefileread():
    filename = str("maze.csv")
    test = checkFile(filename)
    assert test == 7