# Tests here?
import pytest
from game import *


def test_display_menu_success():
    menu = printMenu(True)
    assert menu == "Menu displayed."


def test_display_menu_failure():
    menu = printMenu(False)
    assert menu == "Menu display error."


def test_menu_invalid_option_out_of_range():
    invalidoption = mainMenu(5)
    assert invalidoption == "Invalid option selected."


def test_menu_invalid_option_characters():
    invalidoptionCharcs = mainMenu('abctest')
    assert invalidoptionCharcs == "Invalid option selected."


def test_menu_invalid_option_special_characters():
    invalidoptionSpecCharcs = mainMenu("!@#$")
    assert invalidoptionSpecCharcs == "Invalid option selected."


def test_menu_no_option():
    noOptions = mainMenu("")
    assert noOptions == "Invalid option selected."


def test_menu_select_option_1():
    Option1 = mainMenu(1, 'cut')
    assert Option1 == "Reading maze."


def test_menu_select_option_2():
    Option2 = mainMenu(2)
    assert Option2 == "Viewing maze."


def test_menu_select_option_3():
    Option3 = mainMenu(3, 'cut')
    assert Option3 == "Playing maze game."


def test_menu_select_option_4():
    Option4 = mainMenu(4, 'cut')
    assert Option4 == "Configuring current maze."


def test_menu_select_option_0():
    Option0 = mainMenu(0)
    assert Option0 == False
