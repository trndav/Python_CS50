# dict compehension

# students = ["Hermione", "Harry", "Ron"]
# gryffindors = []
# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})
# print(gryffindors)

# dict comprehension   -argument for student in students
# students = ["Hermione", "Harry", "Ron"]
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
# print(gryffindors)

# dictionary comprehension
# students = ["Hermione", "Harry", "Ron"]
# gryffindors = {student: "Gryffindor" for student in students}
# print(gryffindors)

# enumerate
students = ["Hermione", "Harry", "Ron"]
for i, student in enumerate(students):
    print(i + 1, students[i])