def main():
    text = input("Enter your message here: ")
    print(convert(text))


def convert(message):
    words = []
    for i in message.split():
        if i == ":)":
            i ="🙂"
            words.append(i)
        elif i == ":(":
            i = "🙁"
            words.append(i)
        else:
            words.append(i)
    return " ".join(words)

if __name__ == "__main__":
    main()