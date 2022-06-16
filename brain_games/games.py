"""Module with games."""
from random import randrange

import prompt

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
ERROR_MSG = "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!"  # noqa: E501
START = 1
END = 50


def welcome_user():
    """
    Welcome a user, ask a name.

    Returns: str
    ------------
    A user name.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have you name? ')
    print('Hello, {0}!'.format(name))
    return name


def brain_even():
    """
    Game brain-even, ask user if a number is even or not.

    User should give a correct answer 3 times to win.
    In case of a wrong answer the game is stopped.
    """
    tries = 3
    even = ''
    name = welcome_user()
    print(TASK)
    while tries != 0:
        number = randrange(START, END)         # noqa: S311
        if number % 2 == 0:
            even = 'yes'
        else:
            even = 'no'
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        if answer == even:
            print('Correct!')
            tries -= 1
        else:
            print(ERROR_MSG.format(answer, even, name))
            return
    print('Congratulations, {0}!'.format(name))
