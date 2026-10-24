from ..games.brain_gcd import DESCRIPTION, gcd_question
from ..logic import ask_name, game


def main() -> None:
    name = ask_name()
    game(name, DESCRIPTION, gcd_question)