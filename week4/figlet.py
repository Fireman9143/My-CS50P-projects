from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

def main():
    if check():
        text=input("Input: ")
    if len(sys.argv) == 1:
        font=random.choice(fonts)
        figlet.setFont(font=font)
        print(figlet.renderText(text))
    else:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    
def check():
    if len(sys.argv) == 1: #expects 0 command line arguments
        return True
    elif len(sys.argv) == 3 and sys.argv[2] in fonts: #expects 2 command line arguments
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            return True
        else:
            sys.exit()
    else:
        sys.exit()


if __name__ == "__main__":
    main()