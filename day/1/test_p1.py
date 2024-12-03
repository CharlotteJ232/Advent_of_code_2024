from p1 import unsorted_list_difference
from pathlib import Path


# Tests need to start with test_ or end with _test, as well as the file they are in, for pytest to automatically recognize them (by default)
# Test name: Given, When, Then
# def test_given_a_string_when_the_only_digits_are_in_the_first_and_last_place_combine_them():
#     # Structure: Arrange, Act, Assert
#     # Arrange
#     line = "1abc2"


def test_difference_between_unsorted_lists():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]

    assert unsorted_list_difference(list1, list2) == 11


def test_difference_between_unsorted_lists_2():
    list1 = [0,1]
    list2 = [3,2]

    assert unsorted_list_difference(list1,list2) == 4

