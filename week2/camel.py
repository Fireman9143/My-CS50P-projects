def main() -> None:
    user_text: str = input("camelCase: ")
    print(f"snake_case:", convert(user_text))

def convert(text) -> str:
    new = text
    for letter in text:
        if letter.isupper() and letter != text[0]:
            num = new.index(letter)
            new = new[:num] + "_" + new[num:]
    return new.lower()

if __name__ == "__main__":
    main()