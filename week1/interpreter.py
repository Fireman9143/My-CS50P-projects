def main():
    while True:
        try:
            x,y,z=input("Expression: ").split(" ")
            break
        except ValueError:
            print("Please enter an expression")
    if y == "+":
        print(add(x,z))
    elif y == "-":
        print(subtract(x,z))
    elif y == "*":
        print(multiply(x,z))
    elif y == "/":
        print(divide(x,z))
    else:
        print("Please enter x  +-*/  y  ")


def add(a,b):
    return float(a)+float(b)


def subtract(a,b):
    return float(a)-float(b)


def multiply(a,b):
    return float(a)*float(b)


def divide(a,b):
    return float(a)/float(b)


if __name__ == "__main__":
    main()