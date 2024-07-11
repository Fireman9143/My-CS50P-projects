import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if text := re.findall(r"\bum", s.lower(), re.IGNORECASE):
        return len(text)
    

def bug_count(s):
    if text := re.findall(r" um ", s.lower(), re.IGNORECASE):
        return len(text)
    


if __name__ == "__main__":
    main()