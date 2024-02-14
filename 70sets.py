# Count unique houses

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

# for house in sorted(houses):
#     print(house)

houses = set() # Set accepts no duplicates
for student in students:
    houses.add(student["house"]) # for sets it is add

for house in sorted(houses):
    print(house)