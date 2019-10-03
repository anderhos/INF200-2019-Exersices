# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'


def bubble_sort(somedata):
    dat = list(somedata)
    data_length = len(dat)
    while data_length > 1:
        for index in range(data_length - 1):
            if dat[index] > dat[index + 1]:
                dat[index], dat[index + 1] = dat[index + 1], dat[index]
        data_length -= 1
    return dat


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data is not sorted_data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert bubble_sort(sorted_data) == sorted_data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    reverse_data = [3, 2, 1]
    sorted_data = [1, 2, 3]
    assert bubble_sort(reverse_data) == sorted_data


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    equal_number_list = [1, 1, 1, 1]
    assert bubble_sort(equal_number_list) == equal_number_list


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    data_1 = [4, 9, 2, 3]
    data_2 = [11, 5, 8, 8, 8, 3, 1]
    data_3 = [1.7, 2.3, 1.1]
    data_4 = ["hello", "i", "am", "happy"]
    data_5 = ["x", "y", "c", "e", "d"]
    assert bubble_sort(data_1) == [2, 3, 4, 9]
    assert bubble_sort(data_2) == [1, 3, 5, 8, 8, 8, 11]
    assert bubble_sort(data_3) == [1.1, 1.7, 2.3]
    assert bubble_sort(data_4) == ["am", "happy", "hello", "i"]
    assert bubble_sort(data_5) == ["c", "d", "e", "x", "y"]
