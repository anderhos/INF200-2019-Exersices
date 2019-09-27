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


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
