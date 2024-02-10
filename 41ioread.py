# with open("40names.txt", "r") as file:
#     lines = file.readlines() # Read all lines in file
# for line in lines:
#     print(f"Hi {line}", end="")
#     # or
#     # print(f"Hi {line.rstrip()}")

# Shorter
# with open("40names.txt", "r") as file:
#     for line in file:
#         print(f"Hi {line.rstrip()}")

# Read and sort with list - append to list
# names = []
# with open("40names.txt") as file: # Read file is default without "r" parameter
#     for line in file:
#         names.append(line.rstrip())
# print(names)
# for name in sorted(names):
#     print(f"Hi {name}")

# Shorter

with open("40names.txt") as file: # Read file is default without "r" parameter
    for line in sorted(file, reverse=True): # Sorted reverse order
        print(f"Hi {line.rstrip()}")
