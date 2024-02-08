# Enter max number and guess random generated number
import random

while True:
    level = input("Level: ")
    if not level.isnumeric():
        continue
    level = int(level)
    if level <= 0:
        continue
    rand = random.randint(1, level)
    #print(f"Random is: {rand}")

    while True:
        guess = input("Guess: ")
        if guess.isnumeric():
            guess = int(guess)
            if guess < rand:
                print("Too small!")
            elif guess > rand:
                print("Too large!")
            else:
                print("Just right!")
                break
        else:
            continue
    break
