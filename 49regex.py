# .   any character except a new line
# *   0 or more repetitions
# +   1 or more repetitions
# ?   0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions
# \    escape next character
# ^    matches start of string
# $    matches end of string
# []    set of characters
# [^]   complementing the set any character except @ example [^@]
# \w alphanumeric

# if "@" in email and "." in email:
#     print("Valid!")
# else:
#     print("Invalid!")
####
# username, domain = email.split("@")
# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

import re
email = input("What is your email? ").strip() # can add .lower()

#if re.search(r"^[^@!.]+@[^@]+\.edu$", email): # r - raw string
# if re.search(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.edu$", email):
# if re.search(r"^\w+@\w+\.edu$", email):
# if re.search(r"^\w+@\w+\.(com|edu|gov|net)$", email): # can add , email.lower()
# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
# if re.search(r"^\w+@(\w+\.)*\w+\.edu$", email, re.IGNORECASE):  # name@has.asd.asd.edu
# if re.search(r"^(\w|\.)+@(\w+\.)*\w+\.edu$", email, re.IGNORECASE): # asd..asd@asd.asd.edu
# if re.search(r"^[a-zA-Z0-9_\.]+@(\w+\.)*\w+\.edu$", email, re.IGNORECASE): # asd..asd@asd.asd.edu
if re.search(r"^\w\.+@(\w+\.)*\w+\.edu$", email, re.IGNORECASE): 
    print("Valid")
else:
    print("Invalid")