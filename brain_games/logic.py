ROUNDS_COUNT = 3

def ask_name() -> str:
    name = ""
    while name == "":
        name = input("May I have your name? ")
    return name

def start(name: str, description: str) -> None:
    print(f"Hello, {name}!")
    print(description)

def answer() -> str:
    result = input("Your answer: ")
    return result

def check_answer(name: str, correct: int | str, user_answer: str) -> bool:
    if user_answer == str(correct):
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        print(f"Let's try again, {name}!")
        return False

def game(name: str, description: str, question) -> None:
    start(name, description)
    for i in range(ROUNDS_COUNT):
        correct = question()
        user_answer = answer()
        if not check_answer(name, correct, user_answer):
            return
    print(f"Congratulations, {name}!")

