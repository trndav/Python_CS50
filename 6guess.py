def get_guess():
    guess = input("Enter a guess: ")
    return guess 

def main():
    guess = int(get_guess())
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")

main()