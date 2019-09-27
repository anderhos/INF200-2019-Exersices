# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'


import math


def letter_freq(txt):
    lower_text = txt.lower()
    freq = {}
    for symbol in lower_text:
        if symbol not in freq:
            freq[symbol] = 1
        else:
            freq[symbol] += 1
    return freq


def entropy(message):
    entro = 0
    n = len(message)
    letter_count = letter_freq(message)
    for n_i in letter_count.values():
        if n_i > 0:
            entro -= n_i/n*math.log2(n_i/n)
    return entro


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
