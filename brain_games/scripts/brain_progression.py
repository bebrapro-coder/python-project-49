from ..games.brain_progression import DESCRIPTION, progression_question
from ..logic import ask_name, game


def main() -> None:
    name = ask_name()
    game(name, DESCRIPTION, progression_question)
