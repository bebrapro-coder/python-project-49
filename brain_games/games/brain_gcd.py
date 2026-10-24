import random

MIN_NUMBER = 1
MAX_NUMBER = 99
DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(number1: int, number2: int) -> int:
    while number2 != 0:
        remain = number1 % number2
        number1 = number2
        number2 = remain
    return number1


def gcd_question() -> int:
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    final_gcd = gcd(number1, number2)
    numbers = f"{number1} {number2}"
    print(f"Question: {numbers}")
    return final_gcd
