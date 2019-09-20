# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'


def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    squarelist = []
    for k in range(n):
        if k % 3 == 1:
            squarelist.append(k**2)
    return squarelist


if __name__ == '__main__':
    if squares_by_comp(100) != squares_by_loop(100):
        print('ERROR!')
