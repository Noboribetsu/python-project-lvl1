"""Module with game's common fuctions."""

from random import randrange, choice

import prompt

import math


def welcome_user(task):
    """
    Welcome a user, ask a name.
    Returns: str
    ------------
    A user name.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have you name? ')
    print('Hello, {0}!\n{1}'.format(name, task))
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


def game(task, game, tries=3):
    """
    Execure commong logic for all games.
    Arguments:
    ----------
    task - task of a game.
    game - game function.
    tries - number of correct asnwer that user should make to win.
    """
    name = welcome_user(task)
    while tries != 0:
        question, result = game()
        answer = ask_user(question)
        if answer == result:
            print('Correct!')
            tries -= 1
        else:
            error_msg(answer, result, name)
            return
    print('Congratulations, {0}!'.format(name))


def game_even():
    """
    Module for brain-even.
    Prepare a random number and correct answer.
    """
    number = random_number()
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'


def game_calc():
    """
    Module for brain-calc.
    Prepare a question with expression and correct answer.
    """
    num_1 = random_number()
    num_2 = random_number()
    operation = choice(['+', '-', '*'])
    question = ' '.join([str(num_1), operation, str(num_2)])
    result = str(eval(question))
    return question, result


def game_gcd():
    """
    Module for brain-calc.
    Prepare a question with two random numbers
    and correct answer.
    """
    num_1 = random_number()
    num_2 = random_number()
    question = ' '.join([str(num_1), str(num_2)])
    result = str(math.gcd(num_1, num_2))
    return question, result


def game_progression():
    """
    Module for brain-calc.
    Prepare a question with a number prosgression,
    a hidden number and correct answer.
    """
    first_num = random_number()
    diff = random_number(2, 5)
    prg_len = 10
    last_num = first_num + diff * (prg_len - 1)
    prg = list(map(str, range(first_num, last_num, diff)))
    rnd_indx = random_number(0, prg_len - 1)
    result = prg[rnd_indx]
    prg[rnd_indx] = '..'
    question = ' '.join(prg)
    return question, result


def game_prime():
    """
    Module for brain-prime.
    Prepare a question with a number and correct answer.
    """
    number = random_number()
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                return number, 'no'
    return number, 'yes'
