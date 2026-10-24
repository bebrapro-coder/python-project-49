import random

MIN_NUMBER = 1
MAX_NUMBER = 99
DESCRIPTION = "What is the result of the expression?"

def calc(first_number: int, operator: str, second_number: int) -> int:
    if operator == "+":
        correct_answer = first_number + second_number
        return correct_answer
    elif operator == "-":
        correct_answer = first_number - second_number
        return correct_answer
    else:
        correct_answer = first_number * second_number
        return correct_answer

def calc_question() -> int:
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    calc_operator = random.choice(["+", "-", "*"])
    print(f"Question: {number1} {calc_operator} {number2}")
    result = calc(number1, calc_operator, number2)
    return result






