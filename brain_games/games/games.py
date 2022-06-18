"""Module with games."""
import random

from brain_games.function import welcome_user, random_number

from brain_games.function import ask_user, error_msg


def brain_even(tries=3):
    """
    Game brain-even, ask user if a number is even or not.

    User should give a correct answer 3 times to win.
    In case of a wrong answer the game is stopped.
    """
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    even = ''
    name = welcome_user(task)
    while tries != 0:
        number = random_number()
        if number % 2 == 0:
            even = 'yes'
        else:
            even = 'no'
        answer = ask_user(number)
        if answer == even:
            print('Correct!')
            tries -= 1
        else:
            error_msg(answer, even, name)
            return
    print('Congratulations, {0}!'.format(name))


def brain_calc(tries=3):
    """
    Game brain-calc, ask user the result of the expression.

    User should give a correct answer 3 times to win.
    In case of a wrong answer the game is stopped.
    """
    task = 'What is the result of the expression?'
    name = welcome_user(task)
    while tries != 0:
        operation = random.choice(['+', '-', '*'])
        num_1 = random_number()
        num_2 = random_number()
        question = ' '.join([str(num_1), operation, str(num_2)])
        answer = ask_user(question)
        if answer == str(eval(question)):
            print('Correct!')
            tries -= 1
        else:
            error_msg(answer, eval(question), name)
            return
    print('Congratulations, {0}!'.format(name))
