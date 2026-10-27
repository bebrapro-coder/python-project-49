from ..games.brain_gcd import DESCRIPTION, gcd_question
from ..logic import game


def main() -> None:
    game(DESCRIPTION, gcd_question)
