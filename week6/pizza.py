import sys
import csv
from tabulate import tabulate

def main():
    if check():
        try:
            with open(sys.argv[1]) as file:
                table=csv.reader(file)
                print(tabulate(table, tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File Not Found")

def check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit(f"{sys.argv[1]}Not a CSV file")
    else:
        return True
    
if __name__ == "__main__":
    main()

"""In a file called pizza.py, implement a program that expects exactly one command-line argument, 
the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, 
a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. 
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, 
or if the specified file does not exist, the program should instead exit via sys.exit."""