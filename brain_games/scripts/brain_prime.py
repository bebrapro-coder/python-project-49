from ..games.brain_prime import DESCRIPTION, prime_question
from ..logic import ask_name, game


def main() -> None:
    name = ask_name()
    game(name, DESCRIPTION, prime_question)