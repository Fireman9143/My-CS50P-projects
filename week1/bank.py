def main():
    greet = input("Greeting: ")
    print(f"${value(greet)}")


def value(text):
    words = text.lower().replace(",", " ").split()
    if words[0]=="hello":
        return 0
    elif words[0].startswith("h"):
        return 20
    else:
        return 100


def bug(text):
    words = text.lower().replace(",", " ").split()
    if words[0]=="hello":
        return 100
    elif words[0].startswith("h"):
        return 20
    else:
        return 0


if __name__ == "__main__":
    main()