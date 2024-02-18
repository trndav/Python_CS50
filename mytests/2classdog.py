
class Dog:
    def __init__(self, name, age):  # Allows to pass arguments to Dog()
        self.name = name
        self.age = age
        print(name,age)

    def bark(self):
        print("Woof!")

    def get_name(self):
            return self.name
    
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

dog = Dog("Sasa", 6)
dog2 = Dog("Garo", 8)

dog.bark()
print(dog.get_name())
print(dog.get_age())
dog.set_age(7)
print(dog.get_age())