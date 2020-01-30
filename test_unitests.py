# Tests here?
import pytest
from game import *


# Unit test for functional feature: Displaying menu
@pytest.fixture
def test_display_menu(capsys):
    printMenu()
    captured = capsys.readouterr()
    assert captured.out == "hello\n"


# Unit test for functional feature: Reading Maze
def test_read_maze():
    pass


# Unit test for functional feature: Load Maze
def test_load_mazefile():
    pass


# Unit test for functional feature: Play maze
def test_play_maze():
    pass


# Unit test for functional feature: Configuring maze
def test_configure_maze():
    pass
