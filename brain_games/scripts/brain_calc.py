from ..games.brain_calc import DESCRIPTION, calc_question
from ..logic import ask_name, game


def main() -> None:
    name = ask_name()
    game(name, DESCRIPTION, calc_question)
