class Person:

    people_num = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people_num += 1

    def __del__(self):
        print("Object deleted!") # Use like del p1
        Person.people_num -= 1

    def __str__(self):
        return f"prints string like {self.name} and {self.age}." # Use like print(p1)
    
    def get_older(self, years):
        self.age += years

p1 = Person("Bob", 25)
print(p1)
print(p1.name)
print(p1.age)
p1.get_older(5)
print(p1)
print(Person.people_num)
p2 = Person("Toby", 44)
print(Person.people_num)