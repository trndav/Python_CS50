# Test with 2 arguments (or none) like: python figlet.py -f computer/cola/ghoulish
import sys
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            user_input = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(f"{figlet.renderText(user_input)}")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    user_input = input("Input: ")
    print(figlet.renderText(user_input))
else:
    sys.exit("Invalid usage")
