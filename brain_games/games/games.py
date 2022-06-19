"""Module with games."""

from brain_games.function import game_even, game_gcd, game_calc, game
from brain_games.function import game_progression


def brain_even():
    """
    Game brain-even, ask user if a number is even or not.

    User should give a correct answer 3 times to win.
    In case of a wrong answer the game is stopped.
    """
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    game(task, game_even)


def brain_calc():
    """
    Game brain-calc, ask user the result of the expression.

    User should give a correct answer 3 times to win.
    In case of a wrong answer the game is stopped.
    """
    task = 'What is the result of the expression?'
    game(task, game_calc)


def brain_gcd():
    """
    Game brain-gcd, ask user to find the greatest common divisor of given numbers.

    User should give a correct answer 3 times to win.
    In case of a wrong answer the game is stopped.
    """
    task = 'Find the greatest common divisor of given numbers.'
    game(task, game_gcd)


def brain_progression():
    task = 'What number is missing in the progression?'
    game(task, game_progression)
