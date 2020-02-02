import pytest

from game import *


def test_data_file_blank():
    test = mainMenu(1, 'cut')
    # input == "maze"
    assert test == "Reading maze."

# def test_data_file_wrong():
#    mainMenu("1")
#    value == "maze1.csv"
#    assert value == "error"

# def test_data_file_wrong_extension():
#    mainMenu("1")
#    value == "maze.ppt"
#    assert value == "error"

# def test_data_file_no_extension():
#    mainMenu == 1
#    filename == "maze"
#    assert line_count == 8

# def test_data_file_correct():
#    mainMenu("1")
#    value == "maze.csv"
#    assert value == "error"
