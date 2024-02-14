# class Wizard:
#     def __init__(self, name):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name
#         self.house = house 
    
# class Professor:
#     def __init__(self, name, subject):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name 
#         self.subject = subject

# Inherit from Wizard - redundance
# 1 class inherit, descend from another
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house 
    
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Serverus", "Defence against the Dark Arts")

print(wizard.name, student.name, student.house, professor.name, professor.subject)