import random
from .logic import ask_name
name = ask_name()

def even_start():
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

def even_question() -> int:
    number = random.randint(1, 99)
    print(f"Question: {number}")
    return number


def even_answer() -> str:
    return input("Your answer: ")

def check_answer(number: int, user_answer: str) -> bool:
    if number % 2 == 0:
        correct = "yes"
    else:
        correct = "no"
    if user_answer == correct:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        print(f"Let's try again, {name}!")
        return False

def even_game():
    even_start()
    for i in range(3):
        number = even_question()
        user_answer = even_answer()
        if not check_answer(number, user_answer):
            return
    print(f"Congratulations, {name}!")

def main() -> None:
    even_game()




