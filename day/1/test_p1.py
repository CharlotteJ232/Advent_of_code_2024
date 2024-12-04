from p1 import list_difference, read_lists_from_file, file_column_difference
from pathlib import Path


# Tests need to start with test_ or end with _test, as well as the file they are in, for pytest to automatically recognize them (by default)
# Test name: Given, When, Then
# def test_given_a_string_when_the_only_digits_are_in_the_first_and_last_place_combine_them():
#     # Structure: Arrange, Act, Assert
#     # Arrange
#     line = "1abc2"


def test_difference_between_lists_where_right_is_larger_or_equal_than_left():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]

    assert list_difference(list1, list2) == 11


def test_difference_between_lists_where_right_is_larger_or_equal_than_left_2():
    list1 = [0, 1]
    list2 = [3, 2]

    assert list_difference(list1, list2) == 4


def test_lists_read_from_file():
    input_file_path = Path(__file__).parent / "test_input.txt"

    assert read_lists_from_file(input_file_path) == (
        ["3", "4", "2", "1", "3", "3"],
        ["4", "3", "5", "3", "9", "3"],
    )


def test_difference_between_lists_where_right_bigger_or_equal_than_left_read_from_file():
    input_file_path = Path(__file__).parent / "test_input.txt"

    assert file_column_difference(input_file_path) == 11

def test_difference_between_lists_where_right_not_always_larger_than_left():
    list1 = [1,2,5]
    list2 = [3,2,2]

    assert list_difference(list1,list2) == 3
