import sys
import csv


def main():
    try:
        if check():
            students=[]
            with open(sys.argv[1]) as old:
                file = csv.DictReader(old)
                for row in file:
                    last, first=row['name'].split()
                    house=row['house']
                    students.append({"first":first, "last":last.rstrip(","), "house":house})
                print(students)
            with open(sys.argv[2], 'w') as new:
                new_file=csv.DictWriter(new, fieldnames=['first', 'last', 'house'])
                new_file.writeheader()
                for i in students:
                    new_file.writerow({'first':i['first'], 'last':i['last'], 'house':i['house']})
    except FileNotFoundError:
        sys.exit("File Not Found")


def check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit(f"{sys.argv[1]}Not a CSV file")
    else:
        return True
    

if __name__ == "__main__":
    main()