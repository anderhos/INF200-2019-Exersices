# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'

import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sort_data = sorted(data)
    num_el = len(sort_data)
    if num_el == 0:
        raise ValueError
    if num_el % 2 == 1:
        return sort_data[num_el // 2]
    else:
        return (sort_data[num_el // 2 - 1] + sort_data[num_el // 2]) / 2
# Code found from
# https://github.com/yngvem/INF200-2019-Exercises repo in ex03.rst


def test_list_of_one_element():
    list1 = [1]
    assert median(list1) == 1


def test_list_of_odd_elements():
    odd_list = [1, 1, 1]
    assert median(odd_list) == 1


def test_list_of_even_elements():
    even_list = [1, 1, 1, 2]
    assert median(even_list) == 1


def test_ordered_elements():
    ord_list = [1, 2, 3, 4, 5]
    assert median(ord_list) == 3


def test_rev_ordered_elements():
    rev_list = [5, 4, 3, 2, 1, 0]
    assert median(rev_list) == 2.5


def test_un_ordered_elements():
    unord_list = [3, 20, 1, 3]
    assert median(unord_list) == 3


def test_empty_gives_error():
    with pytest.raises(ValueError):
        median([])


def test_if_data_unchanged():
    data = [1, 2, 3, 4]
    median(data)
    assert data == [1, 2, 3, 4]


def test_works_for_tuples():
    some_tuple = (1, 2, 3, 4)
    assert median(some_tuple) == 2.5

