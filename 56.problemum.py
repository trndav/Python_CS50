import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    matches = re.findall(r"\b ?um[,!?\.*]?\b", s, re.IGNORECASE) 
    counter = len(matches)
    return counter

if __name__ == "__main__":
    main()
