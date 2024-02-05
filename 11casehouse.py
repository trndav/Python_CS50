name = input("What is your name? ")

# if name == "Harry":
#     print("Griffindor")
# elif name == "Hermione":
#     print("Griffindor")
# elif name == "Ron":
#     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# Shorter
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Griffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# Match with case _:
# match name: 
#     case "Harry":
#         print("Griffindor")
#     case "Hermione":
#         print("Griffindor")
#     case "Ron":
#         print("Griffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:    # This case _: is for all other inputs that do not match.
#         print("Who?")

# Match shorter
match name: 
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:    # This case _: is for all other inputs that do not match.
        print("Who?")