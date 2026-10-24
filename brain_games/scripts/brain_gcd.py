import random
from .logic import *

def gcd(number1: int, number2: int) -> int:
    while number2 != 0:
        remain = number1 % number2
        number1 = number2
        number2 = remain
    return number1

def gcd_question():
    number1 = random.randint(1,99)
    number2 = random.randint(1, 99)
    final_gcd = gcd(number1, number2)
    numbers = f"{number1} {number2}"
    print(f"Question: {numbers}")
    return final_gcd

def main() -> None:
    name = ask_name()
    game(name,"Find the greatest common divisor of given numbers.", gcd_question)

