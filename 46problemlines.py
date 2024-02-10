# Count number of linew without #comments and empty lines
import sys

if len(sys.argv) == 2:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")

filename = sys.argv[1]

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

linecounter = 0
for line in file:
    line = line.strip()
    if line.startswith('#'):
        continue
    elif line :
        linecounter = linecounter + 1

print(linecounter)
