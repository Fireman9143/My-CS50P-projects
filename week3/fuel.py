def main() -> None:
    while True:
        try:
            level=convert(input("Fraction: "))
            if level == False:
                raise ValueError
            else:
                print(gauge(level))
                break
        except ValueError:
            print("invalid entry")


def convert(fraction: str)->int:
    try:
        x, y=fraction.split("/")
        x=int(x)
        y=int(y)
        if x>y:
            raise ValueError
        elif y==0:
            raise ZeroDivisionError
        elif x==0:
            return "0"
        else:
            z=(x/y)*100
            z=int(z)
            return z
    except ValueError or ZeroDivisionError:
        return False


def gauge(percent:int)->str:
    if int(percent) <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"
    

def bug_convert(fraction: str)->int:
    try:
        x, y=fraction.split("/")
        x=int(x)
        y=int(y)
        if x>y:
            raise ValueError
        elif y==0:
            raise ZeroDivisionError
        elif x==0:
            return 0
        else:
            z=(x/y)*100
            z=int(z)
            return z
    except ValueError or ZeroDivisionError:
        return False


def bug_gauge(percent:int)->str:
    if int(percent) <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"percent%"

    
if __name__ == "__main__":
    main()