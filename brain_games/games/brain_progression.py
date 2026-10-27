import random

MIN_NUMBER = 1
MAX_NUMBER = 99
PROGRESSION_LENGTH = 10
DESCRIPTION = "What number is missing in the progression?"


def progression(first_number: int, step: int, length: int) -> list[int]:
    return [first_number + i * step for i in range(length)]


def progression_question() -> tuple[str, str]:
    step = random.randint(MIN_NUMBER, MAX_NUMBER)
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_index = random.randint(0, PROGRESSION_LENGTH - 1)
    final_progression = progression(first_number, step, PROGRESSION_LENGTH)
    progression_answer = final_progression[random_index]
    final_progression[random_index] = ".."
    final_progression = map(str, final_progression)
    final_progression = " ".join(final_progression)
    return final_progression, str(progression_answer)
