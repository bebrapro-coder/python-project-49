import random

MIN_NUMBER = 1
MAX_NUMBER = 99
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    return number % 2 == 0


def even_question() -> tuple[str, str]:
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    if not is_even(number):
        return str(number), "no"
    return str(number), "yes"
