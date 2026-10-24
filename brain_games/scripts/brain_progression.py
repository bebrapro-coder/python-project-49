import random
from .logic import *

def progression(first_number: int, step: int):
    numbers = [first_number]
    number = 0
    for i in range(9):
        if number <= first_number:
            number += first_number + step
            numbers.append(number)
        else:
            number += step
            numbers.append(number)
    return numbers

def progression_question():
    step = random.randint(1, 99)
    first_number = random.randint(1, 99)
    random_index = random.randint(0, 9)
    final_progression = progression(first_number, step)
    progression_answer = final_progression[random_index]
    final_progression[random_index] = ".."
    final_progression = map(str, final_progression)
    final_progression = " ".join(final_progression)
    print(f"Question: {final_progression}")
    return progression_answer

def main() -> None:
    name = ask_name()
    game(name,"What number is missing in the progression?", progression_question)