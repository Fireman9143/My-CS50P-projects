def main():
    answer =input("What is the answer to the Great Question of Life, the Universe, and Everything?")
    if answer == "42" or answer.lower() == "forty-two" or answer.lower()== "forty two":
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()