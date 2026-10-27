from ..games.brain_progression import DESCRIPTION, progression_question
from ..logic import game


def main() -> None:
    game(DESCRIPTION, progression_question)
