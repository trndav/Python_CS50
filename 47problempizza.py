# pip install tabulate  -for csv to table ASCI
# Add as argument csv file like python pizza.py name.csv
import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 2:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")

filename = sys.argv[1]
table = []
try:
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

headers = table.pop(0)
print(tabulate(table, headers, tablefmt="grid"))
