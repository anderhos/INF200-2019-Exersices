# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'


def bubble_sort(somedata):
    datalist = list(somedata)
    data_length = len(datalist)
    while data_length > 1:
        for index in range(data_length - 1):
            if datalist[index] > datalist[index + 1]:
                datalist[index], datalist[index + 1] = datalist[index + 1], datalist[index]
        data_length -= 1
    return datalist


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
