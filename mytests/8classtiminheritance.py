
class Dog(object):
    def __init__(self, name, age): #Constructor
        self.name = name # attribute
        self.age = age
        
    def speak(self):
        print(f"Woof! I am {self.name}! I am {self.age} old.")

    def talk(self):
        print("Woof!")

class Cat(Dog):
    def __init__(self, name, age, color): #Constructor
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"I am {self.name}! I am {self.age} old and I am {self.color}.")
    
    def talk(self):
        print("Meaow!")

tim = Cat("Bob", 12, "White")
tim.speak()
bob = Dog("Bob", 14)
bob.speak()
bob.talk()
tim.talk()