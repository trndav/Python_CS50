# Read csv with split(",")
# with open("42names.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"Name is: {row[0]}, from {row[1]}")
#         #print(row)

# Cleaner
# with open("42names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"Name is: {name}, from {house}")

# Sort elements from file
# students = []
# with open("42names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")
# for student in sorted(students):
#     print(student)

# Dictionary
# students = []
# with open("42names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name 
#         student["house"] = house 
#         students.append(student)
# for student in students:
#     print(f"{student['name']} is in {student['house']}")

# Dictionary shorter:
# students = []
# with open("42names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
# for student in students:
#     print(f"{student['name']} is in {student['house']}")

# Sort CSV dictionary
# students = []
# with open("42names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
# def get_name(student):
#     return student["name"]
# for student in sorted(students, key=get_name, reverse=True): # key is sorted parameter
#     print(f"{student['name']} is in {student['house']}")

# Lambda function - anonymous function
# students = []
# with open("42names.csv") as file:
#     for line in file:
#         name, house, home = line.rstrip().split(",")
#         student = {"name": name, "home": home}
#         students.append(student)
# for student in sorted(students, key=lambda somename: student["name"], reverse=True): # key is sorted parameter
#     print(f"{student['name']} is in {student['home']}")

# CSV module CSV.reader - return lists
# import csv
# students = []
# with open("42names.csv") as file:
#     reader = csv.reader(file)
#     for name, home, place in reader:
#         students.append({"name": name, "home": home, "place": place})
# for student in sorted(students, key=lambda student: student["name"]): # key is sorted parameter
#     print(f"{student['name']} is in {student['home']} in {student['place']}")

# CSV.DictReader return dictionaries
# import csv
# students = []
# with open("42names.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"], "place": row["place"]})
# for student in sorted(students, key=lambda student: student["name"]): # key is sorted parameter
#     print(f"{student['name']} is in {student['home']} in {student['place']}")

# # Write to csv file with csv.writer
# import csv 
# name= input("What is your name? ")
# home = input("What is your home? ")
# with open("44namehome.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

# Write to csv file with csv.DictWriter
import csv 
name= input("What is your name? ")
home = input("What is your home? ")
with open("44namehome.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"], lineterminator='\n') # without lineterminator prints new line
    writer.writerow({"name": name, "home": home})



