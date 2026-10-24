from ..logic import ask_name


def main() -> None:
    print(f"Welcome to the Brain Games, {name}!")

if __name__ == "__main__":
    name = ask_name()
    main()