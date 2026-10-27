from ..games.brain_prime import DESCRIPTION, prime_question
from ..logic import game


def main() -> None:
    game(DESCRIPTION, prime_question)
