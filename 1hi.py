# Print and input function
a = "world"
print("Hi with double quotes like 'this'")
print("Double quotes with backslash \"this\"")
print(f"Hi there beautiful {a}!")
print("Hi there beautiful " + a + "!")
print(a)

# Say hi to user
name = input("What is your name? ")
print(f"Hi {name}!")

# print(*objects, sep=' ', end='\n', file=None, flush=False)
print("No new line: ", end="") # Skip newline \n
print(name)

# # Strip whitespaces
# name = name.strip()

# # Capitalize input name = name.capitalize()
# # Title input, each word capitalized
# name = name.title()

# Chain functions
name = name.strip().title()

# For multiple arguments. , adds space before argument
print("Multiple arguments with modified separator, with whitespace strip and capitalize: ", name, sep="x ")
# Or:
# name = input("What is your name? ")name.strip().title()
# print("Input strip and capitalize in 2 lines: ", name, sep="x ")

# Name split
first, last = name.split(" ")
print(f"First name is: {first}, and last name is {last}.")


'''
Multiple
line
comment
'''