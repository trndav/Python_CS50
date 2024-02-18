
class Person:
    number_of_people = 0 # Class attribute 

    def __init__(self, name):
        self.name = name
        Person.add_person()
        # Person.number_of_people += 1
    
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    
p1 = Person("Tim")
print(f"Person.number_of_people(): {Person.number_of_people_()}")
# print(f"Person.number_of_people: {Person.number_of_people}")
# print(f"p1= {p1.number_of_people}")

p2 = Person("Bob")
print(f"Person.number_of_people(): {Person.number_of_people_()}")
# print(f"Person.number_of_people: {Person.number_of_people}")
# Person.number_of_people = 5


