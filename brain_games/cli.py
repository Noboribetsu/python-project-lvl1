"""CLI module."""

import prompt


def welcome_user() -> str:
    """
    Welcome a user, ask a name.

    Returns:
    --------
    name : str
        A user name.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have you name? ')
    print('Hello, {0}!'.format(name))
    return name
