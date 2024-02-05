# students = ["Hermione", "Harry", "Ron"]
# print(students)
# print(students[0])
# print(students[0:2])
# print(students[0:])
# for student in students:
#     print(student)
# for i in range(len(students)):
#     print(f"Iteration with range(len(x)): {i}")
# for i in range(len(students)):
#     print(f"Iteration with range(len(x)) and x[i]: {students[i]}")
# for i in range(len(students)):
#     print(i, students[i])
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
# students = {"Hermione": "Gryffindor", "Harry": "Gryffindor",
#             "Ron": "Gryffindor", "Draco": "Syltherin"}
# print(f"Check Hermione: {students['Hermione']}")
# print(f"check Draco: {students['Draco']}")
# for student in students:
#     print(student)
# for student in students:
#     print(student, students[student], sep=", ")

# List of dictionaries
students = [{"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
            {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
            {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
            {"name": "Draco", "house": "Syltherin", "patronus": None}]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")