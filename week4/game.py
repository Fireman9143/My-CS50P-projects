import random
import sys

def main():
    while True:
        try:
            level=int(input("Level: "))
            if level < 1:
                raise ValueError
            else:
                break
        except ValueError:
            pass
    x=answer(level)
    while True:
        try:
            print(x)
            guess=int(input("Guess: "))
            if guess < 1:
                raise ValueError
            elif guess > level:
                print("Looks like you're guessing outside the range you specified")
            elif guess < x:
                print("Too small")
            elif guess > x:
                print("Too large")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass


def answer(n):
    return random.choice(range(1,n+1))

if __name__ == "__main__":
    main()