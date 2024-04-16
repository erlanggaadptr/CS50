import pyfiglet
import random
import sys

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")

else:
    if len(sys.argv) == 1:
        f = pyfiglet.Figlet(font=random.choice(pyfiglet.FigletFont.getFonts()))

    if len(sys.argv) == 3:
        if sys.argv[1].lower() != '-f' and sys.argv[1].lower() != '--font':
            sys.exit("Invalid usage")

        try:
            f = pyfiglet.Figlet(font=sys.argv[2])

        except pyfiglet.FontNotFound:
            sys.exit("Invalid usage")

    print(f.renderText(str(input("Input: "))))
