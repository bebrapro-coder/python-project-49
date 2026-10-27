import prompt

ROUNDS_COUNT = 3


def welcome() -> None:
    print("Welcome to the Brain Games!")


def ask_name() -> str:
    name = ""
    while name == "":
        name = prompt.string("May I have your name? ")
    return name


def start(name: str, description: str) -> None:
    print(f"Hello, {name}!")
    print(description)


def answer() -> str:
    result = prompt.string("Your answer: ")
    return result


def check_answer(name: str, correct: int | str, user_answer: str) -> bool:
    if user_answer == str(correct):
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        print(f"Let's try again, {name}!")
        return False


def game(description: str, question) -> None:
    welcome()
    name = ask_name()
    start(name, description)
    for i in range(ROUNDS_COUNT):
        question_text, correct = question()
        print(f"Question: {question_text}")
        user_answer = answer()
        if not check_answer(name, correct, user_answer):
            return
    print(f"Congratulations, {name}!")
