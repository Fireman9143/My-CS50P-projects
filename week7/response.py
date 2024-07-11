import validators

def main():
    if email:= validators.email(input("What's your email?: ")):
        print("Valid")
    else:
        print("Invalid")

        
if __name__ == "__main__":
    main()