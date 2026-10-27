from ..games.brain_calc import DESCRIPTION, calc_question
from ..logic import game


def main() -> None:
    game(DESCRIPTION, calc_question)
