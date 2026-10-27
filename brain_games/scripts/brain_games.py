from ..logic import ask_name, welcome


def main() -> None:
    welcome()
    name = ask_name()
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
