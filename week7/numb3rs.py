import re
import sys


def main():
    try:
        print(validate(input("IPv4 Address: ")))
    except ValueError:
        sys.exit("invalid entry")


def validate(ip):
    if addy := re.search(r"^(..?.?)\.(..?.?)\.(..?.?)\.(..?.?)$", ip):
        for set in addy.groups():
            if int(set) in range(0,256):
                return True
            else:
                return False
    else:
        return False
    
    
def bug_validate(ip):
    if addy := re.search(r"^(..?.?)\.(..?.?)\.(..?.?)\.(..?.?)$", ip):
        for set in addy.groups():
            if int(set) in range(0,255):
                return True
            else:
                return False
    else:
        return False


if __name__ == "__main__":
    main()