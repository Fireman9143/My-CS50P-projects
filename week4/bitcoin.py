import sys
import requests

def main():
    if check():
        try:
            bits=float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    elif len(sys.argv) <2:
        sys.exit("Missing command-line arguments")
    else:
        sys.exit("Incorrect arguements")

    try:
        query=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except requests.RequestException:
        sys.exit("unable to process request")
    
    bpi = query['bpi']
    USD = bpi['USD']
    rate = USD['rate_float']
    price = bits * rate
    print(f"One bitcoin is ${price:,.4f} USD")


def check():
    if len(sys.argv) != 2:
        return False
    elif len(sys.argv) ==2:
        return True


if __name__ == "__main__":
    main()