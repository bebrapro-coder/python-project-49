from ..logic import ask_name


def main() -> None:
    name = ask_name()
    print(f"Welcome to the Brain Games, {name}!")

if __name__ == "__main__":
    main()
