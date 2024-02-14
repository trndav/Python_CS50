# Constants shout be uppercase

# MEOWS = 3 # Constant

# for _ in range(MEOWS):
#     print("meow")

# Class constant MEOWS
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()