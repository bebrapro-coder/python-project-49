from .logic import ask_name
name = ask_name()

def main() -> str:
    print(f"Welcome to the Brain Games, {name}!")

if __name__ == "__main__":
    main()