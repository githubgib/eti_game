# Tests here?
import pytest
from game import checkFile, ConfigureMenu, printConfigMenu, printMenu, mainMenu


# Unit test for functional feature: Displaying menu
# @pytest.fixture
# def test_display_menu(capsys):
#     printMenu()
#     captured = capsys.readouterr()
#     assert captured.out == "hello\n"

# Unit test for functional feature: Reading Maze
def test_read_maze():
    test = mainMenu(1, 'cut')
    assert test == "Reading maze."

# Unit test for functional feature: Load Maze


def test_view_maze():
    test = mainMenu(2)
    assert test == "Viewing maze."

# Unit test for functional feature: Play Maze


def test_play_maze():
    test = mainMenu(3, 'cut')
    assert test == "Playing maze game."

# Unit test for functional feature: Configuring maze


def test_configure_maze():
    test = mainMenu(4, 'cut')
    assert test == "Configuring current maze."

# Unit test for functional feature: Exit game


def test_mainMenu_exit():
    test = mainMenu(0)
    assert test == False

 # Unit test for functional feature: Exit game


def test_mainMenu_input_error():
    test = mainMenu(3123)
    assert test == "Invalid option selected."
