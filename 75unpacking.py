# unpacking 

# 2 variables for input
# first, last = input("What is your name? ").split(" ")
# print(f"Hi {first} of the family {last}")

# unpacking example
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins: list= [100, 50, 25]

# print(total(100, 50, 25), "knuts.")
# print(total(coins[0], coins[1], coins[2]), "knuts.")
# print(total(galleons=100, sickles=50, knuts=25), "knuts.")

# unpacking list
# print(total(*coins), "knuts.") # unpacking

# unpacking dictionary
coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts.")
print(total(**coins), "knuts.") # unpacking


