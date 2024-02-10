import sys
import csv

if len(sys.argv) == 3:
    if not sys.argv[1].endswith(".csv"):
        sys.exit(f"Not a CSV file")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")

filename = sys.argv[1]

list = []
with open(filename) as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        list.append(row)

lst2 = [[word.strip() for word in item.split(',')] + [house] for item, house in list]
lst3 = []
for item in lst2:
    lst3.append([item[1], item[0], item[2]])

header = ['first', 'last', 'house']
output = sys.argv[2]

with open(output, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(lst3)
