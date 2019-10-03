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
# https://github.com/yngvem/INF200-2019-Exercises/blob/master/exersices/ex03.rst


def test_list_of_one_element():
    list1 = [1]
    assert median(list1) == 1


