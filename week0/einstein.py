def main():
    while True:
        try:
            mass = int(input("What is the mass in kg? "))
            print(convert(mass))
            break
        except ValueError:
            print("Please enter a whole number")


def convert(number):
    return f"Energy= {number * 300_000_000**2:,} joules"

if __name__ == "__main__":
    main()