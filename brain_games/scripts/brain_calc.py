import random
from .logic import ask_name
name = ask_name()

def calc_start():
    print(f"Hello, {name}!")
    print("What is the result of this expression?")

def calc_question() -> int:
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    calc_operator = random.choice(["+", "-", "*"])
    print(f"Question: {number1} {calc_operator} {number2}")
    if calc_operator == "+":
        return number1 + number2
    elif calc_operator == "-":
        return number1 - number2
    else:
        return number1 * number2

def calc_answer() -> str:
    return input("Your answer: ")

def check_answer(correct: int, user_answer: str) -> bool:
    if user_answer == str(correct):
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        print(f"Let's try again, {name}!")
        return False

def calc_game():
    calc_start()
    for i in range(3):
        correct = calc_question()
        user_answer = calc_answer()
        if not check_answer(correct, user_answer):
            return
    print(f"Congratulations, {name}!")

def main() -> None:
    calc_game()






