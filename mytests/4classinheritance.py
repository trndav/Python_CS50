# Instead of using     
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
# in both classes Cat and Dog, we will create upper class Pet

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am a {self.age} years old")

    def speak(self):
        print("Nothing to say!")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # super() - reference super class (Pet())
        self.color = color

    def speak(self):
        print("Meow!")

    def show(self):
        print(f"I am {self.name} and I am a {self.age} years old, and I am {self.color}")

class Dog(Pet):    
    def speak(self):
        print("Woof!")

class Fish(Pet):
    pass

pet = Pet("Bob", 15)
pet.show()
pet.speak()
cat = Cat("Bill", 11, "white")
cat.show()

dog = Dog("Garo", 12)
dog.show()
dog.speak()
kitty = Cat("Mica", 7, "black")
kitty.show()
kitty.speak()

fish = Fish("Bubbles", 5)
fish.show()
fish.speak()