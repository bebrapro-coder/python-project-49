from ..logic import ask_name


def main() -> None:
    print("Welcome to the Brain Games!")
    name = ask_name()
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
