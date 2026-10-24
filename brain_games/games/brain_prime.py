import random

MIN_NUMBER = 1
MAX_NUMBER = 99
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    else:
        for divider in range(2, number):
            if number % divider == 0:
                return False
    return True


def prime_question() -> str:
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f"Question: {number}")
    if is_prime(number):
        return "yes"
    return "no"
