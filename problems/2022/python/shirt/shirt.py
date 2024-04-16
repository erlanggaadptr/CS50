from PIL import Image, ImageOps
import sys


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")

    elif sys.argv[1].split(".")[1].lower() != sys.argv[2].split(".")[1].lower():
        sys.exit("Input and output have different extensions")

    try:
        open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("File does not exist")

    with Image.open('shirt.png') as shirt:
        with Image.open(sys.argv[1]) as before:
            resized = ImageOps.fit(before, shirt.size)
            resized.paste(shirt, shirt)
            resized.save(sys.argv[2])


if __name__ == '__main__':
    main()
