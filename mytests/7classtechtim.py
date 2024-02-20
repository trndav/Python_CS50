
class Dog(object):
    def __init__(self, name, age): #Constructor
        self.name = name # attribute
        self.age = age
        print("This is dog!")
        
    def speak(self):
        print(f"Woof! I am {self.name}! I am {self.age} old.")

    def change_age(self, age):
        self.age = age
    
    def add_weight(self, weight):
        self.weight = weight

tim= Dog("Tim", 8) # or tim = __init__ ?
tim.speak()
tim.change_age(9)
tim.speak()
print(tim.age)
print(tim.name)
tim.add_weight(25)
print(tim.weight)