import random

from ..logic import *

MIN_NUMBER = 1
MAX_NUMBER = 99
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number: int) -> bool:
    return number % 2 == 0

def even_question() -> str:
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f"Question: {number}")
    if is_even(number):
        return "yes"
    return "no"

def main() -> None:
    name = ask_name()
    game(name, DESCRIPTION , even_question)




