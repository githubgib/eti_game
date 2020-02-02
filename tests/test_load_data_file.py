import pytest
from game import *

def test_data_file_blank():
    value == " "
    assert value == "error"

def test_data_file_wrong():
    value == "maze1.csv"
    assert value == "error"

def test_data_file_wrong_extension():
    value == "maze.ppt"
    assert value == "error"

def test_data_file_no_extension():
    value == "maze"
    assert vaule == "error"

def test_data_file_correct():
    value == "maze.csv"
    assert vaule == 8
