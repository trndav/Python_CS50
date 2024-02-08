import random

#print(random.choice(["Heads", "Tails"]))

# coin = random.choice(["Heads", "Tails"])
# print(coin)

# from random import choice
# coin = choice(["Heads", "Tails"])
# print(coin)

x = random.randint(1, 50)
print(f"Random 1-50: {x}")

cards = ["jack", "ace", "queen"]
random.shuffle(cards)
for card in cards:
    print(card)