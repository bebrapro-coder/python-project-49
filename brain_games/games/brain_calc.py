import random

MIN_NUMBER = 1
MAX_NUMBER = 99
OPERATORS = ["+", "-", "*"]
DESCRIPTION = "What is the result of the expression?"


def calc(first_number: int, operator: str, second_number: int) -> int:
    match operator:
        case "+":
            return first_number + second_number
        case "-":
            return first_number - second_number
        case _:
            return first_number * second_number


def calc_question() -> tuple[str, str]:
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    calc_operator = random.choice(OPERATORS)
    numbers = f"{number1} {calc_operator} {number2}"
    result = calc(number1, calc_operator, number2)
    return numbers, str(result)
