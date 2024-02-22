class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return str(self.name) + ", " + str(self.age)

    def __del__(self):
        print("Object is deconstructed, deleted")

p = Person("Mike", 23)
print(p)
# del p # Deconstruct - delete
