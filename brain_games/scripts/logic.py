def ask_name() -> str:
    name = ""
    while name == "":
        name = input("May I have your name? ")
    return name

