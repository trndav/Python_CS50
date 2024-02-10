# names = []
# for _ in range(3):
#     name = input("What is your name? ")
#     names.append(name)
#     print(f"Hi {name}")

# Or shorter:
# for _ in range(3):
#     names.append(input("What is your name? "))
# for name in sorted(names):
#     print(f"Hi {name}")    

# Save to file
# name = input("What is your name? ")
# file = open("40names.txt", "w")  # Open/create file for writing -w
# file.write(name) # Rewrite content
# file.close() # Close and save

# File append
# name = input("What is your name? ")
# file = open("40names.txt", "a")  # Open/create file for append -a
# file.write(name) # Rewrite content
# file.close() # Close and save

# Append with new line
# name = input("What is your name? ")
# file = open("40names.txt", "a")  # Open/create file for append -a
# file.write(f"{name}\n") # Rewrite content
# file.close() # Close and save

# WITH Append with new line without close
name = input("What is your name? ")
with open("40names.txt", "a") as file: # Open/create file for append -a
    file.write(f"{name}\n") # Rewrite content