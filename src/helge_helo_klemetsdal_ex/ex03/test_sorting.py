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
