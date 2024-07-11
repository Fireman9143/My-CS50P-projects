def main() -> None:
    twttr=input("Input: ")
    print(shorten(twttr))


def shorten(words):
    vowels = ["a", "e", "i", "o", "u"]
    final = words
    for i in words:
        if i.lower() in vowels:
            final = final.replace(i, "")
    return final


def bug(words):
    vowels = ["a", "e", "i", "o", "u"]
    final = words
    for i in words:
        if i in vowels:
            final = final.replace(i, "")
    return final


if __name__ == "__main__":
    main()