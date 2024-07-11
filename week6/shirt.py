import sys
from PIL import Image, ImageOps


def main():
    if check():
        try:
            pic= Image.open(sys.argv[1])
            shirt=Image.open("shirt.png")
            size=shirt.size
            pic=ImageOps.fit(pic, size)
            pic.paste(shirt, shirt)
            pic.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("File not found")


def check():
    ext = ["jpg", "jpeg", "png"]
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        first, ext1 = sys.argv[1].split(".")
        second, ext2 = sys.argv[2].split(".")
        if ext2 not in ext:
            sys.exit("Invalid output")
        elif ext1 != ext2:
            sys.exit("Input and output have different extensions")
        else:
            return True

if __name__ == "__main__":
    main()