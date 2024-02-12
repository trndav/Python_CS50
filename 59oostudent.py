# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()
#     # Or
#     # name, house = get_student()
#     # print(f"{name} from {house}")
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house) # Tuple

# if __name__ == "__main__":
#     main()

# # List
# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw" 
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # return (name, house) # Tuple immutable - not changeable
#     # Or
#     return [name, house]

# if __name__ == "__main__":
#     main()

# Dictionary
# def main():
#     student = get_student()    
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ") 
#     return student

# if __name__ == "__main__":
#     main()

# Dictionary shorter
# def main():
#     student = get_student()    
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ") 
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()

# CLASSES - create own data types
# Dictionary shorter
# class Student:
#     ...

# def main():
#     student = get_student()  
#     print(f"{student.name} from {student.house}")

# def get_student():
#     student = Student()
#     student.name = input("Name: ") # Class student
#     student.house = input("House: ") # Class student
#     return student

# if __name__ == "__main__":
#     main()


# Class objects
# class Student:
#     def __init__(self, name, house):  # Instance method - initialization of object
#         self.name = name
#         self.house = house

# def main():
#     student = get_student()  
#     print(f"{student.name} from {student.house}")

# def get_student():    
#     name = input("Name: ") 
#     house = input("House: ")
#     student = Student(name, house) # Constructor call - instantiate student object
#     return student

# if __name__ == "__main__":
#     main()

# # Class objects
# class Student:
#     def __init__(self, name, house):  # Instance method - initialization of object
#         if not name:
#             #sys.exit("Missing name")  # Import sys
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house

# def main():
#     student = get_student()  
#     print(f"{student.name} from {student.house}")

# def get_student():    
#     name = input("Name: ") 
#     house = input("House: ")   
#     return Student(name, house)

# if __name__ == "__main__":
#     main()

# Class objects __str__ prints string instead of memory
# Function inside class is method
# class Student:
#     def __init__(self, name, house, patronus):  # Instance method - initialization of object
#         if not name:
#             #sys.exit("Missing name")  # Import sys
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#         self.patronus = patronus
#     def __str__(self):
#         return f"{self.name} from {self.house}, has patronus {self.patronus}" # method prints "a student" when print(student) is called

#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "🐴"
#             case "Otter":
#                 return "🦦"
#             case "Russel":
#                 return "🐶"
#             case _:
#                 return "None"      

# def main():
#     student = get_student()  
#     print("Expecto Patronum!")
#     print(student.charm())

# def get_student():    
#     name = input("Name: ") 
#     house = input("House: ")   
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus)

# if __name__ == "__main__":
#     main()

# Class objects __str__ prints string instead of memory
# Function inside class is method
# Properties @property for house
# class Student:
#     def __init__(self, name, house):  # Instance method - initialization of object
#         if not name:
#             #sys.exit("Missing name")  # Import sys
#             raise ValueError("Missing name")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}" # method prints "a student" when print(student) is called
    
#     # Getter
#     @property
#     def house(self):
#         return self._house # To avoid collision with self.name = house in __init__

#     # Setter
#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house # To avoid collision with self.name = house in __init__

# def main():
#     student = get_student()
#     # student.house = "Some other address like hack" # Skip validations
#     print(student)

# def get_student():    
#     name = input("Name: ") 
#     house = input("House: ")   
#     return Student(name, house) Constructor call

# if __name__ == "__main__":
#     main()

# Properties @property for house AND name
class Student:
    def __init__(self, name, house):  # Instance method - initialization of object
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}" # method prints "a student" when print(student) is called
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house # To avoid collision with self.name = house in __init__

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house # To avoid collision with self.name = house in __init__

def main():
    student = get_student()
    # student._house = "Some other address like hack" # Skip validations _house
    print(student)

def get_student():    
    name = input("Name: ") 
    house = input("House: ")   
    return Student(name, house) #Constructor call

if __name__ == "__main__":
    main()