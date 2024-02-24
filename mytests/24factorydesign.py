from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        ''' Interface method '''  
        
class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student"

    def person_method(self):
        print("I am student")
    
class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher"

    def person_method(self):
        print("I am teacher")
        
class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid type")
        return -1

if __name__ == "__main__":
    choice = input("What type of person you want to create\n")
    person = PersonFactory.build_person(choice)
    person.person_method()

