# -*- coding: utf-8 -*-

__author__ = 'Helge Helo Klemetsdal'
__email__ = 'hegkleme@nmbu.no'


from random import randint as rd


def guess_sum_of_two_dicethrows():
    """The function takes a guess of the sum of two dicethrows

    :return: returns the guess as long as it is not less than 1.
    """
    your_guess = 0
    while your_guess < 1:
        your_guess = int(input('Your guess: '))
    return your_guess


def generate_sum():
    """ Generates a sum of two dice throws

    :return: The sum
    """
    return rd(1, 6) + rd(1, 6)


def check_guess(guess, generated_sum):
    """ The function checks if the guess is equal to the generated sum.

    :param guess: The players guessed sum
    :param generated_sum: The generated dice sum
    :return: True if equal, False if not
    """
    return guess == generated_sum


if __name__ == '__main__':
    win_condition = False
    guesses = 3
    Sum = generate_sum()
    while win_condition is False and guesses > 0:
        player_guess = guess_sum_of_two_dicethrows()
        win_condition = check_guess(Sum, player_guess)
        if win_condition is False:
            print('Wrong, try again!')
            guesses -= 1

    if guesses > 0:
        print('You won {} points.'.format(guesses))
    else:
        print('You lost. Correct answer: {}.'.format(Sum))
