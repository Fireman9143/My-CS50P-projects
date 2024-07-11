import sys

def main():
    if check():
        try:
            lines=[]
            with open(sys.argv[1], "r") as file:
                for line in file:
                    if line.startswith("#") or line.startswith("\n"):
                        pass
                    else:
                        lines.append(line)
                print(lines)
                print(len(lines))
        except FileNotFoundError:
            sys.exit("File Not Found")

def check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")
    else:
        return True

if __name__ == "__main__":
    main()