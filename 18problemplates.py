def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    punc = "!\#$%&'()*+,-./:;<=>?@[]^_`{|}~"
    # Check lenght, first 2 chars is alpha, and no spaces.
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and " " not in s:
        # Check if input has punctiations
        for char in s:
            if char in punc:
                return False
        # Check if the first numeric character is '0'
        first_numeric = next((i for i, char in enumerate(s) if char.isdigit()), None)            
        if first_numeric is not None and s[first_numeric] == '0':
            return False
        # If string has number and all other characters are not number
        for char in s:
            if char.isdigit():
                if not s[first_numeric+1:].isdigit():
                    return False
        # Check if contains numbers and then if last char is alphabetic
        for char in s:
            if char.isdigit() and s[len(s)-1].isalpha():
                return False
        return True
main()