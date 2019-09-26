# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'


def letter_freq(txt):
    lower_text = txt.lower()
    freq = {}
    for symbol in lower_text:
        if symbol not in freq:
            freq[symbol] = 1
        else:
            freq[symbol] += 1
    return freq


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
