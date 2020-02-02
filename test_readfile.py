# # Tests here?
# import pytest
from game import checkFile

def test_linecount():
    filename = str("maze.csv")
    test = checkFile(filename)
    assert test == 8