# Converts inputs to format: xx, xx, xx, and xx
# pip install inflect

import inflect

p = inflect.engine()
lst = []
while True:
    try:
        user_input = input("Name: ")
        lst.append(user_input)
    except EOFError:
        print()
        inflectlist = p.join(lst, ",")
        print(f"Adieu, adieu, to {inflectlist}")
        break


