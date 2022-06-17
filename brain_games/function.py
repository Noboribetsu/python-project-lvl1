"""Module with game's common fuctions."""

from random import randrange

import prompt


def welcome_user(task):
    """
    Welcome a user, ask a name.

    Returns: str
    ------------
    A user name.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have you name? ')
    print('Hello, {0}!'.format(name))
    print(task)
    return name


def random_number(start=1, end=50):
    """Return a random number."""
    return randrange(start, end)  # noqa: S311


def ask_user(question):
    """Ask user a question and return an answer."""
    print('Question: {0}'.format(question))
    return prompt.string('Your answer: ')


def error_msg(answer, result, name):
    """Print error message."""
    msg = "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!"  # noqa: E501
    print(msg.format(answer, result, name))
