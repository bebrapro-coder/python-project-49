import random

MIN_NUMBER = 1
MAX_NUMBER = 99
MIN_HIDDEN_INDEX = 0
MAX_HIDDEN_INDEX = 9
PROGRESSION_LENGTH = 9
DESCRIPTION = "What number is missing in the progression?"

def progression(first_number: int, step: int) -> list[int]:
    numbers = [first_number]
    number = 0
    for i in range(PROGRESSION_LENGTH):
        if number <= first_number:
            number += first_number + step
            numbers.append(number)
        else:
            number += step
            numbers.append(number)
    return numbers

def progression_question() -> int:
    step = random.randint(MIN_NUMBER, MAX_NUMBER)
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_index = random.randint(MIN_HIDDEN_INDEX, MAX_HIDDEN_INDEX)
    final_progression = progression(first_number, step)
    progression_answer = final_progression[random_index]
    final_progression[random_index] = ".."
    final_progression = map(str, final_progression)
    final_progression = " ".join(final_progression)
    print(f"Question: {final_progression}")
    return progression_answer
