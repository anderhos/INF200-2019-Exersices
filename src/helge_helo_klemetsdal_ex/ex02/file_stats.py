# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'


def char_counts(textfilename):
    with open(textfilename, "r") as file:
        read_string = file.read()
    symbol_list = []
    count_list = [0 for _ in range(256)]
    for symbol in read_string:
        symbol_list.append(symbol)
    for char in symbol_list:
        count_list[ord(char)] = symbol_list.count(char)
    return count_list


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
