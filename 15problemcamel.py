user_input = input("camelCase: ")

for letter in user_input:
    if letter.isupper():
        letter = letter.replace(letter, "_"+letter.lower())
    #print("snake_case: ", end="")
    print(letter, end="")
