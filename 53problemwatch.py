import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):

    # if matches := re.search(r"^(https?://)?(www\.)?youtube\.com/embed/(.+)$", s, re.IGNORECASE):
    if matches := re.search(r"src=\"(https?://)?(www\.)?youtube\.com/embed/([a-zA-Z0-9_]+)", s, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(3)}"
    else:
        return None

if __name__ == "__main__":
    main()
