# Tests here?
import pytest
from game import printMenu


# Unit test for functional feature: Displaying menu
# @pytest.fixture
# def test_display_menu(capsys):
#     printMenu()
#     captured = capsys.readouterr()
#     assert captured.out == "hello\n"

def test_print_menu_success():
    test = printMenu(True)
    assert test == "Menu displayed."

def test_print_menu_failure():
    test = printMenu(False)
    assert test == "Menu display error."
