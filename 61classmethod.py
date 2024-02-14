# Class Hat and its methods @classmethod -decorator
# import random

# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
#     def sort(self, name):
#         # house = random.choice(self.houses)
#         # print(name, "is in", house)
#         # Or shorter        
#         print(name, "is in", random.choice(self.houses))

# hat = Hat() # Instantiate object
# hat.sort("Harry")

# @classmethod -decorator - no need to instantiate
import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):      # @classmethod cls
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")
