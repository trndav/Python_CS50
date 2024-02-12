
# name = input(" What is your name? ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"Hi, {name}!")

import re
# If Lastname, Firstname then Frist Last, if First Last then no changes
# name = input(" What is your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name) # groups
# if matches:
#     last, first = matches.groups()  # match groups
#     name = f"{first} {last}"

# print(f"Hi, {name}!")

# Longer
# name = input(" What is your name? ").strip()
# matches = re.search(r"^(.+), *(.+)$", name) # groups
# if matches:
#     # last = matches.group(1) 
#     # first = matches.group(2)  # match groups
#     # name = f"{first} {last}"
#     # Or Simpler. shorter
#     name = matches.group(2) + " " + matches.group(1)
# print(f"Hi, {name}!")

# Very short
name = input(" What is your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name): # groups  := assignment and bool operator
    name = matches.group(2) + " " + matches.group(1)
print(f"Hi, {name}!")