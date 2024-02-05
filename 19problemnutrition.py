user_input = input("Item: ")
x = user_input.lower()

dictionary = {"apple": "130", "avocado": "50", "sweet cherries": "100", "kiwifruit": "90", "pear": "100"}

if x in dictionary:
    print(f"Calories: {dictionary[x]}")
else:
    print("")
