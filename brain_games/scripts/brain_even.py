from ..games.brain_even import DESCRIPTION, even_question
from ..logic import ask_name, game


def main() -> None:
    name = ask_name()
    game(name, DESCRIPTION, even_question)
